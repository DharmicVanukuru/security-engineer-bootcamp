domain = input("Enter domain: ")
issuer = input("Enter issuer: ")
expiry_days = int(input("Enter the expiry days: "))

print("\nCertificate Summary")
print("--------------------")
print("Domain :", domain)
print("Issuer :", issuer)
print("Expiry :", expiry_days, "days")

if expiry_days < 30:
    print("Status : Warning")
else:
    print("Status : Valid")