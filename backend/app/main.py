from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.storage.database import initialize_database
from app.api.documents import router as documents_router

initialize_database()

app = FastAPI(
    title="Telecom GenAI Platform",
    version="1.0"
)

app.include_router(upload_router)
app.include_router(documents_router)

@app.get("/")
def root():
    return {
        "message": "Telecom GenAI Deployment Intelligence Platform"
    }
