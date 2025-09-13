from fastapi import APIRouter
from pydantic import BaseModel
from services import migration_service

router = APIRouter()

class MigrationRequest(BaseModel):
    repo_path: str  # local path of cloned repo

@router.post("/start")
def start_migration(request: MigrationRequest):
    result = migration_service.run_migration(request.repo_path)
    return {"status": "migration complete", "output_path": result}
