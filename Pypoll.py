
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

# Import the datetime class from the datetime module.
# import datetime
# Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# To reduce the confusion on importing a module with the same name as a class we can use an abbreviated alias dt for the datetime module.
# Import the datetime class from the datetime module.
# import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'
# #to open the file
# with open(file_to_load) as election_data:

# #To do: perform analysis.
#     print(election_data)

# #to close the file.
# election_data.close()

# os.path.join("Resources", "election_results.csv")
# file_to_load = os.path.join("Resources", "election_results.csv")

import csv
import os
#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

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
    print(headers)
    headers = next(file_reader)
    print(headers)
    

# import os
# import csv 
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file. outfile is for the first line object 
# #to keep writing on the text file add outfile
# outfile = open(file_to_save, "w")
# # Write some data to the file. \n generates new line. new line character
# outfile.write("Hello World\n")
# outfile.write("my name is sandra")

# # Close the file
# outfile.close()

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     #txt_file.write("Hello World")
#     # Write three counties to the file.
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson.")
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("---------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# txt_file.close()
