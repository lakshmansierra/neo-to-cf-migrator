from fastapi import APIRouter
from models.repo_request import RepoRequest
from fastapi.responses import JSONResponse
from services import git_service

router = APIRouter()

@router.post("/fetch")
def fetch_repo(request: RepoRequest):
    try:
        repo_path = git_service.clone_repo(
            repo_url=request.repo_url,
            pat=request.pat,
        )
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "status_code": 200,
                "message": "Repository cloned successfully",
                "data": {"cloned_to": repo_path}
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "status_code": 500,
                "message": f"Failed to fetch repo: {str(e)}",
                "data": None
            }
        )
