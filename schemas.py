from pydantic import BaseModel

class UploadDocumentCreate(BaseModel):
    path: str
    filename: str
    filesize: int
