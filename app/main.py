from fastapi import FastAPI
# from .app_logging import getLogger

# logger = getLogger(__name__)

from app.app_logging import logger

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("abc")
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    logger.info(f"{item_id}, {q}")
    return {"item_id": item_id, "q": q}
