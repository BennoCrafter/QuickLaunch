from models.alias_data import AliasData


class Alias:
    def __init__(self, alias: str, data: AliasData, description: str = "") -> None:
        self.alias: str = alias
        self.description = description
        self.data: AliasData = data

    def to_dict(self) -> dict:
        """Convert the Alias instance to a dictionary."""
        return {
            'alias': self.alias,
            'description': self.description,
            'data': self.data.to_dict()  # Assuming AliasData also has a to_dict method
        }
