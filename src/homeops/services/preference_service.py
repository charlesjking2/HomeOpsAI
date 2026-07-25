class PreferenceService:

    def __init__(self, household):
        self.household = household

    def restaurant_goal(self):
        return self.household.preferences.restaurant_goal_per_week

    def leftovers_policy(self):
        return self.household.preferences.leftovers_policy

    def shopping_day(self):
        return self.household.preferences.shopping_day

    def meal_planning_day(self):
        return self.household.preferences.meal_planning_day
    
    def available_equipment(self):
        return [
            appliance.name
            for appliance in self.household.appliances
            if appliance.available
        ]