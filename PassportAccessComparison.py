#Comparing which countries can be access between different passports
#Add edit distance and random selection features
#import json
import ssl
import csv #https://www.programiz.com/python-programming/csv#:~:text=To%20write%20to%20a%20CSV,data%20into%20a%20delimited%20string.


# Function is no longer useful, only USA data was available in JSON format

#A function to return a list of visa free countries for JSON Data files from this website
#https://worldpopulationreview.com/country-rankings/us-passport-visa-free-countries
# def NoVisaList(JSONFileName):
#     #Opening the URL, then reading it into a handle
#     Countryfilehandle = open(JSONFileName)
#     #using the load JSON method. This returns a dictionary that is stored in info
#     Countrydata = json.load(Countryfilehandle)
#     #print('User count:', len(Countrydata))
# #{'country': 'Afghanistan', 'visaReqs': 'Required', 'travelAdvisory': 'Level 4: Don't'}
# #In USA data we have a list. Each list element has a dictionary with 3 tuples seen above
#     Countryvisafreelist = []
#     for i in range(len(Countrydata)):
#         if Countrydata[i]['visaReqs'] == 'Not Required': #Find only the countries no visa Required
#             Countryvisafreelist.append(Countrydata[i]['country'])
#     return Countryvisafreelist
#USAvisafreelist = NoVisaList('USAPassportData.json')
#print(USAvisafreelist)


#CSV Passport data. JSON data only available for USA, new function must be written
#https://github.com/ilyankou/passport-index-dataset#readme

i = 0
referenceRow = [] #Creating a list of all the countries using the first row
with open(r"C:\Users\wisam\OneDrive\Documents\Python\Personal\passport-index-matrix.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if i == 0: referenceRow = row #The first row of the csv file, contains all countries
        break

#A function to get the CSV row data for a specific country
def FindingCountryRow(Country):
    with open(r"C:\Users\wisam\OneDrive\Documents\Python\Personal\passport-index-matrix.csv") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == Country:
                countryRow = row
                #print('Got it!!')
                break
        return countryRow
#A function to return a list of visa free/visa on arrival countries for a specific country
#This is where the real logic is happening
def FindingVisaFree(countryRow):
    Countryvisafreelist = []
    i = 0
    for listelement in countryRow:
        if listelement == 'visa on arrival' or listelement == "visa free":
            Countryvisafreelist.append(referenceRow[i])
        try:
            int(listelement)
            Countryvisafreelist.append(referenceRow[i]) #Comment this out for VOA or vise-free only
            i +=1
        except:
            i += 1
            continue
    return Countryvisafreelist

#A function that compares accessible countries between two passports, and returns a list
#of countries the first passport will get you into and the second will not
def CountryComparison(visafreelist1, visafreelist2):
    countriesUnlocked = []
    for listelement in visafreelist1:
        if listelement in visafreelist2: continue
        else: countriesUnlocked.append(listelement)
    return countriesUnlocked

def GettingAndVerifyingCountry():
    #GettingAndVerifyingCountry.counter += 1
    i = 1
    while True:
        userCountry = input("Please enter a country: ")
        if userCountry in referenceRow:
            break
        else:
            print("Error, the country you entered is not in our list. Please try again:")
            i+=1
            if i%3 == 0:
                print("Here is a list of the countries you can select from. Please pay attention to spelling")
                print(*referenceRow[1:], sep = ", ")
            continue
    return userCountry
#GettingAndVerifyingCountry.counter = 0

print("The first country's passport will unlock new countries compared to the second country's passport")

country1 = GettingAndVerifyingCountry()
country1Row = FindingCountryRow(country1)
country1VisaFree = FindingVisaFree(country1Row)

country2 = GettingAndVerifyingCountry()
country2Row = FindingCountryRow(country2)
country2VisaFree = FindingVisaFree(country2Row)

unlockedWithCountry1 = CountryComparison(country1VisaFree, country2VisaFree)
print("A {} passport will get you into these countries, and a {} passport will not:".format(country1, country2))
print(*unlockedWithCountry1, sep = "\n")


#CTRL+/ for block comments
