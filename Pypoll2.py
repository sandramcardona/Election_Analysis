# #assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'
# #to open the file
# election_data = open(file_to_load, 'r')

# with open(file_to_load) as election_data:

# #To do: perform analysis.
#     print(election_data)
#     #print(election_data.readlines())
# #to close the file.
# election_data.close()

# import os

# #Create a filename variable to a direct or indirect path to the file
# file_to_save = os.path.join("Analysis","election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
# Import the datetime class from the datetime module.
# import datetime
# Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# # To reduce the confusion on importing a module with the same name as a class we can use an abbreviated alias dt for the datetime module.
# # Import the datetime class from the datetime module.
# # import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# # assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'
# # #to open the file
# with open(file_to_load) as election_data:

# # #To do: perform analysis.
#     print(election_data)

# # #to close the file.
# # election_data.close()

# os.path.join("Resources", "election_results.csv")
# file_to_load = os.path.join("Resources", "election_results.csv")

import os
import csv 
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file. outfile is for the first line object 
#to keep writing on the text file add outfile
outfile = open(file_to_save, "w")
# Write some data to the file. \n generates new line. new line character
outfile.write("Hello World\n")
outfile.write("my name is sandra")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")
    # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson.")
    txt_file.write("Counties in the Election\n")
    txt_file.write("---------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

txt_file.close()


#Pseudocode
# In this project, our final Python script will need to be able to deliver the following information when the script is run: 
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote



# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.
# 6. Get the percentage of votes each candidate won
# 7. List/print the percentage values 
# 8. Determine and print the winner of the election based on popular vote

#Add our dependencies
import csv
import os
#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# variable to Initialize a total vote counter
total_votes = 0
# Candidate Options as a list therefore brakets are needed
candidate_options = []
#Variable for Empty dictionary for candidates and votes
candidate_votes = {}
# Declaring variables for Winning Candidate and Winning Count tracker variables 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To Do: read and analyze the data here
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file
    #for row in file_reader:
    #print the file object
        #print(row)
    #Read and print the header row.
    headers = next(file_reader)
    headers = next(file_reader)
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # 3. Print the candidate name from each row.
        candidate_name = row[2]
        #If the candidate does not match any existing candidate then add if it does then skip
        if candidate_name not in candidate_options:
            # 4. Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count starting with each candidate's vote count to zero. Once is set to zero we can start tallying the votes for each candidate.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count everytime the name appears by incrementing by 1
        candidate_votes[candidate_name] += 1
#Determine the percentage of votes for each candidate by looping throught the counts.
# first, iterate through the candidate list.
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes) * 100
    #4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
    # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)
