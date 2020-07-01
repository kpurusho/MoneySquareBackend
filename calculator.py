from math import pow


class Calculator:
    def calculateLumpsumReturns(self, args:dict) -> float:
        if 'presentValue' in args:
            presentValue = float(args['presentValue'])

        if 'rateOfReturn' in args:
            rateOfReturn = float(args['rateOfReturn'])

        if 'investmentDurationInYears' in args:
            investmentDurationInYears = float(args['investmentDurationInYears'])

        if 'numberOfCompoundInterestInYear' in args:
            numberOfCompoundInterestInYear = int(args['numberOfCompoundInterestInYear'])

        rateOfReturn = rateOfReturn/100
        return presentValue * (pow((1+(rateOfReturn/numberOfCompoundInterestInYear)), (numberOfCompoundInterestInYear * investmentDurationInYears)))
