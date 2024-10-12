from pandas.testing import assert_series_equal
import pandas as pd
from animal_shelter import features
import pytest

def test_check_is_dog():
    is_dog = pd.Series(["Dog", "Cat",])
    actual = features.check_is_dog(is_dog)
    expected = pd.Series([True, False])
    assert_series_equal(actual, expected)

def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    actual = features.check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(actual, expected)

def test_get_hair_type():
    hair_types = pd.Series(["shorthair", "medium hair", "longhair", "short", "curly"])
    actual = features.get_hair_type(hair_types)
    expected = pd.Series(["shorthair", "medium hair", "longhair", "unknown", "unknown"])
    assert_series_equal(actual, expected)

# def test_compute_days_upon_outcome():

@pytest.fixture()
def fixture_get_sex_neutered():
    sex_upon_outcome = pd.Series(["spayed Female", "spayed Male", "neutered Female", "neutered Male", "intact Female", "intact Male"])
    return sex_upon_outcome

def test_get_sex(fixture_get_sex_neutered):
    actual = features.get_sex(fixture_get_sex_neutered)
    expected = pd.Series(["female", "male", "female", "male", "female", "male"])
    assert_series_equal(actual, expected)

def test_get_neutered(fixture_get_sex_neutered):
    actual = features.get_neutered(fixture_get_sex_neutered)
    expected = pd.Series(["fixed", "fixed", "fixed", "fixed","intact", "intact"])
    assert_series_equal(actual, expected)
