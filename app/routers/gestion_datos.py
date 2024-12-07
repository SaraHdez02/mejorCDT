from fastapi import APIRouter, HTTPException
from app.services.calculadora_service import calculate_expired_rate, calculate_roi, find_rates

router = APIRouter()


@router.get("/rates")
def get_rates(investment_amount: float, investment_term: int):
    """
    Endpoint to find effective annual rates based on investment amount and term.
    """
    try:
        rates = find_rates(investment_amount, investment_term, "data/bank_rates.csv")
        if not rates:
            raise HTTPException(status_code=404, detail="No rates found for the entered amount and term.")
        unique_rates = list({rate['bank']: rate for rate in rates}.values())
        return unique_rates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/expired-rate")
def calculate_expired_rate_endpoint(effective_annual_rate: float, term: int):
    """
    Endpoint to calculate the expired rate from the effective annual rate and term.
    """
    try:
        expired_rate = calculate_expired_rate(effective_annual_rate, term, 'data/bank_rates.csv')
        return {"expired_rate": expired_rate}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/roi")
def calculate_roi_endpoint(amount: float, expired_rate: float):
    """
    Endpoint to calculate ROI based on the amount and expired rate.
    """
    try:
        roi = calculate_roi(amount, expired_rate, 'data/bank_rates.csv')
        return {"roi": roi}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
