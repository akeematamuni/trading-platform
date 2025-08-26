from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from shared.util import get_service_name

load_dotenv()

app = FastAPI(title="Trading Platform", version="0.0.1")


@app.get("/home")
async def get_home():
    return JSONResponse({"message": get_service_name()}, status_code=200)


if __name__ == "__main__":
    import os

    import uvicorn

    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 8000))

    uvicorn.run(app, host=host, port=port)
