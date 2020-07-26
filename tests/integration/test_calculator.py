import math
import struct
import app
import unittest

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        pass
        app.app.testing = True
        self.app = app.app.test_client()

    def test_lumpsumReturns(self):
        print('lumpsumReturnsTest')
        data = {
            'presentValue': 1000,
            'rateOfReturn' : 8,
            'investmentDurationInYears' : 10,
            'numberOfCompoundInterestInYear' : 1,
            'recurringMonthlyInvestment' : 0,

        }
        result = math.ceil(float(self.app.get('/lumpsumreturns', query_string = data).data.decode("utf-8")))
        self.assertEqual(2159, result)
        
