import abc


class GoalNotAvailableException(Exception):
    pass


class GoalAccessor(abc.ABC):
    @abc.abstractmethod
    def getGoals(self, user: str) -> list:
        pass

    @abc.abstractmethod
    def getGoal(self, id: str) -> dict:
        pass

    @abc.abstractmethod
    def addGoal(self, goal: dict) -> dict:
        pass

    @abc.abstractmethod
    def updateGoal(self, goal: dict) -> dict:
        pass

    @abc.abstractmethod
    def deleteGoal(self, id: str):
        pass
