def print_summary(domain, issuer, expiry_days):
    print("\nCertificate Summary")
    print("-------------------")
    print(f"Domain : {domain}")
    print(f"Issuer : {issuer}")
    print(f"Expiry : {expiry_days} days")

domain = input("Enter domain: ")
issuer = input("Enter issuer: ")
expiry_days = int(input("Enter the expiry days: "))

print_summary(domain, issuer, expiry_days)

if expiry_days < 30:
    print("Status : Warning")
elif 30 <= expiry_days <= 90:
    print("Status : Expiring Soon")
else :
    print("Status : Valid")