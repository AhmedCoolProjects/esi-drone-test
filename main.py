from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from classes.tps_algorithm import Main

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    lat_list = [float]
    lng_list = [float]


@app.get("/")
def welcome():
    return {"message": "Welcome to Jina Template API"}
# endpoint


@app.post("/tps")
async def create_item(item: Item):
    tps_item = Main(item.lat_list, item.lng_list)
    result_item = tps_item.n_permutation()
    return result_item


@app.get("/tps")
def tps():
    return {"message": "TPS get"}
