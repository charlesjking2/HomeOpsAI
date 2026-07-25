class StorePlanner:
    """
    Assigns groceries to preferred stores.
    """

    def __init__(
        self,
        stores,
    ):
        self.stores = stores


    def assign_store(
        self,
        item,
    ):

        item = item.lower()

        if "bulk" in item:
            return "Costco"

        if "clean" in item:
            return "Target"

        return "Meijer"