import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    rand_int = requests.get('https://milestonep.azurewebsites.net/api/Service2?code=rwdH4XLcYAnu6OJhqfTamF/NKcXEVODa4L15Ok1XuYwwexVl8LXkWA==')
    rand_str = requests.get('https://milestonep.azurewebsites.net/api/service3?code=/c0gAOFQYqflLf3ePnKzPTuc4yMAtSMjvii05pzGLqjI746D9KwXzw==')
    rand_val =  rand_int.text + rand_str.text


    # Initialize the Cosmos client
    endpoint = "https://milestone.documents.azure.com:443/"
    key = 'K3ceqtLPD6EhUNhKo5CiGlIiDOzZPaqV37lFqps7408O8kIqddhXavClXctzM528oRTfPE0mZf2ZndTGiumbnQ=='

    # <create_cosmos_client>
    client = CosmosClient(endpoint, key)
    # </create_cosmos_client>

    # Create a database
    # <create_database_if_not_exists>
    database_name = 'AzureRandomDatabase'
    database = client.create_database_if_not_exists(id=database_name)
    # </create_database_if_not_exists>

    # Create a container
    # Using a good partition key improves the performance of database operations.
    # <create_container_if_not_exists>
    container_name = 'RandomDBContainer'
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path="/lastName"),
        offer_throughput=400
    )
    # </create_container_if_not_exists>


    # Add items to the container
    random_items_to_create = [rand_val]

    # <create_item>
    container.create_item(body=random_items_to_creat)
    # </create_item>





    return func.HttpResponse(
        str(rand_val),
        status_code=200
    )
