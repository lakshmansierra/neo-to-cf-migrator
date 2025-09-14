import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from api import git_routes, migration_routes
from models.response_model import APIResponse  # your unified response model

app = FastAPI(title="Neo to CF Migrator")

# ✅ Success: You return APIResponse directly in your routes
# Example: return APIResponse(success=True, message="Repo cloned", data={...})

# ✅ Handle HTTPException (business errors raised with `raise HTTPException`)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException): # POST-ROUTE
    return JSONResponse(
        status_code=exc.status_code,
        content=APIResponse(
            success=False,
            message=exc.detail,
            data=None,
            error={"type": "HTTPException"}
        ).model_dump()
    )

# ✅ Handle Pydantic validation errors (422)
@app.exception_handler(RequestValidationError) # PRE-ROUTE
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=APIResponse(
            success=False,
            message="Validation error",
            data=None,
            error=exc.errors()  # keep original detail so devs don’t lose info
        ).model_dump()
    )

# ✅ Handle any other unhandled errors (500)
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception): # POST-ROUTE
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=APIResponse(
            success=False,
            message="Internal server error",
            data=None,
            error={"detail": str(exc)}
        ).model_dump()
    )

# Routers
app.include_router(git_routes.router, prefix="/git", tags=["Git"])

@app.get("/")
def root():
    return {"message": "Neo to CF Migration API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
