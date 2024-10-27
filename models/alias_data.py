from models.action import Action


class AliasData:
    def __init__(self, path: str, action: Action) -> None:
        self.path: str = path
        self.action: Action = action

    def get_last_path_component(self) -> str:
        return self.path.split("/")[-1]

    def to_dict(self) -> dict:
        return {"path": self.path, "action": self.action.to_dict()}
