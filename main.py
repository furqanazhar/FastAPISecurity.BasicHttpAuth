from fastapi import FastAPI
from routers import security
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_ROUTE = '/FastAPISecurity/v1'

app.include_router(
    router=security.router,
    prefix=f'{API_ROUTE}',
    tags=['security']
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
