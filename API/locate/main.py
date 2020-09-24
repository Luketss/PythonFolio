import requests

def get_google_api_key():
    with open('api-key.txt', 'r') as file:
        api_key = file.read()
    return api_key

def get_the_address():
    
    place_of_start = input("Define start address: ")

    place_of_end = input("Define end place: ")

def get_google_location():
    pass

a = get_google_api_key()

print(a)
