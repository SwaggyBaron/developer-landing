from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.schemas import ContactRequest
from app.logger import logger
from app.services import analyze_sentiment
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware


app = FastAPI(
    title="Developer Landing API",
    version="1.0.0"
)

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/api/contact")
@limiter.limit("5/minute")
async def contact(request: Request, data: ContactRequest):

    sentiment = analyze_sentiment(data.comment)

    logger.info(
        f"New contact request: "
        f"name={data.name}, "
        f"email={data.email}"
    )

    return {
        "message": "Contact request received",
        "sentiment": sentiment,
        "data": data
    }

@app.get("/api/health")
def health():
    return {"status": "ok"}