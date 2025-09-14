import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from api import git_routes
from models.response_model import APIResponse  # your unified response model

app = FastAPI(title="Neo to CF Migrator")

# Routers
app.include_router(git_routes.router, prefix="/git", tags=["Git"])

@app.get("/")
def root():
    return {"message": "Neo to CF Migration API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
