import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    rand_str = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    return func.HttpResponse(
        str(rand_str),
        status_code=200
    )
