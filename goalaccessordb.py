import goalaccessor


class GoalAccessorDb(goalaccessor.GoalAccessor):
    def __init__(self):
        super().__init__()

    def getGoals(self, user: str) -> list:
        pass

    def getGoal(self, id: int) -> dict:
        pass

    def addGoal(self, goal: dict) -> dict:
        pass

    def updateGoal(self, goal: {}) -> dict:
        pass

    def deleteGoal(self, id: int):
        pass
