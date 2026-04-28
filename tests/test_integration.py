from services.orders_service.app import run

def test_integration_flow():
    try:
        run()
        assert True
    except Exception:
        assert False
