
from fastapi import FastAPI
from routers.tarefa_router import router as tarefa_router

app = FastAPI()
app.include_router(tarefa_router)
