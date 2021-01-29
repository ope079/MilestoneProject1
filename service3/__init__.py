import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    rand_str = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(5))
    return func.HttpResponse(
        str(rand_str),
        status_code=200
    )
