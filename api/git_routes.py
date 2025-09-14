from fastapi import APIRouter, Request
from models.repo_request import RepoRequest
from fastapi.responses import JSONResponse
from services import git_service

router = APIRouter()

@router.post("/fetch")
def fetch_repo(request: RepoRequest, http_request: Request):
    try:
        auth_header = http_request.headers.get("authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={
                    "status": "error",
                    "status_code": 401,
                    "message": "Missing Authorization header",
                    "data": None
                }
            )
        
        pat = auth_header.split(" ")[1]
        
        repo_path = git_service.clone_repo(
            repo_url=request.repo_url,
            pat=pat,
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
                "message": f"{str(e)}",
                "data": None
            }
        )
