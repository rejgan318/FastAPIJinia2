"""
Тест на FastAPI + Jinja2 + static files
uvicorn должен присутствовать в виртуальном окружении
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# В директории проекта должна быть директория templates, в которой находятся шаблоны jinja2
templates = Jinja2Templates(directory='templates')
# https://fastapi.tiangolo.com/tutorial/static-files/
app.mount(path="/stat", app=StaticFiles(directory="static"), name="st")

@app.get("/")
async def hello_word():
    return {"message": "Hello World!"}


@app.get("/items/{id}", response_class=HTMLResponse)    # явно указываем, что возвращаться будет не json
async def read_item(request: Request, id: str):
    # передача "request": request в Jinja2- непременное требование, с этим нужно смириться )
    return templates.TemplateResponse("item_template.html", {"request": request, "id": id})


if __name__ == '__main__':
    uvicorn.run(app)
