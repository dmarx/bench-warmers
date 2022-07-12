from pathlib import Path
import subprocess

def get_last_modified_date(fpath, verbose=True):
    cmd = "git log -n 1 --pretty=format:%as --".split( )
    cmd += [str(fpath)]
    if verbose:
        print(cmd)
    response = subprocess.run(cmd, capture_output=True)
    outv = response.stdout.decode()
    if verbose:
        print(outv)
    return outv

md_files = Path('.').glob('*.md')
TOC = []
for fpath in list(md_files):
    if fpath.name == 'README.md':
        continue
    with open(fpath) as f: 
        header = f.readline()
        if header.startswith('# '):
            d_ = {'fpath':fpath}
            d_['title'] = header[2:].strip()
            d_['last_modified'] = get_last_modified_date(fpath)
            TOC.append(d_)

TOC = sorted(TOC, key=lambda x:x['last_modified'])[::-1]

url_root = '' # "https://github.com/dmarx/bench-warmers/blob/main/"

header= "|last_modified|title|\n|:---|:---|\n"
recs = [f"|{d['last_modified']}|[{d['title']}]({url_root}{d['fpath']})|" for d in TOC]
toc_str= header + '\n'.join(recs)

#readme_stub = "# title \n\n text goes here\n\n{TOC}\n\n# another section"
with open('README.stub') as f:
    readme_stub = f.read()
readme = readme_stub.replace('{TOC}',toc_str)

with open('README.md','w') as f:
    f.write(readme)
