from os import environ
from azure.communication.email import EmailClient
import azure.functions as func
import datetime
import json
import logging


app = func.FunctionApp()


@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.FUNCTION)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    connection_string = environ.get("EMAIL_SERVICE_CONNECTION_STRING")
    # logging.info("connection_string: {connection_string}".format(connection_string=connection_string))
    client = EmailClient.from_connection_string(connection_string)
    
    message = {
        "content": {
            "subject": "This is the subject",
            "plainText": "This is the body",
            "html": "<html><h1>This is the body</h1></html>"
        },
        "recipients": {
            "to": [
                {
                    "address": "alberto@onamail.com",
                    "displayName": "Alberto (My Friend)"
                }
            ]
        },
        "senderAddress": "DoNotReply@drimerdev.site"
    }

    poller = client.begin_send(message)
    result = poller.result()
    
    breakpoint()
    
    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )