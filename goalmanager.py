import goalaccessor


class GoalManager:
    def __init__(self, goalAccessor: goalaccessor.GoalAccessor):
        self._goalAccessor = goalAccessor
        super().__init__()

    def getGoals(self, user: str) -> list:
        return self._goalAccessor.getGoals(user)

    def getGoal(self, id: int) -> dict:
        return self._goalAccessor.getGoal(id)

    def addGoal(self, goal: dict):
        return self._goalAccessor.addGoal(goal)

    def updateGoal(self, goal: dict):
        return self._goalAccessor.updateGoal(goal)

    def deleteGoal(self, id: int):
        return self._goalAccessor.deleteGoal(id)
