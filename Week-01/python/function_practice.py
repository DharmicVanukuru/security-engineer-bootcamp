certificates =[
    {
        "common name" : "abc.com",
        "issuer" : "Sectigo",
        "expiry_days" : 15
    },
    {
       "common name" : "xyz.com",
        "issuer" : "Sectigo",
        "expiry_days" : 99
    },
     {
       "common name" : "kgf.com",
        "issuer" : "Sectigo",
        "expiry_days" : 1
    }
]

def check_certificate(certificate):
    print(certificate["common name"])
    print(certificate["expiry_days"])

    if certificate["expiry_days"] < 30:
        print("Warning")
    else:
        print("Valid")


for certificate in certificates:
    check_certificate(certificate)
    print()