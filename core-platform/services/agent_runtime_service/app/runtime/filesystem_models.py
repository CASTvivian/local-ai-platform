from pydantic import BaseModel
from typing import Optional


class FileWriteRequest(BaseModel):
    sandbox_id: Optional[str] = None
    path: str
    content: str = ""


class FileReadRequest(BaseModel):
    sandbox_id: str
    path: str


class FileListRequest(BaseModel):
    sandbox_id: str
    path: str = "."


class FileDeleteRequest(BaseModel):
    sandbox_id: str
    path: str
