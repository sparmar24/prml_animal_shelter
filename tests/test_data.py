from animal_shelter import data
import pytest

def test_convert_camel_case():
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("Camel-case") != "camel_case"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        data.divide(10, 0)


#example of writing fixtures
@pytest.fixture()
def list_of_numbers():
    return [1, 2, 3, 4, 5]

def test_all_nums(list_of_numbers):
    assert all(type(element) is int for element in list_of_numbers)

def test_sum(list_of_numbers):
    assert sum(list_of_numbers) == 15


#breaking single statement written below.
# assert all(type(element) is int for element in list_of_numbers)

# list_of_numbers = [1,2,3,4,5]
# type_ele = []
# for element in list_of_numbers:
#     is_int = type(element) is int
#     type_ele.append(is_int)
# print(type_ele)
# print(all(type_ele))
