import abc

class InvestmentNotAvailableException(Exception):
    pass


class InvestmentAccessor(abc.ABC):
    @abc.abstractmethod
    def getInvestments(self, user: str) -> list:
        pass

    @abc.abstractmethod
    def getInvestment(self, id: str) -> dict:
        pass

    @abc.abstractmethod
    def addInvestment(self, investment: dict) -> dict:
        pass

    @abc.abstractmethod
    def updateInvestment(self, investment: dict) -> dict:
        pass

    @abc.abstractmethod
    def deleteInvestment(self, id: str):
        pass
