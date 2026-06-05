from fastapi import APIRouter, HTTPException

from app.storage.document_repository import (
    get_document,
    get_all_documents
)

router = APIRouter()


@router.get("/documents")
def list_documents():

    rows = get_all_documents()

    results = []

    for row in rows:

        results.append({
            "id": row[0],
            "filename": row[1],
            "json_path": row[2],
            "status": row[3],
            "created_at": row[4]
        })

    return results


@router.get("/documents/{document_id}")
def get_document_by_id(document_id: int):

    row = get_document(document_id)

    if not row:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return {
        "id": row[0],
        "filename": row[1],
        "json_path": row[2],
        "status": row[3],
        "created_at": row[4]
    }

