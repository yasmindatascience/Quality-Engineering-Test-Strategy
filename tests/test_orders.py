import pytest
from services.orders_service.queries import get_order_by_id

def test_get_order_by_id():
    result = get_order_by_id(1)

    assert result is None or isinstance(result, tuple)
