import pytest
import uuid
from api_client import YougileProjectAPI


@pytest.fixture(scope="session")
def api_client():
    base_url = "https://ru.yougile.com/api-v2"
    token = "NJ-yvrBQ_3K6zIaBxIxoVMqh5EzeFeAhSIAUT0x1bakr5cZMIi2S96qrBaY5D93X"
    return YougileProjectAPI(base_url, token)


@pytest.fixture
def unique_title():
    return f"ГосУслуги_{uuid.uuid4().hex[:8]}"
