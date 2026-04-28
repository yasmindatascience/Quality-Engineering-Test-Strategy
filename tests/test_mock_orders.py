from unittest.mock import patch
from services.orders_service.queries import get_order_by_id

@patch("services.orders_service.queries.psycopg2.connect")
def test_get_order_mock(mock_connect):

    mock_conn = mock_connect.return_value
    mock_cursor = mock_conn.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 101, 2)

    result = get_order_by_id(1)

    assert result == (1, 101, 2)
