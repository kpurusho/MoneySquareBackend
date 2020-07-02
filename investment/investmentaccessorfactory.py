import investment.investmentaccessor
import investment.investmentaccessordb
#import investmentacccessormock

class InvestmentAccessorFactory:
    def getInvestmentAccessor(self) -> investment.investmentaccessor.InvestmentAccessor:
        return investment.investmentaccessordb.InvestmentAccessorDb()
        # return investmentaccessormock.InvestmentAccessorMock()
