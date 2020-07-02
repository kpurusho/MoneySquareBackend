import investment.investmentaccessor


class InvestmentManager:
    def __init__(self, investmentAccessor: investment.investmentaccessor.InvestmentAccessor):
        self._investmentAccessor = investmentAccessor
        super().__init__()

    def getInvestments(self, user: str) -> list:
        return self._investmentAccessor.getInvestments(user)

    def getInvestment(self, id: str) -> dict:
        return self._investmentAccessor.getInvestment(id)

    def addInvestment(self, investment: dict):
        return self._investmentAccessor.addInvestment(investment)

    def updateInvestment(self, investment: dict):
        return self._investmentAccessor.updateInvestment(investment)

    def deleteInvestment(self, id: str):
        return self._investmentAccessor.deleteInvestment(id)
