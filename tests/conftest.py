import pytest
from src.api_utils import HeadHunterAPI


@pytest.fixture
def hh_api_test():
    return HeadHunterAPI()