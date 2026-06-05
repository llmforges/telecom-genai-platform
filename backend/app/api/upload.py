from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.document_processor import process_document
from app.storage.document_repository import save_document

router = APIRouter()

UPLOAD_DIR = "../uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    json_file = process_document(file_path)
    document_id = save_document(
        file.filename,
        json_file,
        "processed"
    )
    return {
        "document_id": document_id,
	"filename": file.filename,
	"status": "processed",
	"json_output": json_file
       }
