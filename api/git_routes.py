from fastapi import APIRouter, HTTPException
from models.repo_request import RepoRequest
from models.response_model import APIResponse
from services import git_service
from utils.response_helper import make_response

router = APIRouter()

@router.post("/fetch", response_model=APIResponse)
def fetch_repo(request: RepoRequest):
    try:
        repo_path = git_service.clone_repo(
            repo_url=request.repo_url,
            pat=request.pat,
        )
        return make_response(
            status="success",
            status_code=200,
            message="Repository cloned successfully",
            data={"cloned_to": repo_path}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=make_response(
                status="error",
                status_code=500,
                message=f"Failed to fetch repo: {str(e)}"
            ).dict()
        )
