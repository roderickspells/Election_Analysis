# #
# print("Hello World")

counties = ["Arapahoe" , "Denver" , "jefferson", "El Paso"]
# print(counties)
# print(counties[2])
#counties.append("el paso")

# print(counties)

# counties_dict = {}
#  counties_dict["Arapahoe"] = 422829
#  counties_dict["Denver"] = 463353
#  counties_dict["Jefferson"] = 432438

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# #
# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.") 
# #

# #counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#    print(counties[1])

#    temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#    print("Turn on the AC.")
# else:
#     print("Open the windows.")


# #what is the score?
# score =int(input("What is your test score? "))
# #Determine the grade
# if score >= 90:
#     print('Your grade is an A')
# else:
#         if score >= 80:
#             print('Your grade is an B')
#         else:
#                 if score >= 70:
#                     print('Your grade is an C')
#                 else:
#                         if score >= 60:
#                             print('Your grade is an D')
#                         else:
#                             print('Your grade is an F')

# # What is the score?
# secondScore = int(input("What is your test secondScore? "))
# # Determine the grade.
# if secondScore >= 90:
#     print('Your grade is an A.')
# elif secondScore >= 80:
#     print('Your grade is a B.')
# elif secondScore >= 70:
#     print('Your grade is a C.')
# elif secondScore >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# if "Arapahoe" in counties and "El Paso" in counties:
#         print("Araohoe and El Paso are in the list of counties")
# else:
#         print('Arapahoe or El Paso is not in the list of counties')

# if "Arapahoe" in counties or "El Paso" in counties:
#         print("Arapahoe or El Paso is in the list of counties.")
# else:
#          print("Arapahoe and El Paso are not in the list of counties.")
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# for county in counties:
#     print(county)

numbers = [0, 1 , 2 , 3, 4]
# for num in numbers:
#     print(num)
# for num in range(3):
#      print(num)

# for i in range(len(counties)):
#     print(counties[i])

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))


# #skill drill
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")


#items key-value pair

# for county, voters in counties_dict.items():
#     print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#      print(county_dict['registered_voters'])


# for county_dict in voting_data:
#      print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county in voting_data:
    print(f"{county} county has {voters} registerd voters.")