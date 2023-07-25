from github import Github
from github.Issue import Issue
import os

def convert_issue_to_note(issue_number: int, g: Github, username: str, repository: str):
    """Fetch issue, create a new markdown note from its content, and close the issue."""
    repo = g.get_repo(f"{username}/{repository}")
    issue = repo.get_issue(number=issue_number)
    file_content = issue.body

    # add "from_issue" badge
    file_content = "\n\n".join([
        "# " + issue.title,
        "labels: from_issue",
        file_content,
        "[Link to original issue](" + issue.html_url + ")",
    ])

    # create (and commit) a new note
    repo.create_file(issue.title.replace(" ", "_") + ".md", f"Create note from issue #{issue_number}", file_content)

    # add a comment with a link to the new note
    issue.create_comment(f"Issue migrated to note: {issue.title.replace(' ', '_')}.md")

    # close the issue
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
create_files_from_issues(repo_name, 'actually-an-article', token)
