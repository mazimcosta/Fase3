
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import APIRouter
from routers.livro_router import router as livro_router
from routers.usuario_router import router as usuario_router
from routers.emprestimo_router import router as emprestimo_router


app= FastAPI()
app.include_router(usuario_router)
app.include_router(livro_router)
app.include_router(emprestimo_router)



