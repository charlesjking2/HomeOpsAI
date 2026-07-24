from homeops.services.knowledge_loader import load_family


def test_family_size():

    family = load_family()

    assert len(
        family["family"]["members"]
    ) == 6
