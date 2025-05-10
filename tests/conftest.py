import pytest
import httpx
from httpx import ASGITransport
from calc_cdu.main import app as calc_cdu_app


@pytest.fixture
def async_client_factory():
    """
    Devuelve una factoría de AsyncClient para cualquier FastAPI app.
    """
    def _create_client(app=calc_cdu_app):
        transport = ASGITransport(app=app)
        return httpx.AsyncClient(transport=transport, base_url="http://test")
    return _create_client


@pytest.fixture
async def async_client(async_client_factory):
    """
    Cliente AsyncClient por defecto usando calc_cdu.app
    """
    async with async_client_factory() as client:
        yield client
