from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def hello():
    return {"message": "Hello Harry"}


class NamePayload(BaseModel):
    name: str = "Wimbledon"


## csv file path = 
# path = r'C:\Users\Harry Ridgway\Desktop\Visual Studio Projects\Built Enviroment\Data\priorities_by_oa_2024_03_05_ai.csv'

# @app.post("/get_winner_count_by_const_name")
# async def get_winner_count_by_const_name(payload: NamePayload):
#     data = pd.read_csv(path, encoding='latin1')
#     data = data[data['PCON25NM'] == payload.name]
#     v_counts = data['winner'].value_counts().to_dict()
#     return v_counts

path = r"C:\Users\Harry Ridgway\Desktop\Visual Studio Projects\be_api\RAG_by_OA_AI_27_02_2024.csv"
@app.post("/get_rag_at_ward_by_Constituency")
async def get_rag_at_ward_by_Constituency(payload: NamePayload):
    data = pd.read_csv(path, encoding='latin1')
    data = data[data['PCON25NM'] == payload.name]
    average_pop = data['pop'].mean()
    data['weighted_rag'] = data['rag'] * ( data['pop'] / average_pop )
    wards = data.groupby('WD23NM')['weighted_rag'].mean().to_dict()
    for key in wards:
        wards[key] = round(wards[key], 2)
        
    return wards





