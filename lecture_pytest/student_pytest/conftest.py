import pytest


@pytest.fixture(autouse=True)
def student_pytest_fixture():
    print('student_pytest_fixture setup')
    yield
    print('student_pytest_fixture teardown')


@pytest.fixture(autouse=False)
def student1_pytest_fixture():
    yield 5
