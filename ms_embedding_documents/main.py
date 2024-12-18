from fastapi import FastAPI
from api.routes import router

app = FastAPI()

# Prefixo para as rotas da API
app.include_router(router, prefix="/ms_embedding")

# start API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)