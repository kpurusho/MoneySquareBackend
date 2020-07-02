from azure.cosmos import exceptions, CosmosClient, PartitionKey
import goal.goalaccessor


class GoalAccessorDb(goal.goalaccessor.GoalAccessor):
    def __init__(self):
        endpoint = "https://moneysquare.documents.azure.com:443/"
        key = 'weo3vRIX2wSInZ1u4CYP18W2k55p2CZdYjnCyTo1CKpVuq3f8Ebk6SqCisW2O1J6znN49AF4vTkvCMKThcYdOQ=='
        self.client = CosmosClient(endpoint, key)
        database_name = 'MoneySquareDatabase'
        database = self.client.create_database_if_not_exists(id=database_name)
        container_name = 'GoalContainer'
        self.container = database.create_container_if_not_exists(
            id=container_name, 
            partition_key=PartitionKey(path="/id"),
            offer_throughput=400
        )
        super().__init__()

    def getGoals(self, user: str) -> list:
        query = 'SELECT * FROM c WHERE c.user IN ("' + user + '")'

        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items

    def getGoal(self, id: str) -> dict:
        query = 'SELECT * FROM c WHERE c.id IN ("' + id + '")'

        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items[0]

    def addGoal(self, goal: dict) -> dict:
        #goal['id'] = self.getNewGoalId()
        self.container.create_item(body=goal)

    def updateGoal(self, goal: dict) -> dict:
        read_item = self.container.read_item(item=goal['id'], partition_key=goal['id'])
        for k in goal:
            read_item[k] = goal[k]
        return self.container.replace_item(item=read_item, body=read_item)

    def deleteGoal(self, id: str):
        self.container.delete_item(item=id, partition_key=id)

