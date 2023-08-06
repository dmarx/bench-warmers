import git
import json
import logging
import time
from typing import List, Union

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)
from loguru import logger

GIT_REPO = git.Repo('.')

# def get_commits_from_blame(fpath: str, repo: git.Repo =GIT_REPO) -> List[git.Commit]:
#     """
#     Get commit hashes from the output of 'git blame' for a file.

#     Args:
#         fpath (str): The file path.

#     Returns:
#         list: A list of commit objects.
#     """
#     result = subprocess.run(['git', 'blame', '--line-porcelain', fpath], capture_output=True, text=True)
#     lines = result.stdout.split('\n')
#     commit_lines = [line for line in lines if line.startswith('commit ')]
#     commit_hashes = [line.split()[1] for line in commit_lines]

#     commits = [repo.commit(hash_) for hash_ in commit_hashes]

#     return commits

def get_commits_from_blame(fpath: str, repo: git.Repo =GIT_REPO) -> List[git.Commit]:
    """
    Get commit hashes from the output of 'git blame' for a file.

    Args:
        fpath (str): The file path.

    Returns:
        list: A list of commit objects.
    """
    result = subprocess.run(['git', 'blame', '--line-porcelain', fpath], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    commit_hashes = [line for line in lines if re.match(r'^[0-9a-f]{40}$', line)]
    commit_hashes = list(dict.fromkeys(commit_hashes))  # remove duplicates while preserving order

    commits = [repo.commit(hash_) for hash_ in commit_hashes]

    return commits


def get_file_commits(fpath: str, repo: git.Repo =GIT_REPO) -> List[git.Commit]:
    """Get all commits for a file in reverse chronological order."""
    commits = list(repo.iter_commits(paths=fpath))
    commits += get_commits_from_blame(fpath) # possibly gets us some commits from old filenames
    return list(set(commits))

def get_diffs_for_file(commit: git.Commit, fpath: str) -> list:
    """
    Get the diffs associated with a file in a given commit.

    Args:
        commit (git.Commit): The commit to check.
        fpath (str): The file path to check.

    Returns:
        list: A list of git.Diff objects associated with the file.
    """
    diffs = []
    for parent in commit.parents:
        diff_index = parent.diff(commit)
        diffs.extend([d for d in diff_index.iter_change_type('M') if d.a_path == fpath or d.b_path == fpath])

    return diffs


def is_automated_user(commit: git.Commit) -> bool:
    """Check if a commit is by an automated user."""
    automated_users = ["action@github.com"] # Add other automated users if needed
    return commit.author.email in automated_users

def is_rename_only(commit: git.Commit, fpath: str) -> bool:
    """Check if a commit only renames or moves the file."""
    try:
        diffs = commit.parents[0].diff(commit)
    except IndexError:
        logger.error("No parent found for commit")
        return False

    for diff in diffs.iter_change_type('R'):
        if diff.a_blob.path == fpath or diff.b_blob.path == fpath:
            return True
    return False

# def is_tag_change_only(commit: git.Commit, fpath: str) -> bool:
#     """Check if a commit only changes the tags of the file."""
#     try:
#         diffs = commit.parents[0].diff(commit)
#     except IndexError:
#         logger.error("No parent found for commit")
#         return False

#     for diff in diffs.iter_change_type('M'):
#         if diff.a_blob.path == fpath or diff.b_blob.path == fpath:
#             diff_lines = diff.a_blob.data_stream.read().decode().split('\n')
#             new_lines = diff.b_blob.data_stream.read().decode().split('\n')
#             old_tags = diff_lines[2] if len(diff_lines) > 2 else ''
#             new_tags = new_lines[2] if len(new_lines) > 2 else ''
#             unchanged_lines = [old == new for old, new in zip(diff_lines, new_lines)]
#             if len(unchanged_lines) > 2:
#                 unchanged_lines[2] = True
#             if all(unchanged_lines) and old_tags != new_tags:
#                 return True
#     return False

def is_tag_change_only(commit: git.Commit, fpath: str) -> bool:
    """Check if a commit only changes the tags of the file."""
    try:
        diffs = commit.parents[0].diff(commit)
    except IndexError:
        logger.error("No parent found for commit")
        return False

    for diff in diffs.iter_change_type('M'):
        if diff.a_blob.path == fpath or diff.b_blob.path == fpath:
            diff_lines = diff.a_blob.data_stream.read().decode().split('\n')
            new_lines = diff.b_blob.data_stream.read().decode().split('\n')
            
            old_tags_line = next((line for line in diff_lines if line.startswith("labels:")), '')
            new_tags_line = next((line for line in new_lines if line.startswith("labels:")), '')

            unchanged_lines = [old == new for old, new in zip(diff_lines, new_lines)]
            
            if old_tags_line or new_tags_line:  # if either file has a labels line
                index = diff_lines.index(old_tags_line) if old_tags_line in diff_lines else new_lines.index(new_tags_line)
                unchanged_lines[index] = True
            
            if all(unchanged_lines) and old_tags_line != new_tags_line:
                return True
    return False


def is_title_change_only(commit: git.Commit, fpath: str) -> bool:
    """Check if a commit only changes the title of the file."""
    try:
        diffs = commit.parents[0].diff(commit)
    except IndexError:
        logger.error("No parent found for commit")
        return False

    for diff in diffs.iter_change_type('M'):
        if diff.a_blob.path == fpath or diff.b_blob.path == fpath:
            diff_lines = diff.a_blob.data_stream.read().decode().split('\n')
            new_lines = diff.b_blob.data_stream.read().decode().split('\n')
            old_title = diff_lines[0] if len(diff_lines) > 0 and diff_lines[0].startswith('# ') else ''
            new_title = new_lines[0] if len(new_lines) > 0 and new_lines[0].startswith('# ') else ''
            unchanged_lines = [old.strip() == new.strip() for old, new in zip(diff_lines, new_lines)]
            if len(unchanged_lines) > 0:
                unchanged_lines[0] = True
            if all(unchanged_lines) and old_title != new_title:
                return True
    return False

def is_badge_change_only(commit: git.Commit, fpath: str) -> bool:
    """
    Check if a commit only modifies the tags of a file.
    
    Args:
        commit (git.Commit): The commit to check.
        fpath (str): The file path to check.

    Returns:
        bool: True if the commit only modifies the tags of the file, False otherwise.
    """
    diffs = get_diffs_for_file(commit, fpath)
    for diff in diffs:
        old_lines = diff.a_blob.data_stream.read().decode().split('\n')
        new_lines = diff.b_blob.data_stream.read().decode().split('\n')

        old_lines_no_badges = [line for line in old_lines if not re.match(r'^!\[\]', line)]
        new_lines_no_badges = [line for line in new_lines if not re.match(r'^!\[\]', line)]

        if old_lines_no_badges != new_lines_no_badges:
            return False
    return True

def get_last_modified_date(fpath: str, repo: git.Repo =GIT_REPO) -> Union[int, None]:
    """Get the last modification date of a file that is not by an automated user or a simple rename, tag change or title change."""
    file_commits = get_file_commits(fpath, repo)
    if not file_commits:
        logger.error(f"No commits found for file: {fpath}")
        return int(time.time()) #None

    for commit in reversed(file_commits):
        if is_automated_user(commit) or is_rename_only(commit, fpath):
            continue
        if is_title_change_only(commit, fpath):
            continue
        if is_tag_change_only(commit, fpath) or is_badge_change_only(commit, fpath):
            continue
        return commit.committed_date

    return file_commits[-1].committed_date

## Usage
##repo = git.Repo('/path/to/your/repo')
##fpath = 'path/to/your/file'
##last_modified_date = get_last_modified_date(fpath, repo)
##print(f"The last modified date of the file {fpath} is {last_modified_date}")


################################

from pathlib import Path
import random
import re
import subprocess
from collections import defaultdict
from loguru import logger

random.seed(0)

def get_last_modified_date_old(fpath, verbose=True, timestamp=True):
    fmt = "%as"
    if timestamp:
        fmt="%at"
    # ignore commits where author=action@github.com
    #cmd = f"git log --author='^(?!.*action).*$' --perl-regexp --pretty=format:{fmt} --".split( )
    #cmd = f"git log --author='^(?!Github).*$' --perl-regexp --pretty=format:{fmt} --".split( )
    #cmd = f"git log --pretty=format:{fmt} --".split() # straight killin me here...
    cmd = f"git log --pretty=format:{fmt}__%ae --".split() # straight killin me here...
    cmd += [str(fpath)]
    if verbose:
        logger.debug(cmd)
    response = subprocess.run(cmd, capture_output=True)
    #logger.debug(response.returncode)
    #logger.debug(response.stderr.decode())
    commits = response.stdout.decode()
    #logger.debug(outv)
    logger.debug(response)
    #if verbose:
    #    print(outv)
    #outv = outv.split()[0]
    commits = commits.split()
    for c in commits:
        outv, author_email = c.split('__')
        if author_email != 'action@github.com':
            break
    if verbose:
        logger.debug(outv)
    return outv


def badges2kv(text):
    outv = badges2kv_labels(text)
    if not outv:
        outv = badges2kv_regex(text)
    return outv

def badges2kv_labels(text):
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    lines = [line for line in lines if not line.startswith('#')]
    if lines[0].startswith('labels:'):
        labels = lines[0].replace('labels:','').strip().split(',')
        return [('tag', label.strip()) for label in labels]


def badges2kv_regex(text):
    testpat = r'\/([a-zA-Z]+-[a-zA-Z_]+-[a-zA-Z]+)'

    badges = re.findall(testpat, text)
    #return {b.split('-')[0]:b.split('-')[1] for b in badges}
    return [(b.split('-')[0], b.split('-')[1]) for b in badges]


def make_badge(label, prefix='tag', color='lightgrey', root='.'):
    #return f"![](https://img.shields.io/badge/{prefix}-{label}-{color})"
    return f"[![](https://img.shields.io/badge/{prefix}-{label}-{color})]({root}/tags/{label}.md)"


def random_hex_color():
    """generates a string for a random hex color"""
    # https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python
    # https://stackoverflow.com/questions/52843385/python-using-format-f-string-to-output-hex-with-0-padding-and-center
    r = lambda: random.randint(0,255)
    return  f"{r():x}{r():x}{r():x}"

#timestamp = get_last_modified_date(filepath, repo)
#date = datetime.fromtimestamp(timestamp)
#print(date.strftime('%Y-%m-%d %H:%M:%S'))

from datetime import datetime as dt

def timestamp_to_date(timestamp, fmt='%Y-%m-%d'):
    date = dt.fromtimestamp(timestamp)
    return date.strftime(fmt)

import json
with open("tag_lemmatization.json") as f:
    tags_map = json.load(f)

md_files = Path('.').glob('*.md')
TOC = []
unq_tags = defaultdict(list)
for fpath in list(md_files):
    if fpath.name == 'README.md':
        continue
    with open(fpath) as f: 
        header = f.readline()
        if header.startswith('# '):
            text = f.read()
            badge_meta = badges2kv(text)
            d_ = {'fpath':fpath}
            d_['title'] = header[2:].strip()
            d_['last_modified_ts'] = get_last_modified_date(fpath)
            d_['last_modified'] = timestamp_to_date(d_['last_modified_ts'])
            d_['n_char'] = len(text)
            #d_['tags'] = [v for k,v in badge_meta if k =='tag']
            d_['tags'] = [tags_map.get(v,v) for k,v in badge_meta if k =='tag']
            d_['tags'] = [t for t in d_['tags'] if t] # in case we have any tags that lemmatize to empty string
            d_['tags'].sort()
            #unq_tags.update(d_['tags'])
            for tag in d_['tags']:
                unq_tags[tag].append(d_)
            TOC.append(d_)

tag_badges_map = {tag_name:make_badge(label=tag_name, color = random_hex_color()) for tag_name in unq_tags}

def make_badges(unq_tags, sep=' '):
    return sep.join([tag_badges_map[tag] for tag in unq_tags])
    
    
TOC = sorted(TOC, key=lambda x:x['last_modified_ts'])[::-1]

header= "|last_modified|title|est. idea maturity|tags\n|:---|:---|---:|:---|\n"
recs = [f"|{d['last_modified']}|[{d['title']}]({ Path('.')/d['fpath'] })|{d['n_char']}|{make_badges(d['tags'])}|" for d in TOC]
toc_str= header + '\n'.join(recs)


from collections import Counter

cnt = Counter()
for k,v in unq_tags.items():
  cnt[k] = len(v)
cnt.most_common()

readme = None
if Path('README.stub').exists():
    with open('README.stub') as f:
        readme_stub = f.read()
    readme = readme_stub.replace('{TOC}', toc_str)
    readme = readme.replace('{tags}', make_badges(unq_tags))
    #readme += f"\n\n<!--\n{[(k, len(v)) for k,v in unq_tags.items()]}\n--!>"
    readme += f"\n\n<!--\n{cnt.most_common()}\n--!>"
    readme = readme.strip()
if not readme:
    with open('empty.stub') as f:
        readme = f.read()

with open('README.md','w') as f:
    f.write(readme)
    
    
# overriding it this way is ugly but whatever
tag_badges_map = {tag_name:make_badge(label=tag_name, color = random_hex_color(), root='..') for tag_name in unq_tags}
def make_badges(unq_tags, sep=' '):
    return sep.join([tag_badges_map[tag] for tag in unq_tags])
    
    
Path("tags").mkdir(exist_ok=True)
for tag, pages in unq_tags.items():
    pages = sorted(pages, key=lambda x:x['last_modified_ts'])[::-1]
    recs = [f"|{d['last_modified']}|[{d['title']}]({ Path('..')/d['fpath'] })|{d['n_char']}|{make_badges(d['tags'])}|" for d in pages]
    with open(f"tags/{tag}.md", 'w') as f:
        page_str = f"# Pages tagged `{tag}`\n\n"
        page_str += header + '\n'.join(recs)
        f.write(page_str)
