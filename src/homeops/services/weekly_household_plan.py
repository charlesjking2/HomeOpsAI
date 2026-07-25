class WeeklyHouseholdPlan:

    def __init__(
        self,
        meal_engine,
        grocery_engine,
        store_planner,
    ):
        self.meal_engine = meal_engine
        self.grocery_engine = grocery_engine
        self.store_planner = store_planner


    def generate(self):

        meals = self.meal_engine.generate()

        groceries = self.grocery_engine.build_list(
            meals
        )

        stores = {}

        for item in groceries:
            store = self.store_planner.assign_store(
                item
            )

            stores.setdefault(
                store,
                []
            ).append(item)

        return {
            "meals": meals,
            "shopping": stores,
        }