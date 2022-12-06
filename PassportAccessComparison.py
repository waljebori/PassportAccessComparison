#Comparing which countries can be access between different passports
#Features to add:
#1. Add edit distance to enhance user experience
#2. Add random selection features as an option so users don't have to select a specific country


import ssl
import csv
#CSV Passport data.
#https://github.com/ilyankou/passport-index-dataset#readme

i = 0
referenceRow = [] #Creating a list of all the countries using the first row
with open(r"passport-index-matrix.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if i == 0: referenceRow = row #The first row of the csv file, contains all countries
        break

#A function to get the CSV row data for a specific country
def FindingCountryRow(Country):
    with open(r"passport-index-matrix.csv") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == Country:
                countryRow = row
                #print('Got it!!')
                break
        return countryRow
#A function to return a list of visa free/visa on arrival countries for a specific country
def FindingVisaFree(countryRow):
    Countryvisafreelist = []
    i = 0
    for listelement in countryRow:
        if listelement == 'visa on arrival' or listelement == "visa free":
            Countryvisafreelist.append(referenceRow[i])
        try:
            int(listelement) #A number represents the length of the visa granted, if a number is there
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
