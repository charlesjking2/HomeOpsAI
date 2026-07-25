from homeops.services.leftover_engine import LeftoverEngine


class Meal:
    def __init__(
        self,
        name,
        makes_leftovers,
    ):
        self.name = name
        self.makes_leftovers = makes_leftovers


def test_leftovers_preferred_for_busy_days():

    engine = LeftoverEngine()

    brisket = Meal(
        "Brisket",
        True,
    )

    assert engine.should_prefer(
        brisket,
        busy_day=True,
    )