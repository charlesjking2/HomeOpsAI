from homeops.services.memory_service import MemoryService


def test_memory_records_meals():

    memory = MemoryService(
        ":memory:"
    )

    memory.add_meal(
        "Tacos",
        "2026-07-24"
    )

    assert memory.recently_used(
        "Tacos"
    )