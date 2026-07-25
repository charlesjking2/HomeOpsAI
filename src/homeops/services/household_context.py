from homeops.models.family import Family
from homeops.models.household import Household
from homeops.models.meal import Meal

from homeops.services.knowledge_loader import (
    load_family,
    load_household,
    load_meals,
)


class HouseholdContext:
    """
    Centralized household knowledge object.

    This becomes the context provided
    to future AI agents.
    """

    def __init__(
        self,
        family: Family,
        household: Household,
        meals: list[Meal],
    ):
        self.family = family
        self.household = household
        self.meals = meals

    @classmethod
    def load(cls):

        # Load family YAML
        family_yaml = load_family()

        family = Family(
            members=family_yaml["family"]["members"]
        )

        # Load household YAML
        household_yaml = load_household()

        household = Household(
            **household_yaml
        )

        # Load meals YAML
        meals_yaml = load_meals()

        meals = []

        for category, data in meals_yaml["categories"].items():
            for meal_name in data["meals"]:
                meals.append(
                    Meal(
                        name=meal_name,
                        category=category,
                        proteins=[],
                        equipment=[],
                    )
                )

        return cls(
            family=family,
            household=household,
            meals=meals,
        )

    def summary(self):
        return {
            "family_name": self.household.family_name,
            "family_size": self.family.size,
            "restaurant_goal": (
                self.household.preferences.restaurant_goal_per_week
            ),
            "meal_count": len(self.meals),
            "stores": [
                store.name
                for store in self.household.stores
            ],
        }