from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API

PAYMENT = {
    "c8e7c816-2d84-43cb-b961-15cae477a3b5":
    {
        "sessionToken": "7a1U5u6q1I6g9t7P5j1x4V6g5n6I4a1i3W0e5u2W4f3s7J2h6c8K8c9n4R5b7o3Q8z1f5O4c7w3H9h2f8Y9e4b4T6p6s4B9t8q7T3k0a6G0d3f5F0b5i8D3f5h9W2g3q",
        "payment": {
            "id" : 563,
            "idPayment" : "c8e7c816-2d84-43cb-b961-15cae477a3b5",
            "amount" : {
                "currency" : "EUR",
                "currencyNumber" : None,
                "amount" : 5415471,
                "decimalDigits" : 2
            },
            "email" : "test123@example.com",
            "subject" : "Pagamento",
            "receiver" : "PagoPa",
            "urlRedirectEc" : "http://localhost:8082/pa/ec?paymentId=a9711488-12fe-4a91-8b5a-f58f0b2657d2",
            "isCancelled" : False,
            "bolloDigitale" : False,
            "fiscalCode" : "SXOBBP86C06G702J",
            "origin" : "WALLET_APP",
            "idCarrello" : "fQT2qIxBzZVYuIz",
            "detailsList" : [ {
                "idPayment" : None,
                "IUV" : "iuv_aIPnRTwbJqzNJhv",
                "CCP" : "ccp_PuvdmMOjTTUUGuy",
                "idDominio" : "idD_cgYbyOZFbGZNPxH",
                "enteBeneficiario" : "Vertapple TAFE",
                "importo" : 54154.71,
                "tipoPagatore" : "G",
                "codicePagatore" : "YJIFYF96C50I471P",
                "nomePagatore" : "Lucia D'amico"
            } ],
            "iban" : "IT28V7783068935Q514JA19BB8U"
        }
    }
}

TRANSACTION = {
        "id" : 1803,
        "created" : 1599465491145,
        "updated" : 1599465491145,
        "amount" : {
            "currency" : "EUR",
            "currencyNumber" : None,
            "amount" : 5415471,
            "decimalDigits" : 2
        },
        "grandTotal" : {
            "currency" : "EUR",
            "currencyNumber" : None,
            "amount" : 5415582,
            "decimalDigits" : 2
        },
        "description" : "Pagamento",
        "merchant" : "PagoPa",
        "idStatus" : 0,
        "statusMessage" : "Da autorizzare",
        "error" : False,
        "success" : False,
        "fee" : {
            "currency" : "EUR",
            "currencyNumber" : None,
            "amount" : 111,
            "decimalDigits" : 2
        },
        "urlRedirectPSP" : None,
        "urlCheckout3ds" : "http://pagopa-dev:8080/wallet/checkout?id=MTgwMw==",
        "paymentModel" : 0,
        "token" : "MTgwMw==",
        "idWallet" : 223,
        "idPsp" : 22,
        "idPayment" : 563,
        "nodoIdPayment" : "60628ff0-a24a-4586-819c-4f8b6ea4c021",
        "spcNodeDescription" : None,
        "spcNodeStatus" : None,
        "accountingStatus" : None,
        "authorizationCode" : None,
        "orderNumber" : 1803,
        "rrn" : None,
        "numAut" : None,
        "paymentCancelled" : False,
        "detailsList" : [ {
            "idPayment" : None,
            "IUV" : "iuv_aIPnRTwbJqzNJhv",
            "CCP" : "ccp_PuvdmMOjTTUUGuy",
            "idDominio" : "idD_cgYbyOZFbGZNPxH",
            "enteBeneficiario" : "Vertapple TAFE",
            "importo" : 54154.71,
            "tipoPagatore" : "G",
            "codicePagatore" : "YJIFYF96C50I471P",
            "nomePagatore" : "Lucia D'amico"
        } ],
        "directAcquirer" : True
    }

WALLET = {
        "idWallet" : 223,
        "creditCard" : {
            "id" : 200,
            "holder" : "Mary Reyes",
            "pan" : "************0006",
            "expireMonth" : "11",
            "expireYear" : "34",
            "securityCode" : None,
            "brandLogo" : "http://localhost:8080/wallet/assets/img/creditcard/carta_visa.png",
            "flag3dsVerified" : False,
            "brand" : "VISA",
            "onUs" : True
        }
        
        # ,
        # "psp" : {
        #     "id" : 22,
        #     "idPsp" : "NEXI_Visa",
        #     "businessName" : "Psp NEXI 2",
        #     "paymentType" : "CP",
        #     "idIntermediary" : "Psp Nexi",
        #     "idChannel" : "NEXI (Visa)",
        #     "logoPSP" : "http://pagopa-dev:8080/pp-restapi/v3/resources/psp/22",
        #     "serviceLogo" : "http://pagopa-dev:8080/pp-restapi/v3/resources/service/22",
        #     "serviceName" : "NEXI (Visa)",
        #     "fixedCost" : {
        #         "currency" : "EUR",
        #         "currencyNumber" : None,
        #         "amount" : 111,
        #         "decimalDigits" : 2
        #     },
        #     "appChannel" : False,
        #     "tags" : None,
        #     "serviceDescription" : None,
        #     "serviceAvailability" : "NEXI",
        #     "urlInfoChannel" : None,
        #     "paymentModel" : 1,
        #     "flagStamp" : True,
        #     "idCard" : 99997,
        #     "isCancelled" : None,
        #     "lingua" : "IT",
        #     "codiceAbi" : "99997",
        #     "isPspOnus" : False,
        #     "participant" : None,
        #     "codiceConvenzione" : None,
        #     "isDirectAcquirer" : None,
        #     "favoriteSellerCharge" : None,
        #     "cancelled" : None,
        #     "solvedByPan" : False
        # },
        # "idPsp" : 22,
        # "pspEditable" : False,
        # "lastUsage" : None,
        # "idPagamentoFromEC" : None,
        # "pspListNotOnUs" : None,
        # "isPspToIgnore" : False,
        # "registeredNexi" : False,
        # "matchedPsp" : None
    }
