"""
Account Service

This microservice handles the lifecycle of Accounts
"""
# pylint: disable=unused-import
from flask import jsonify, request, make_response, abort, url_for   # noqa; F401
from service.models import Account
from service.common import status  # HTTP Status Codes
from . import app  # Import Flask application
<<<<<<< HEAD
import json
=======
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a


############################################################
# Health Endpoint
############################################################
@app.route("/health")
def health():
<<<<<<< HEAD
    """
    Health Status
    """
=======
    """Health Status"""
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a
    return jsonify(dict(status="OK")), status.HTTP_200_OK


######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
<<<<<<< HEAD
    """
    Root URL response
    """
=======
    """Root URL response"""
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a
    return (
        jsonify(
            name="Account REST API Service",
            version="1.0",
            # paths=url_for("list_accounts", _external=True),
        ),
        status.HTTP_200_OK,
    )


######################################################################
# CREATE A NEW ACCOUNT
######################################################################
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """
    Creates an Account
    This endpoint will create an Account based the data in the body that is posted
    """
    app.logger.info("Request to create an Account")
    check_content_type("application/json")
    account = Account()
    account.deserialize(request.get_json())
    account.create()
    message = account.serialize()
    # Uncomment once get_accounts has been implemented
    # location_url = url_for("get_accounts", account_id=account.id, _external=True)
    location_url = "/"  # Remove once get_accounts has been implemented
    return make_response(
        jsonify(message), status.HTTP_201_CREATED, {"Location": location_url}
    )

<<<<<<< HEAD

######################################################################
# LIST ALL ACCOUNTS
######################################################################
@app.route("/accounts", methods=["GET"])
def list_accounts():
    """
    List all Accounts
    This endpoint returns all Accounts as a list
    """
    accounts = Account.all()
    if not accounts:
        return json.dumps([], default=str), status.HTTP_200_OK
    return make_response(
        json.dumps(accounts, default=str), status.HTTP_200_OK
    )
=======
######################################################################
# LIST ALL ACCOUNTS
######################################################################

# ... place you code here to LIST accounts ...
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a


######################################################################
# READ AN ACCOUNT
######################################################################
<<<<<<< HEAD
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    """
    Reads an Account
    This endpoint will read an Account based on the account_id that is requested
    """
    app.logger.info("Request to read an Account with id: %s", account_id)
    account = Account.find(account_id)
    if not account:
        abort(status.HTTP_404_NOT_FOUND, f"Account with id [{account_id}] could not be found.")
    return account.serialize(), status.HTTP_200_OK
=======

# ... place you code here to READ an account ...
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a


######################################################################
# UPDATE AN EXISTING ACCOUNT
######################################################################
<<<<<<< HEAD
@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    """
    Updates an Account information
    This endpoint will update an already existing Account information based on the account_id that is requested
    """
    app.logger.info("Request to read an Account with id: %s", account_id)
    account = Account.find(account_id)
    if not account:
        abort(status.HTTP_404_NOT_FOUND, f"Account with id [{account_id}] could not be found.")
    account.deserialize(request.get_json())
    account.update()
    return account.serialize(), status.HTTP_200_OK
=======

# ... place you code here to UPDATE an account ...
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a


######################################################################
# DELETE AN ACCOUNT
######################################################################
<<<<<<< HEAD
@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """
    Deletes a single Account
    This endpoint will delete an existing account based on the account_id that is requested
    """
    app.logger.info("Request to read an Account with id: %s", account_id)
    account = Account.find(account_id)
    if account:
        account.delete()
    return "", status.HTTP_204_NO_CONTENT
=======

# ... place you code here to DELETE an account ...
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################
<<<<<<< HEAD
def check_content_type(media_type):
    """
    Checks that the media type is correct
    """
=======


def check_content_type(media_type):
    """Checks that the media type is correct"""
>>>>>>> 1b50c88e08626c848688a42c96143d6b41d5eb1a
    content_type = request.headers.get("Content-Type")
    if content_type and content_type == media_type:
        return
    app.logger.error("Invalid Content-Type: %s", content_type)
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}",
    )
