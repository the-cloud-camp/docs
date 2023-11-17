from python_pytest.basics import add

def test_add_can_add_numbers():
    num = 3
    num2 = 45
    result = add(num, num2)
    assert result == 48