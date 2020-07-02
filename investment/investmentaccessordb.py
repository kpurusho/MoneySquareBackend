from azure.cosmos import exceptions, CosmosClient, PartitionKey
import investment.investmentaccessor


class InvestmentAccessorDb(investment.investmentaccessor.InvestmentAccessor):
    def __init__(self):
        endpoint = "https://moneysquare.documents.azure.com:443/"
        key = 'weo3vRIX2wSInZ1u4CYP18W2k55p2CZdYjnCyTo1CKpVuq3f8Ebk6SqCisW2O1J6znN49AF4vTkvCMKThcYdOQ=='
        self.client = CosmosClient(endpoint, key)
        database_name = 'MoneySquareDatabase'
        database = self.client.create_database_if_not_exists(id=database_name)
        container_name = 'InvestmentContainer'
        self.container = database.create_container_if_not_exists(
            id=container_name, 
            partition_key=PartitionKey(path="/id"),
            offer_throughput=400
        )
        super().__init__()

    def getInvestments(self, user: str) -> list:
        query = 'SELECT * FROM c WHERE c.user IN ("' + user + '")'

        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items

    def getInvestment(self, id: str) -> dict:
        query = 'SELECT * FROM c WHERE c.id IN ("' + id + '")'

        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return items[0]

    def addInvestment(self, investment: dict) -> dict:
        self.container.create_item(body=investment)

    def updateInvestment(self, investment: dict) -> dict:
        read_item = self.container.read_item(item=investment['id'], partition_key=investment['id'])
        for k in investment:
            read_item[k] = investment[k]
        return self.container.replace_item(item=read_item, body=read_item)

    def deleteInvestment(self, id: str):
        self.container.delete_item(item=id, partition_key=id)

