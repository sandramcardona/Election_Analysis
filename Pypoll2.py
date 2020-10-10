#assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
#to open the file
election_data = open(file_to_load, 'r')

with open(file_to_load) as election_data:

#To do: perform analysis.
    print(election_data)
    #print(election_data.readlines())
# # #to close the file.
# # election_data.close()
# import os

# #Create a filename variable to a direct or indirect path to the file
# file_to_save = os.path.join("Analysis","election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")


