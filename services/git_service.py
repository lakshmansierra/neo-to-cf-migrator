import os
import subprocess
import tempfile

class GitAuthError(Exception):
    """Raised when Git authentication fails"""
    pass

def clone_repo(repo_url: str, username: str, password: str) -> str:
    """
    Clone a Git repo into a temporary folder using username/password.
    Raises GitAuthError if authentication fails.
    """
    if not username or not password:
        raise GitAuthError("Username and password are required")

    # Inject credentials into HTTPS URL
    if repo_url.startswith("https://"):
        repo_url_with_creds = repo_url.replace("https://", f"https://{username}:{password}@")
    else:
        repo_url_with_creds = repo_url  # fallback (rare)

    base_dir = tempfile.mkdtemp(prefix="neo_cf_repo_")
    try:
        result = subprocess.run(
            ["git", "ls-remote", repo_url_with_creds],
            capture_output=True, text=True, check=True
        )
        # Authentication succeeded, now clone
        subprocess.run(["git", "clone", repo_url_with_creds, base_dir], check=True)
        return base_dir
    except subprocess.CalledProcessError as e:
        if "Authentication failed" in e.stderr:
            raise GitAuthError("Authentication failed: Invalid username or token")
        elif "Repository not found" in e.stderr:
            raise GitAuthError("Repository not found or access denied")
        else:
            raise GitAuthError(f"Git error: {e.stderr.strip()}")

