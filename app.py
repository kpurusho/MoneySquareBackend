from flask import Flask, request
from flask_cors import CORS
import calculator
import goalmanager
import goalaccessormock
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

    goalManager = goalmanager.GoalManager(goalaccessormock.GoalAccessorMock())
    return json.dumps(goalManager.getGoals(user))


@app.route('/goals/<id>', methods=['GET'])
def getGoal(id):
    goalManager = goalmanager.GoalManager(goalaccessormock.GoalAccessorMock())
    return json.dumps(goalManager.getGoal(id))


@app.route('/goals/<id>', methods=['DELETE'])
def deleteGoal(id):
    goalManager = goalmanager.GoalManager(goalaccessormock.GoalAccessorMock())
    return json.dumps(goalManager.deleteGoal(id))


@app.route('/goals/<id>', methods=['PUT'])
def updateGoal(id):
    goal = request.json
    goalManager = goalmanager.GoalManager(goalaccessormock.GoalAccessorMock())
    return json.dumps(goalManager.updateGoal(goal))


@app.route('/goals', methods=['POST'])
def createGoal():
    goal = request.json
    goalManager = goalmanager.GoalManager(goalaccessormock.GoalAccessorMock())
    return json.dumps(goalManager.addGoal(goal))


if __name__ == '__main__':
    app.run(debug=True)
