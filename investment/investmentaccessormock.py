import investment.investmentaccessor
import datetime
import json
import os


class InvestmentAccessorMock(investment.investmentaccessor.InvestmentAccessor):
    def __init__(self):
        self._investments = self.readStore()
        super().__init__()

    def getInvestments(self, user: str) -> list:
        return self._investments

    def getInvestment(self, id: str) -> dict:
        return self.getInvestmentLocal(id)

    def addInvestment(self, investment: dict) -> dict:
        self._investments.append(investment)
        self.saveStore()
        return investment

    def updateInvestment(self, investment: dict) -> dict:
        g = self.getInvestmentLocal(int(investment['id']))
        for k in investment:
            g[k] = investment[k]
        self.saveStore()
        return g

    def deleteInvestment(self, id: str):
        g = self.getInvestmentLocal(id)
        self._investments.remove(g)
        self.saveStore()

    def getInvestmentLocal(self, id: str) -> dict:
        for g in self._investments:
            if g['id'] == id:
                return g
        raise investment.investmentaccessor.InvestmentNotAvailableException()

    def readStore(self) -> list:
        if os.path.exists('investmentstore.json'):
            with open('investmentstore.json', mode='r') as mf:
                return json.load(mf)
        return []

    def saveStore(self):
        with open('investmentstore.json', mode='w') as mf:
            mf.write(json.dumps(self._investments))
