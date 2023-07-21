from pydantic import BaseModel, Field


class AuthData(BaseModel):
    client_id: str = Field(example="client_id")
    api_key: str = Field(example="api_key")
