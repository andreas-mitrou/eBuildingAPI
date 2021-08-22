from fastapi import FastAPI
import uvicorn
from routers import anouncements, users

app = FastAPI()
_host = "0.0.0.0"
_port = 8000


app.include_router(anouncements.router)
app.include_router(users.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}



if __name__ == "__main__":
    uvicorn.run(app, host=_host, port=_port)