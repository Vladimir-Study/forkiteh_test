from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import  Request, RequestCreateSchema


async def create_request(session: AsyncSession, request: RequestCreateSchema):
    query = select(Request).filter_by(address=request.address)
    exist = await session.execute(query)
    if not exist:
        db_request = Request(address=request.address)
        session.add(db_request)
        await session.commit()
        return db_request


async def get_requests(session: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(Request).offset(skip).limit(limit)
    result = await session.execute(query)
    for i in result.all():
        print(i)
    return result.all()