# test using your own fixture
def test_one():
    print('student_pytest test_one executed')


# test using both fixtures
def test_two(global_lecture_pytest_fixture):
    print('student_pytest test_two executed')


# test using all fixtures
def test_three(global_lecture_pytest_fixture, student1_pytest_fixture):
    assert type(student1_pytest_fixture) is int

