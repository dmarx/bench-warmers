from github import Github
from github.Issue import Issue
import os

def convert_issue_to_note(issue: Issue, repo_name: str, token: str):
    """Converts a single issue into a markdown note in the repository."""
    g = Github(token)
    repo = g.get_repo(repo_name)

    file_content = f"# {issue.title}\n\n{issue.body}"
    file_path = f"{issue.title.replace(' ', '_')}.md"
    repo.create_file(path=file_path, message=f"Convert issue #{issue.number} to note",
                     content=file_content)

    # Comment on and close the issue
    issue.create_comment(f"Issue has been converted to a note. See the note [here](https://github.com/{repo_name}/blob/main/{file_path}).")
    issue.edit(state='closed')

def create_files_from_issues(repo_name: str, label_name: str, token: str):
    """Fetches all the open issues with a particular label from a repository and converts them into markdown notes."""
    g = Github(token)
    repo = g.get_repo(repo_name)

    # Get all open issues
    open_issues = repo.get_issues(state='open')

    for issue in open_issues:
        # Check if the issue has the correct label
        if label_name in [label.name for label in issue.labels]:
            convert_issue_to_note(issue, repo_name, token)

# The token should be stored as an environment variable to avoid exposing it in the script
token = os.getenv('GITHUB_TOKEN')
repo_name = os.getenv('GITHUB_REPOSITORY')
create_files_from_issues(repo_name, 'actally-an-article', token)
