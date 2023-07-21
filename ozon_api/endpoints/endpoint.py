from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from ozon_api.db.database import get_async_session
from ozon_api.schemas.ozon_schema import AuthData
from ozon_api.services.ozon_service import OzonService

router = APIRouter()


@cbv(router)
class OzonCBV:
    ozon_service = OzonService()
    session = Depends(get_async_session)

    @router.post("/ozon-data")
    async def get_and_store_ozon_data(self, auth_data: AuthData):
        """Получаем данные для авторизации на озоне и добавляем данные в БД."""
        client_id = auth_data.client_id
        api_key = auth_data.api_key
        headers = {
            "Client-Id": client_id,
            "Api-Key": api_key,
        }
        # await self.ozon_service.authorization_on_ozon(headers)

        payload = await self.ozon_service.get_payload_for_etgb()
        new_data = await self.ozon_service.operation_on_etgb(headers, payload)
        return new_data
