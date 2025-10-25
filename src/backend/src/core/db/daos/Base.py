from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from src.backend.src.core.db.connect_db import async_session


class BaseDAO:
    model = None

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session() as s:
            try:
                res = await s.get_one(cls.model, id=id)
            except SQLAlchemyError:
                return {
                    "msg": "error"
                }
        return res

    @classmethod
    async def obj_or_none(cls, **filters):
        async with async_session() as s:
            query = select(cls.model.__teble__.columns).filter_by(**filters)
            try:
                res = await s.execute(query)
                result = res.mappings().one_or_none()
            except SQLAlchemyError:
                return {
                    "msg": "error"
                }
        return result

    @classmethod
    async def all_by_filter(cls, **filters):
        async with async_session() as s:
            query = select(cls.model.__teble__.columns).filter_by(**filters)
            try:
                res = await s.execute(query)
                result = res.mappings().all()
            except SQLAlchemyError:
                return {
                    "msg": "error"
                }
        return result

    @classmethod
    async def add_data(cls, **data):
        async with async_session() as s:
            model = cls.model(**data)
            try:
                s.add(model)
                await s.commit()
            except SQLAlchemyError:
                return {
                    "msg": "error"
                }
        return model