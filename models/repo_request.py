from pydantic import BaseModel, Field, field_validator

class RepoRequest(BaseModel):
    repo_url: str = Field(..., description="HTTPS URL of the Git repository")
    username: str = Field(..., description="Git username / personal access token owner")
    password: str = Field(..., description="Git password / personal access token")
    description: str | None = Field(None, description="Optional description for this repo")

    @field_validator("repo_url")
    @classmethod
    def validate_repo_url(cls, v: str) -> str:
        if not v.startswith("https://") and not v.startswith("http://"):
            raise ValueError("repo_url must start with http:// or https://")
        return v
