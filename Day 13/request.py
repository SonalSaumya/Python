import requests

response = requests.get('https://restcountries.com/v3.1/all')

if response.status_code == 200:
    print("Response recieved")
else:
    print("Failed to receive ",response.status_code)

countries = response.json()

for c in countries:
    name = c.get('name',{}).get('common','N/A')
    capital = c.get('capital',['N/A'])[0]
    area = c.get('area','N/A')

    if name == 'India':
        print(f"Country : {name}" )
        print(f"Capital : {capital}")
        print(f"Area : {area}")


