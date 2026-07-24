import yaml


def load_yaml(path):

    with open(path, "r") as file:
        return yaml.safe_load(file)


def load_family():

    return load_yaml(
        "config/family.yaml"
    )


def load_household():

    return load_yaml(
        "config/household.yaml"
    )


def load_meals():

    return load_yaml(
        "config/meals.yaml"
    )
