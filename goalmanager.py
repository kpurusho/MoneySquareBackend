import goalaccessor


class GoalManager:
    def __init__(self, goalAccessor: goalaccessor.GoalAccessor):
        self._goalAccessor = goalAccessor
        super().__init__()

    def getGoals(self, user: str) -> list:
        return self._goalAccessor.getGoals(user)

    def getGoal(self, id: str) -> dict:
        return self._goalAccessor.getGoal(id)

    def addGoal(self, goal: dict):
        return self._goalAccessor.addGoal(goal)

    def updateGoal(self, goal: dict):
        return self._goalAccessor.updateGoal(goal)

    def deleteGoal(self, id: str):
        return self._goalAccessor.deleteGoal(id)
