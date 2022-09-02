import pytest
from pytest_voluptuous import S
from dotenv import load_dotenv
from utils.session import req_session
from schemas.regres import single_resource, create


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def test_positive_single_resource():
    response = req_session().get('/api/unknown/2')
    assert S(single_resource) == response.json()


def test_color_is_string():
    response = req_session().get('/api/unknown/2')
    assert isinstance(response.json()['data']['color'], str)


def test_create():
    response = req_session().post('/api/users', data={"name": "Meowth",
    "job": "pokemon"})
    assert response.status_code == 201
    assert S(create) == response.json()
    assert str(response.json()['name']) == 'Meowth'


def test_update():
    response = req_session().put('/api/users/2', data={"name": "Meowth",
    "job": "pokemon"})
    assert response.status_code == 200
    assert str(response.json()['name']) == 'Meowth'
    assert isinstance(response.json()['job'], str)


def test_delete():
    response = req_session().delete('/api/users/2')
    assert response.status_code == 204
