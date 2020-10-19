from payment import PAYMENT as payment
from payment import TRANSACTION as transaction
from payment import WALLET as wallet_res

from flask import make_response, abort, request

def startSession(idPayment):    
    if idPayment in payment:
        return payment[idPayment]
    else:
        abort(404, f"startSession error {idPayment} not found")


def pay(idPayment):
    # req_data = request.data
    # print(req_data)
    if idPayment in payment:
        return transaction
    else:
        abort(404, f"pay error {idPayment} not found")

def addWallet():
    return wallet_res


