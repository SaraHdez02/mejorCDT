from pydantic import BaseModel

class RateRequest(BaseModel):
    amount: float
    term_in_days: int

class RateResponse(BaseModel):
    bank: str
    rate: float
    profitability: float
