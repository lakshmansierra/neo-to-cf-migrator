import subprocess
import tempfile

def clone_repo(repo_url: str, pat: str) -> str:
    repo_url_with_creds = repo_url.replace("https://", f"https://x-access-token:{pat}@")
    base_dir = tempfile.mkdtemp(prefix="neo_cf_repo_")
    
    try:
        subprocess.run(
            ["git", "ls-remote", repo_url_with_creds],
            capture_output=True, text=True, check=True
        )
        subprocess.run(["git", "clone", repo_url_with_creds, base_dir], check=True)
        return base_dir
    
    except subprocess.CalledProcessError as e:
        raise Exception(f"Git error: {e.stderr.strip()}")