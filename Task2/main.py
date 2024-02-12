from flask import Flask
from flask import request
from flask import Response

from Services.salesService import getUnauthorizedSellers

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello_world():

    try:
        # Read data from request body
        json_data = request.get_json(force=True)

        productListings = json_data["productListings"]
        salesTransactions = json_data["salesTransactions"]

        return getUnauthorizedSellers(productListings, salesTransactions)

    except:
        return Response(
            "{}",
            status=400,
        )
