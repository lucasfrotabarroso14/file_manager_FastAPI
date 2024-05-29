import uvicorn
from fastapi import FastAPI

from app.microservices.organization_microservice.organization_view import router
import logging

from app.microservices.user_microservice.user_view import routerteste

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()



app.include_router(router)
app.include_router(routerteste)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
