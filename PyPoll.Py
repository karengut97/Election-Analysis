# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes for each candidate
# 4. The total number of votes each candidate won
# 5. THe winner of the election based on popular vote

# Import csv and os modules
import csv
import os

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total votes counter
total_votes = 0

# initialize the new list for candidate names
candidate_options = []

# Declare an empty dictionary to track votes by candidate
candidate_votes = {}

# Wining candidate, count and percentage tracker
winning_count = 0
winning_percentage = 0
winning_cadidate = ""

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # Check to see if candidate is already in list
        if (candidate_name not in candidate_options):
            
            # Add candidate name to candidate options list
            candidate_options.append(candidate_name)

            # Now save that candidate name in the dictionary
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes.
    vote_percentage = "{0:.1f}".format((float(votes) / float(total_votes)) *100)

    # 4. Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage}% of the vote.")     

    # Determine if the votes are greater than winning_count
    if(votes > winning_count):
        # If true, set winning votes and percentage variables 
        winning_count = votes
        winning_percentage = vote_percentage

        # And, set the winning_cadidate equal to the candidate_name
        winning_cadidate = candidate_name
    
    # To do: print out the winning cadidate, vote count & percentage to the terminal
    print(f"{candidate_name}: {vote_percentage}% ({votes:,})\n")  

winning_cadidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_cadidate}\n"
    f"Winner Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage}%\n"
    f"------------------------\n")
print(winning_cadidate_summary)



# Print the candidate vote dictionary
# print(candidate_votes)

# Print the candidate options list
# print(candidate_options)

# print the total votes
# print(total_votes)

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
