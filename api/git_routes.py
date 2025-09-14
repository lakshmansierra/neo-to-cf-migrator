from fastapi import APIRouter, HTTPException
from services import git_service
from models.repo_request import RepoRequest
from models.response_model import APIResponse
from utils.response_helper import make_response

router = APIRouter()

@router.post("/fetch", response_model=APIResponse)
def fetch_repo(request: RepoRequest):
    try:
        repo_path = git_service.clone_repo(
            repo_url=request.repo_url,
            username=request.username,
            password=request.password
        )
        return make_response(
            status="success",
            status_code=200,
            message="Repository cloned successfully",
            data={"cloned_to": repo_path, "description": request.description}
        )
    except git_service.GitAuthError:
        raise HTTPException(
            status_code=401,
            detail=make_response("error", 401, "Git authentication failed").dict()
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=make_response("error", 500, f"Failed to fetch repo: {str(e)}").dict()
        )
