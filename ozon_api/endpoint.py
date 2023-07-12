from datetime import date, datetime, timedelta

import requests
from fastapi import APIRouter, HTTPException

from ozon_api.db.database import Seller, session
from ozon_api.schema import AuthData

router = APIRouter()


@router.post("/ozon-data")
async def get_and_store_ozon_data(auth_data: AuthData):
    """Получаем данные для авторизации на озоне и добавляем данные в БД."""
    client_id = auth_data.client_id
    api_key = auth_data.api_key

    headers = {
        "Client-Id": client_id,
        "Api-Key": api_key,
    }
    auth_response = requests.get("https://api-seller.ozon.ru", headers=headers)
    auth_response_data = auth_response.json()
    if auth_response_data["code"] == 16:
        raise HTTPException(status_code=400, detail="Ошибка авторизации в API Озона")

    today = date.today()
    period_start = today - timedelta(days=4)
    payload = {
        "from": period_start.strftime("%Y-%m-%d"),
        "to": today.strftime("%Y-%m-%d"),
    }
    etgb_response = requests.get(
        "https://api.ozon.ru/posting/fbs/getEtgb", headers=headers, params=payload
    )
    etgb_data = etgb_response.json()

    for item in etgb_data["result"]:
        posting_number = item["posting_number"]
        etgb = item["etgb"]
        number = etgb["number"]
        dates = datetime.strptime(etgb["date"], "%Y-%m-%d").date()
        url = etgb["url"]

        seller_data = Seller(
            posting_number=posting_number,
            number_etgb=number,
            date_etgb=dates.strftime("%Y-%m-%d"),
            url_etgb=url,
        )
        session.add(seller_data)
    session.commit()
    return {"message": "Данные успешно записаны в ClickHouse"}
