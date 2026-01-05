from fastapi import FastAPI, APIRouter, Request
from starlette.responses import JSONResponse

from app.database import create_tables
from contextlib import asynccontextmanager
from app.api import users
from app.exceptions import AppException


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

example = FastAPI(lifespan=lifespan)

@example.get("/health_check")
def health_check():
    return {"status": "ok"}

@example.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(status_code=exc.code, content={"error": exc.message})

api_router = APIRouter(prefix="/api")
api_router.include_router(users.router, prefix="/users", tags=["Users"])

example.include_router(api_router)

