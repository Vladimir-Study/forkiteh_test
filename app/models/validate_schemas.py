from typing import List, Optional
from pydantic import BaseModel


class AddressInfoSchema(BaseModel):
    address: str
    balance: int
    energy: int
    bandwidth: int


class RequestCreateSchema(BaseModel):
    address: str


class RequestResponseSchema(BaseModel):
    id: int
    address: str
    timestamp: str

    class Config:
        from_attributes = True


class PaginatedRequestsSchema(BaseModel):
    total: int
    items: List[RequestResponseSchema]