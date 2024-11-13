import  requests
response = requests.get('https://restcountries.com/v3.1/all')

if response.status_code == 200:
    print("Response recieved")
else:
    print("Failed to receive ",response.status_code)

countries = response.json()


r = input("Enter region : ")

try:
    for c in countries:
        name=""
        capital=""
        area=""

        name = c.get('name', {}).get('common', 'N/A')
        capital = c.get('capital', ['N/A'])[0]
        area = c.get('area', 'N/A')
        reg = c.get('region', 'N/A')
        # ccode = c.get('currencies', 'N/A')

    if name == r:
        print(f"Country : {name}")
        print(f"Capital : {capital}")
        print(f"Area : {area}")
        print(f"Region : {reg}")
        #print(f"Currency code : {ccode}")
    else:
        print("Not found")

except Exception as e:
    print("Not found",e)






