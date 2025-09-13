import uvicorn
from fastapi import FastAPI
from api import git_routes, migrate_routes

app = FastAPI(title="Neo to CF Migrator")

# include routers
app.include_router(git_routes.router, prefix="/git", tags=["Git"])
app.include_router(migrate_routes.router, prefix="/migrate", tags=["Migration"])

@app.get("/")
def root():
    return {"message": "Neo to CF Migration API is running 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
