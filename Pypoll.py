
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
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping throught the counts.
    # first, iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (
        #4. Print the candidate name and percentage of votes.
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #save the candidate results to our text file.
        print(candidate_results)
        txt_file.write(candidate_results)
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
    # Print the candidate summary
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)    

