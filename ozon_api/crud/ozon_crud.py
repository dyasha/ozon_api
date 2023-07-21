import datetime

from dateutil.parser import parse as parse_date

from ozon_api.db.database import Seller


class OzonCRUD:
    """CRUD Ozon"""

    async def add_data_from_ozon_api(self, etgb_data, session):
        """Добавление данных в БД."""
        for item in etgb_data["result"]:
            posting_number = item["posting_number"]
            etgb = item["etgb"]
            number = etgb["number"]
            dates = parse_date(etgb["date"]).date()
            url = etgb["url"]
            current_timestamp = datetime.datetime.now()

            seller_data = Seller(
                posting_number=int(posting_number),
                number_etgb=number,
                date_etgb=dates,
                url_etgb=url,
                timestamp=current_timestamp,
            )
            print(seller_data)
            session.add(seller_data)
        session.commit()
        await session.commit()
        return {"message": "Данные успешно записаны в ClickHouse"}


ozon_crud = OzonCRUD()
