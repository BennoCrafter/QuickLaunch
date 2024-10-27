class Action:
    def __init__(self, action: str, args=None) -> None:
        self.action = action
        self.args = args if args is not None else []

    def to_dict(self) -> dict:
        return {"action": self.action, "args": self.args}
