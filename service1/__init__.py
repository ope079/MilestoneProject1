import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey



endpoint = ''
key = ''


client = CosmosClient(endpoint, key)

database_name = 'RandomDatabase'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'RandomDBContainer'
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/random"), 
    offer_throughput=400
)





def main(req: func.HttpRequest) -> func.HttpResponse:
    rand_int = requests.get('https://function079.azurewebsites.net/api/Service2?code=OQ7NqJoVXySydhZ8iFV/9O849dseyfcr1SIC9f7GFok0iFMCaDS0zQ==')
    rand_str = requests.get('https://function079.azurewebsites.net/api/service3?code=T/WnvvaZuwb8i68eBItAgI6rVruEyafQvagmSmeaCzp836G1UiwZ7A==')
    rand_val = rand_int.text + rand_str.text
    

    container.create_item(body={
        "id": 1, 
        "random_name" : rand_val
    })
   
    
    return func.HttpResponse(
        rand_val,
        status_code=200
    )
