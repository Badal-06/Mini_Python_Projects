import phonenumbers
from phonenumbers import geocoder , carrier 

number = str(input("enter your phone number with country code: "))

ch_number = phonenumbers.parse(number,"CH")
print("location: " ,geocoder.description_for_number(ch_number,"en"))

service_number = phonenumbers.parse(number,"RO")
print("carrier: ", carrier.name_for_number(service_number,"en"))