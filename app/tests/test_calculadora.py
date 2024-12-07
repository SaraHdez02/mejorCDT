import os
from app.services.calculadora_service import calculate_roi, calculate_expired_rate, find_rates

current_dir = os.path.dirname(__file__)
bank_file = os.path.join(current_dir, '..', '..', 'data', 'bank_rates.csv')


def test_calculate_roi():
    results = calculate_roi(1000000, 180, bank_file)
    assert len(results) > 0
    for result in results:
        assert result["total_profitability"] > 0


def test_calculate_expired_rate():
    results = calculate_expired_rate(0.05, 180, bank_file)
    assert len(results) > 0
    for result in results:
        assert result["expired_rate"] > 0


def test_find_rates():
    results = find_rates(1000000, 180, bank_file)
    assert len(results) > 0
    for result in results:
        assert result["effective_annual_rate"] > 0
