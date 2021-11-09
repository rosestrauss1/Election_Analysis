# Add our dependencies.
import csv
import os
#The Data we need to retrieve
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

 # Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

 # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

       # Write three counties to the file.
            txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()


#1. The total number of votes cast
#2. A complete list of the candidates who recieved votes
#3. The percentage of votes that each candidate won
#4. The total number of votes that each candidate won
#5. The winner of each election based on popular vote