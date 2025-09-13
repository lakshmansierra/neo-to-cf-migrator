from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator
from services import git_service

router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: str = Field(..., description="HTTPS URL of the Git repository") # tells the field is required
    username: str = Field(..., description="Git username / personal access token owner")
    password: str = Field(..., description="Git password / personal access token")
    description: str | None = Field(None, description="Optional description for this repo") # optional, default=None

    # Pydantic v2 field validator
    @field_validator("repo_url")
    @classmethod
    def validate_repo_url(cls, v: str) -> str:
        if not v.startswith("https://") and not v.startswith("http://"):
            raise ValueError("repo_url must start with http:// or https://")
        return v

@router.post("/fetch")
def fetch_repo(request: RepoRequest):
    try:
        # Try cloning repo using provided credentials
        repo_path = git_service.clone_repo(
            repo_url=request.repo_url,
            username=request.username,
            password=request.password
        )
        return {
            "status": "success",
            "cloned_to": repo_path,
            "description": request.description
        }
    except git_service.GitAuthError:
        # Custom exception if authentication failed
        raise HTTPException(status_code=401, detail="Git authentication failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch repo: {str(e)}")


