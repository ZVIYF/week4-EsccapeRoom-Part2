class Utils:


    @staticmethod
    def item_by_ID(item_id: str, objects: list):
        for item in objects:
            if item["id"] == item_id:
                return item


    @staticmethod
    def search_by_value(key:str, value, objects: list[object], partial=False)-> list:
        if partial:
            return list(filter(lambda item: value in item.getattr(key), objects))
        return list(filter(lambda item: item.getattr(key) == value, objects))
    