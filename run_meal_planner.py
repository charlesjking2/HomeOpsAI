import os

from dotenv import load_dotenv

from homeops.services.openai_meal_planner import OpenAIMealPlanner


load_dotenv()

mock_mode = os.getenv(
    "MOCK_MODE",
    "true"
).lower() == "true"


if mock_mode:
    print(
        """
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
    )

else:
    api_key = os.environ["OPENAI_API_KEY"]

    planner = OpenAIMealPlanner(api_key)

    try:
        print(planner.recommend())

    except Exception as e:
        print(f"Meal planner failed: {e}")