import requests
wassitNumber = input("Enter the WASSIT number: ")
identityDocNumber = input("Enter the identity document number: ")
url = "https://ac-controle.anem.dz/AllocationChomage/api/validateCandidate/query?wassitNumber={}&identityDocNumber={}".format(wassitNumber, identityDocNumber)
response = requests.get(url)
data = response.json()
if data["status"] == "ERROR":
    print("The server is under pressure. Please try again later.")
else:
    print(json.dumps(data, indent=4, sort_keys=True))
