from animal_shelter.data import load_data
from animal_shelter.features import add_features

animal_outcomes = load_data("data/test.csv")
breakpoint()
with_features = add_features(animal_outcomes)
breakpoint()
print(with_features.head())
