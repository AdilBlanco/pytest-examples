import sys
import pytest
from datetime import date

from src.container import Container, ContainerPlatform


@pytest.fixture(scope="session")
def con():
    container = Container()
    yield container


@pytest.fixture(scope="session")
def conplatfom():
    container = ContainerPlatform()
    yield container


def test_container():
    assert isinstance(Container, type) == True


@pytest.mark.skip(reason="The Container class requires implementation.")
def test_has_code_attribute():
    msg = 'The Container class does not have a name attribute.'
    assert hasattr(Container, 'name') == True, msg


@pytest.mark.skipif(date.today().day % 2 != 0, reason="Skipping Odd days")
def test_skipping_odd_days(con):
    msg = 'Invalid code attribute.'
    assert con.code.endswith('0') == True, msg


@pytest.mark.skipif(date.today().day % 2 == 0, reason="Skipping even days")
def test_skipping_even_days(con):
    msg = 'Invalid code attribute.'
    assert con.code.endswith('1') == True, msg


@pytest.mark.skipif(sys.platform.startswith('win'), reason='Requires Windows.')
def test_requires_windows(conplatfom):
    assert conplatfom.code == 'XC-win'


@pytest.mark.skipif(sys.platform.startswith('linux'), reason='Requires Linux.')
def test_requires_linux(conplatfom):
    assert conplatfom.code == 'XC-linux'


# pipenv run pytest -rs tests/test-container.py
