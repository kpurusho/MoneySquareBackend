import goal.goalaccessor
import goal.goalaccessordb
#import goalacccessormock

class GoalAccessorFactory:
    def getGoalAccessor(self) -> goal.goalaccessor.GoalAccessor:
        return goal.goalaccessordb.GoalAccessorDb()
        # return goalaccessormock.GoalAccessorMock()
