from pandas.testing import assert_series_equal
import pandas as pd
from animal_shelter import features

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

def test_get_sex():
    sex = pd.Series(["Male", "Female", "unknown"])
    actual = features.get_sex(sex)
    expected = pd.Series(["male", "female", "unknown"])
    assert_series_equal(actual, expected)

def test_get_neutered():
    neutered = pd.Series(["neutered", "spayed", "intact"])
    actual = features.get_neutered(neutered)
    expected = pd.Series(["fixed", "fixed", "intact"])
    assert_series_equal(actual, expected)

def test_get_hair_type():
    hair_types = pd.Series(["shorthair", "medium hair", "longhair", "short", "curly"])
    actual = features.get_hair_type(hair_types)
    expected = pd.Series(["shorthair", "medium hair", "longhair", "unknown", "unknown"])
    assert_series_equal(actual, expected)

# def test_compute_days_upon_outcome():
