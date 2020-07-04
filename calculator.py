from math import pow


class Calculator:
    def calculateLumpsumReturns(self, args: dict) -> float:
        presentValue = 0
        if 'presentValue' in args:
            presentValue = float(args['presentValue'])

        if 'rateOfReturn' in args:
            rateOfReturn = float(args['rateOfReturn'])

        if 'investmentDurationInYears' in args:
            investmentDurationInYears = float(
                args['investmentDurationInYears'])

        if 'numberOfCompoundInterestInYear' in args:
            numberOfCompoundInterestInYear = int(
                args['numberOfCompoundInterestInYear'])

        recurringMonthlyInvestment = 0
        if 'recurringMonthlyInvestment' in args:
            recurringMonthlyInvestment = int(
                args['recurringMonthlyInvestment'])

        rateOfReturn = rateOfReturn/100
        lumpSum = self.calculateLumpsum(presentValue, rateOfReturn, investmentDurationInYears, numberOfCompoundInterestInYear)
        recurringSum = self.calculateRecurringInvestmentMaturity(presentValue, rateOfReturn, investmentDurationInYears, numberOfCompoundInterestInYear, recurringMonthlyInvestment)
        return  lumpSum + recurringSum

    def calculateLumpsum(self, presentValue: float, rateOfReturn: float, investmentDurationInYears: float, numberOfCompoundInterestInYear: float):
        return presentValue * (pow((1+(rateOfReturn/numberOfCompoundInterestInYear)), (numberOfCompoundInterestInYear * investmentDurationInYears)))

    def calculateRecurringInvestmentMaturity(self,  presentValue: float, rateOfReturn: float, 
    investmentDurationInYears: float, numberOfCompoundInterestInYear: float, recurringMonthlyInvestment: float):
        numberOfQuaters = investmentDurationInYears*4.0
        return recurringMonthlyInvestment * (pow((1+(rateOfReturn/4)),numberOfQuaters)-1)/(1-(pow((1+(rateOfReturn/4)),(-1/3))))
