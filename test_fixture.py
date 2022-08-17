import pytest

@pytest.fixture
def f():
    print("Greetings from f()")
    return "apa"

def test_g(f):
    print(f"Greetings from g() {f}")
