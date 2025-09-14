from pydantic import BaseModel, Field, field_validator

class RepoRequest(BaseModel):
    repo_url: str = Field(..., description="HTTPS URL of the Git repository")
    # pat: str = Field(..., description="Git personal access token")

    @field_validator("repo_url")
    @classmethod
    def validate_repo_url(cls, v: str) -> str:
        if not v.startswith("https://") and not v.startswith("http://"):
            raise ValueError("repo_url must start with http:// or https://")
        return v
