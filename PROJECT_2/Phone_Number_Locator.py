import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Enter your phone number with country code: ")

parsed_number = phonenumbers.parse(number)  # no region override needed

# Get location
location = geocoder.description_for_number(parsed_number, "en")
print("Location:", location)

# Get carrier
service_provider = carrier.name_for_number(parsed_number, "en")
print("Carrier:", service_provider)