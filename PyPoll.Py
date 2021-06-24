# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes for each candidate
# 4. The total number of votes each candidate won
# 5. THe winner of the election based on popular vote

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Import csv and os modules
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)



# Using the open() function with the "w" mode we will write data to the file
#open(file_to_save, "w")

# Using the with statement opent he file as a text file
#outfile = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
    

# Write some data to the file
#outfile.write("Hello World")

# Close the file
#outfile.close()
