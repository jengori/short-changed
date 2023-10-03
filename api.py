from fastapi import FastAPI
from short_changed import router

shortchanged = FastAPI()


@shortchanged.get("/")
def hello():
    return {"Hello! You have been": "short changed"}


shortchanged.include_router(router.router, prefix="/short-changed")



