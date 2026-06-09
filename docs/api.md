# API Documentation

## POST /documents/upload

Upload telecom PDF.

Request:
multipart/form-data

Response:

{
  "document_id": 1,
  "filename": "ims.pdf",
  "status": "processed"
}

---

## GET /documents

Returns all processed documents.

---

## GET /documents/{id}

Returns metadata for a specific document.
