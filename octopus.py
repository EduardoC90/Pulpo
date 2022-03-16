import requests
import json, os, time
from colorama import Fore

# NO ROBES, JOTO

banner = Fore.CYAN + """

                888                                    
                888                                    
                888                                    
 .d88b.  .d8888b888888 .d88b. 88888b. 888  888.d8888b  
d88""88bd88P"   888   d88""88b888 "88b888  88888K      
888  888888     888   888  888888  888888  888"Y8888b. 
Y88..88PY88b.   Y88b. Y88..88P888 d88PY88b 888     X88 
 "Y88P"  "Y8888P "Y888 "Y88P" 88888P"  "Y88888 88888P' 
                              888                      
                              888                      
                              888                      """
print(banner)
print("                                               By gogo")
try:
   phone_number = input("Escribe un numero: ")
   print("--------------------------------------")
#change for your API KEY
   access_key = '5c8cc90d6e39f2643e01454fb4bb4172'
   url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
   response = requests.get(url)
   answer = response.json()

   if answer["valid"] == True:
    #print(answer)
    print(Fore.RED + "Number:",answer["number"])
    print("International format:",answer["international_format"])
    print("Country prefix:",answer["country_prefix"])
    print("Country name:",answer["country_name"])
    print("Location:",answer["location"])
    print("Carrier:",answer["carrier"])
    print("Line type:",answer["line_type"])
   else:
    print("El numero no existe")
except KeyboardInterrupt:
    print(Fore.YELLOW + "\nSaliendo")