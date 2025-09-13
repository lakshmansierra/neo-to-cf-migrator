import os
import subprocess
import tempfile

def clone_repo(repo_url: str) -> str:
    """
    Clone a Git repo into a temporary folder.
    Returns the local path.
    """
    base_dir = tempfile.mkdtemp(prefix="neo_cf_repo_")
    try:
        subprocess.run(["git", "clone", repo_url, base_dir], check=True)
        return base_dir
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to clone repo: {str(e)}")
