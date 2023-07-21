from datetime import date, timedelta

import httpx

from ozon_api.crud.ozon_crud import ozon_crud
from ozon_api.db.database import session
from ozon_api.exceptions.ozon_exceptions import OzonExceptions

OZON_URL = "https://api-seller.ozon.ru"
ETGB_URL = "https://api.ozon.ru/posting/fbs/getEtgb"


class OzonService:
    """Озон Сервис."""

    ozon_exceptions = OzonExceptions()

    async def authorization_on_ozon(self, headers):
        """Авторизация на Озоне."""
        try:
            async with httpx.AsyncClient() as client:
                auth_response = await client.get(OZON_URL, headers=headers)
                auth_response.raise_for_status()
                auth_response_data = auth_response.json()
        except httpx.RequestError as e:
            raise OzonExceptions(self.ozon_exceptions.request_error_message(e))
        except ValueError as e:
            raise OzonExceptions(self.ozon_exceptions.json_processing_error_message(e))
        if auth_response_data["code"] == 16:
            raise OzonExceptions(self.ozon_exceptions.authorization_error_message())
        return auth_response_data

    async def get_payload_for_etgb(self):
        """Получение параметров."""
        today = date.today()
        period_start = today - timedelta(days=4)
        payload = {
            "from": period_start.strftime("%Y-%m-%d"),
            "to": today.strftime("%Y-%m-%d"),
        }
        return payload

    async def operation_on_etgb(self, headers, payload):
        """Получение данных с ETGB и оптправка на запись."""
        try:
            async with httpx.AsyncClient() as client:
                etgb_response = await client.get(
                    ETGB_URL, headers=headers, params=payload
                )
                etgb_response.raise_for_status()
                etgb_data = etgb_response.json()

            add_to_db = await ozon_crud.add_data_from_ozon_api(etgb_data, session)
        except httpx.RequestError as e:
            raise OzonExceptions(self.ozon_exceptions.request_error_message(e))
        except ValueError as e:
            raise OzonExceptions(self.ozon_exceptions.json_processing_error_message(e))
        return add_to_db
