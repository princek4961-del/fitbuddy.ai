
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import UserInput
from ai_service import generate_workout,nutrition_tip
import database

app=FastAPI()

templates=Jinja2Templates(directory="templates")


@app.get("/",response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/generate")
def generate(user:UserInput):

    plan=generate_workout(user)
    tip=nutrition_tip(user.goal)

    database.cursor.execute(
        "INSERT INTO users(name,age,weight,goal,intensity,plan) VALUES(?,?,?,?,?,?)",
        (user.name,user.age,user.weight,user.goal,user.intensity,plan)
    )

    database.conn.commit()

    return {"plan":plan,"tip":tip}
