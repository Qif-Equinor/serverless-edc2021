import logging
import os
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Monitor Github push
    :param req: HttpRequest
    :return:  HttpResponse
    """
    logging.info('GitHub Monitor processed a request.')
    var = os.environ.get("VARIABLE_FOO")
    logging.info(var)
    req_body = req.get_body()

    json_body = json.loads(req_body.decode())
    logging.info(json_body)
    return func.HttpResponse(f"Hello {json_body}!")
