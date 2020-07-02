import goal.goalaccessor
import datetime
import json
import os


class GoalAccessorMock(goal.goalaccessor.GoalAccessor):
    def __init__(self):
        self._goals = self.readStore()
        super().__init__()

    def getGoals(self, user: str) -> list:
        return self._goals

    def getGoal(self, id: str) -> dict:
        return self.getGoalLocal(id)

    def addGoal(self, goal: dict) -> dict:
        self._goals.append(goal)
        self.saveStore()
        return goal

    def updateGoal(self, goal: dict) -> dict:
        g = self.getGoalLocal(int(goal['id']))
        for k in goal:
            g[k] = goal[k]
        self.saveStore()
        return g

    def deleteGoal(self, id: str):
        g = self.getGoalLocal(id)
        self._goals.remove(g)
        self.saveStore()

    def getGoalLocal(self, id: str) -> dict:
        for g in self._goals:
            if g['id'] == id:
                return g
        raise goal.goalaccessor.GoalNotAvailableException()

    def readStore(self) -> list:
        if os.path.exists('goalstore.json'):
            with open('goalstore.json', mode='r') as mf:
                return json.load(mf)
        return []

    def saveStore(self):
        with open('goalstore.json', mode='w') as mf:
            mf.write(json.dumps(self._goals))
