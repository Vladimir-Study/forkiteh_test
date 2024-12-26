from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import Tron

from . import crud
from app.models import AddressInfoSchema, RequestCreateSchema, PaginatedRequestsSchema, Request
from app.database import setup_database, get_async_session

app = FastAPI()


SessionDependency = Annotated[AsyncSession, Depends(get_async_session)]


@app.post("/setup_database/")
async def recreate_database():
    await setup_database()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Database setup successful"})


@app.post("/address_info/", response_model=AddressInfoSchema)
async def get_address_info(address: str, session: SessionDependency):
    client = Tron()
    account = client.get_account(address)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    info = {
        "address": address,
        "balance": account["balance"],
        "energy": account["energy"],
        "bandwidth": account["freeNetUsed"]
    }

    await crud.create_request(session, RequestCreateSchema(address=address))

    return info


@app.get("/requests/", response_model=PaginatedRequestsSchema)
async def read_requests(session: SessionDependency, skip: int = 0, limit: int = 10):
    requests = await crud.get_requests(session, skip=skip, limit=limit)
    return {"total": len(requests), "items": requests}
