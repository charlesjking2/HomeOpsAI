from openai import OpenAI

from homeops.services.household_context import HouseholdContext


class OpenAIMealPlanner:

    def __init__(
        self,
        api_key: str | None = None,
        use_ai: bool = True,
    ):
        self.use_ai = use_ai

        if use_ai:
            self.client = OpenAI(api_key=api_key)
        else:
            self.client = None


    def recommend(self):

        context = HouseholdContext.load()

        if not self.use_ai:
            return self.mock_recommendation(context)

        prompt = f"""
You are helping plan meals.

Family:
{context.summary()}

Recommend five dinners for this week.
"""

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt,
        )

        return response.output_text


    def mock_recommendation(self, context):

        return """
Mock Meal Plan

Monday:
- Chicken Shawarma
  Reason: Easy preparation

Tuesday:
- Tacos
  Reason: Busy family night

Wednesday:
- Honey Salmon
  Reason: Healthy option

Thursday:
- Chicken Parmesan Wraps
  Reason: Quick dinner

Friday:
- Cheeseburgers
  Reason: Family favorite
"""