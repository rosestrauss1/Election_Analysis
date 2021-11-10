print("Hello World")

'using if statements'
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

'using if else statements'
counties = ["Arapahoe","Denver","Jefferson"]
if counties[2] == 'Arapahoe':
    print (counties[1])
else:
    print (counties[2])

'memberhsip operators practice'
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

'combine membership and logical operations I(and could also be or)'
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

'For Loop to Iterate Through Lists and Tuples'
for county in counties:
    print(county)

'you can use a range to execute the same output, but you must know the number of values in the list'
for i in range(len(counties)):
    print(counties[i])
    'in this code, i indicates the index (number of values, so 0,1,2) and then inside the range'
    'is the length of the list of counties (which = 3). We use i =0 the output is Arapahoe and it continues to'
    'iterate through 1,2'

'Iterate Through a Dictionary'
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

'get keys from dictionary using for loop'
for county in counties_dict:
    print(county)

'using the key method to get keys from the dictionary'
for county in counties_dict.keys():
    print(county)

'get the values of the dictionary'
for voters in counties_dict.values():
    print(voters)

'Get the Key-Value Pairs of a Dictionary in For Loop'
for county, voters in counties_dict.items():
    print(county, voters)
'key is first variable, value is second in dictionaries'

'Print each dictionary using a for loop'
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

'use the range function to iterate over the list of dictionaries and print the counties in voting_data'
for i in range(len(voting_data)):

      print(voting_data[i])

'nested for loop to print both dictionary variable and value'
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

'nested for loop to print only values'
for county_dict in voting_data:
     print(county_dict['registered_voters'])

'nested for loop to print only variables'
for county_dict in voting_data:
    print(county_dict['county'])