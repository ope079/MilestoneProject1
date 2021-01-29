import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    random_num = random.randint(10000, 99999)

    return   func.HttpResponse(

        str(random_num),
        status_code=200
    ) 
