from flask import Flask, request
from flask_cors import CORS
import calculator
import goal.goalmanager
import goal.goalaccessor
import goal.goalaccessorfactory
import investment.investmentmanager
import investment.investmentaccessor
import investment.investmentaccessorfactory
import json

app = Flask(__name__)
CORS(app)
app.secret_key = "MoneySquareBackend"


@app.route('/lumpsumreturns', methods=['GET'])
def getLumpsumpReturns():
    calc = calculator.Calculator()
    result = calc.calculateLumpsumReturns(request.args)
    return str(result)


@app.route('/goals', methods=['GET'])
def getGoals():
    args = request.args
    if 'user' in args:
        user = args['user']

    goalManager = goal.goalmanager.GoalManager(goal.goalaccessorfactory.GoalAccessorFactory().getGoalAccessor())
    return json.dumps(goalManager.getGoals(user))


@app.route('/goals/<id>', methods=['GET'])
def getGoal(id):
    goalManager = goal.goalmanager.GoalManager(goal.goalaccessorfactory.GoalAccessorFactory().getGoalAccessor())
    return json.dumps(goalManager.getGoal(id))


@app.route('/goals/<id>', methods=['DELETE'])
def deleteGoal(id):
    goalManager = goal.goalmanager.GoalManager(goal.goalaccessorfactory.GoalAccessorFactory().getGoalAccessor())
    return json.dumps(goalManager.deleteGoal(id))


@app.route('/goals/<id>', methods=['PUT'])
def updateGoal(id):
    g = request.json
    goalManager = goal.goalmanager.GoalManager(goal.goalaccessorfactory.GoalAccessorFactory().getGoalAccessor())
    return json.dumps(goalManager.updateGoal(g))


@app.route('/goals', methods=['POST'])
def createGoal():
    g = request.json
    goalManager = goal.goalmanager.GoalManager(goal.goalaccessorfactory.GoalAccessorFactory().getGoalAccessor())
    return json.dumps(goalManager.addGoal(g))



@app.route('/investments', methods=['GET'])
def getInvestments():
    args = request.args
    if 'user' in args:
        user = args['user']

    investmentManager = investment.investmentmanager.InvestmentManager(investment.investmentaccessorfactory.InvestmentAccessorFactory().getInvestmentAccessor())
    return json.dumps(investmentManager.getInvestments(user))


@app.route('/investments/<id>', methods=['GET'])
def getInvestment(id):
    investmentManager = investment.investmentmanager.InvestmentManager(investment.investmentaccessorfactory.InvestmentAccessorFactory().getInvestmentAccessor())
    return json.dumps(investmentManager.getInvestment(id))


@app.route('/investments/<id>', methods=['DELETE'])
def deleteInvestment(id):
    investmentManager = investment.investmentmanager.InvestmentManager(investment.investmentaccessorfactory.InvestmentAccessorFactory().getInvestmentAccessor())
    return json.dumps(investmentManager.deleteInvestment(id))


@app.route('/investments/<id>', methods=['PUT'])
def updateInvestment(id):
    g = request.json
    investmentManager = investment.investmentmanager.InvestmentManager(investment.investmentaccessorfactory.InvestmentAccessorFactory().getInvestmentAccessor())
    return json.dumps(investmentManager.updateInvestment(g))


@app.route('/investments', methods=['POST'])
def createInvestment():
    g = request.json
    investmentManager = investment.investmentmanager.InvestmentManager(investment.investmentaccessorfactory.InvestmentAccessorFactory().getInvestmentAccessor())
    return json.dumps(investmentManager.addInvestment(g))

if __name__ == '__main__':
    app.run(debug=True)
