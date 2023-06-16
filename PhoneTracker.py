import colorama
import phonenumbers
import subprocess
import geopy
from colorama import Fore, Style

from phonenumbers import geocoder, carrier, timezone, data, shortnumberinfo, region_code_for_country_code, region_code_for_number, PhoneMetadata, COUNTRY_CODE_TO_REGION_CODE
from geopy.geocoders import Nominatim


print ("")
print ("Countries that you can get all avalaible info in a phone number")

print("---------------------------------------------------------------------------------")
print(" Pakistan, Spain, Romoania, Morena, Unite Kingdom, Egypt ")
print("---------------------------------------------------------------------------------")

print ("")
phone = input("Enter the phone number target: ")
Target =  phonenumbers.parse (phone, None)
Country = geocoder.country_name_for_number(Target, "en")
ISP = carrier.name_for_number(Target, "en")
Validation = phonenumbers.is_valid_number(Target)
Number_Validation = phonenumbers.is_possible_number(Target)
Diall_Validation = phonenumbers.phonenumberutil.can_be_internationally_dialled(Target)
Carrier_Specific = phonenumbers.is_carrier_specific(Target)
CC = phonenumbers.phonenumberutil.region_code_for_country_code(Target.country_code)
Time = timezone.time_zones_for_geographical_number(Target)
Line = phonenumbers.phonenumberutil.number_type(Target)
TrunkCode = geocoder.description_for_valid_number(Target, "en")
lineTypeVal = phonenumbers.is_possible_number_for_type(Target, numtype=Line)


subprocess.call(["bash","animation.sh"]) 

print("")
print(Style.BRIGHT+Fore.BLUE + "---------------------------------------------------------------------------------")
print (Style.BRIGHT+Fore.GREEN + "Country Digit:" + Style.BRIGHT+Fore.WHITE  ,Target.country_code)
print (Style.BRIGHT+Fore.GREEN + "National number:" + Style.BRIGHT+Fore.WHITE ,Target.national_number)
print (Style.BRIGHT+Fore.GREEN + "Country: " + Style.BRIGHT+Fore.WHITE  + Country)
print (Style.BRIGHT+Fore.GREEN + "Country Code:" + Style.BRIGHT+Fore.WHITE  ,CC )


if TrunkCode == Country: print (Style.BRIGHT+Fore.GREEN + "Area:" + Style.BRIGHT+Fore.YELLOW ,"Unknow")
else: print(Style.BRIGHT+Fore.GREEN + "Area:" + Style.BRIGHT+Fore.WHITE   , TrunkCode)

if ISP == "": print (Style.BRIGHT+Fore.GREEN + "Org:", Style.BRIGHT+Fore.YELLOW + "Unknow" ) 
else: print(Style.BRIGHT+Fore.GREEN +"Org: " + Style.BRIGHT+Fore.WHITE + ISP)

if Line == 0: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Fixed" )
if Line == 2: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Fixed or Mobile")
if Line == 1: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Mobile")
if Line == 3: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Free")
if Line == 4: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Premium Rate")
if Line == 5: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Shared Cost")
if Line == 6: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "VOIP")
if Line == 7: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Personal Number")
if Line == 8: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Pay Line")
if Line == 9: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "UAN")
if Line == 10: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "VoiceMail")
if Line == 99: print (Style.BRIGHT+Fore.GREEN + "Line:", Style.BRIGHT+Fore.WHITE + "Unknow")


print (Style.BRIGHT+Fore.GREEN + "Timezone:" + Style.BRIGHT+Fore.WHITE , Time)

print(Style.BRIGHT+Fore.BLUE + "---------------------------------------------------------------------------------")
if Number_Validation == True: print (Style.BRIGHT+Fore.GREEN + "The number is possible:" + Style.BRIGHT+Fore.WHITE  ,"Yes")
if lineTypeVal == True: print (Style.BRIGHT+Fore.GREEN + "The number is possible for the type of line:" + Style.BRIGHT+Fore.WHITE , "Yes")
if Validation == True: print (Style.BRIGHT+Fore.GREEN + "The number can receive calls and send messages:" + Style.BRIGHT+Fore.WHITE , "Yes")
if Diall_Validation == True: print(Style.BRIGHT+Fore.GREEN + "The number can be marked internationally:" + Style.BRIGHT+Fore.WHITE , "Yes")
if Carrier_Specific == True: print (Style.BRIGHT+Fore.GREEN + "The carrier is Specific:" + Style.BRIGHT+Fore.WHITE , "Yes")


if Number_Validation == False: print (Style.BRIGHT+Fore.GREEN + "The number is possible:" + Style.BRIGHT+Fore.WHITE + " No")
if Validation == False: print (Style.BRIGHT+Fore.GREEN + "The number can receive calls and send messages:" + Style.BRIGHT+Fore.WHITE + " No")
if Diall_Validation == False: print(Style.BRIGHT+Fore.GREEN + "The number can be marked internationally:" + Style.BRIGHT+Fore.WHITE + " No")
if Carrier_Specific == False: print (Style.BRIGHT+Fore.GREEN + "The carrier is Specific:" + Style.BRIGHT+Fore.WHITE + " No")
if lineTypeVal == False: print (Style.BRIGHT+Fore.GREEN + "The number is possible for the type of line:" + Style.BRIGHT+Fore.WHITE + " No")

print(Style.BRIGHT+Fore.BLUE + "---------------------------------------------------------------------------------")

