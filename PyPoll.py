# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a avariable to save the file to a path
file_to_save = os.path.join("analysis" , "election_analysis.txt")

#Open the election data results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)


#using the open() funstion with the "w" mode we will write data to the file
with open(file_to_save,"w") as txt_file:

    #Write three counties to the file
    
    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")



# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.