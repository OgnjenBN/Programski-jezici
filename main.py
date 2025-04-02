from fastapi import FastAPI 
from database import engine
import models, routers
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)