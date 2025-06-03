import os
from github import Github

def main():
    # Get GitHub token from env
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not found in environment variables")
        return

    # Authenticate with GitHub
    g = Github(token)
    repo_name = os.getenv("GITHUB_REPOSITORY", "your-username/your-repo")  # Override or hardcode

    repo = g.get_repo(repo_name)

    commits = repo.get_commits()[:5]
    print("Last 5 commits:")
    for commit in commits:
        print(f"- {commit.commit.message}")

if __name__ == "__main__":
    main()
