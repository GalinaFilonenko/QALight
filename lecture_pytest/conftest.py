import pytest


@pytest.fixture(autouse=False)
def global_lecture_pytest_fixture():
    print('global lecture_pytest fixture setup')
    yield
    print('global lecture_pytest fixture teardown')