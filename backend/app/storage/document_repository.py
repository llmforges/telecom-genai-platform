from app.storage.database import get_connection


def save_document(
        filename,
        json_path,
        status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO documents
        (
            filename,
            json_path,
            status
        )
        VALUES (?, ?, ?)
    """, (
        filename,
        json_path,
        status
    ))

    conn.commit()

    document_id = cursor.lastrowid

    conn.close()

    return document_id


def get_document(document_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM documents
        WHERE id = ?
    """, (document_id,))

    row = cursor.fetchone()

    conn.close()

    return row

def get_all_documents():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM documents
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
