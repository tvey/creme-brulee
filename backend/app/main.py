from fastapi import FastAPI, APIRouter

from app.words.api.v1 import router as words_router
from app.words.schemas import Word

root_router = APIRouter()
app = FastAPI()


@root_router.get('/')
def index():
    return {'message': 'Hey'}


app.include_router(words_router)
app.include_router(root_router)
