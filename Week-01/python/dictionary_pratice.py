# certificate = {
#     "domain": "abc.com",
#     "issuer": "Sectigo",
#     "expiry_days": 45,
#     "key_size": 2048
# }

# certificate["status"] = "Expiring soon"
# certificate["algorithm"] = "SHA 256"


# # print(certificate["algorithm"])
# # print(certificate.keys())
# # print(certificate.values())
# for key, value in certificate.items():
#     print(key,":", value)


certificates = [
    {
        "domain": "abc.com",
        "expiry_days": 120
    },
    {
        "domain": "bank.com",
        "expiry_days": 15
    }
]

for certificate in certificates:
    print(certificate["domain"])
    print(certificate["expiry_days"])

    if certificate["expiry_days"] < 30:
     print("Status : warning")
    else:
     print("Status : valid")
    
    print()

