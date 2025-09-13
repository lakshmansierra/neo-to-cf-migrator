from fastapi import APIRouter
from pydantic import BaseModel
from services import git_service

router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: str

@router.post("/fetch")
def fetch_repo(request: RepoRequest):
    repo_path = git_service.clone_repo(request.repo_url)
    return {"status": "success", "cloned_to": repo_path}
