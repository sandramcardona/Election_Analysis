# Election_Analysis

## Project Overview
A Colorado Borad of Elections employee has given me the tasks below to complete the election audit of a recent locatl congressional election.

1. Calculate the Total number of votes cast in this congressional election.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the Percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.0, Visual Studio Code, 1.50

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper 
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Diana DeGette: 73.8% (272,892)
    - Charles Casper Stockham: 23.0% (85,213)
    - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
    - Candidate Diana DeGette, who received 272,892 of the 369,711 votes. The candidate won 73.8% of the popular votes.
Below are the results after the code ran using the scrip written:

![alt text](https://github.com/sandramcardona/Election_Analysis/blob/main/Resources/Results_Election_Analysis.png)
    
## Challenge Overview
The election commission has requested some additional data to complete the audit:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.0, Visual Studio Code, 1.50

## Challenge Summary
The analysis of the election based on county shows that:
- There were 369,711 votes cast in the election.
- The counties that were part of the election were: 
    - Denver
    - Arapahoe
    - Jefferson
- The results of votes per county were:
    - Denver: 82.8% (306,055)
    - Jefferson: 10.5% (38,855)
    - Arapahoe: 6.7% (24,801)
- The county with the largest number of votes was Denver.

Below are the results after the code ran using the scrip written to include counties:

![alt text](https://github.com/sandramcardona/Election_Analysis/blob/main/Resources/Results_Pypoll_Challenge_Election_analysis.png)

Based on the results, the script written to analyze the results for this election can be modified in several ways to use for any future election. The modificaton will be to  define a function that can be called with single commands and can be designed to accept new files and process the written script with the new data and provide the results needed for the election analysis. One of the modifications will be to create a function to find the votes by county and the other modification will be to create a second function fo find the votes for the candidates and the winning candidate. 

# Overview of Methods Used

The csv file provided with the data was opened through Python VS Code. Then the dependencies for OS and CSV were imported and the file was accessed by creating a file_to-load variable and file_to_save variable that would open and save the file. Using a "with Open" statement the election results were open by identifying the file_reader as a csv reader for the election data. Then the 2 headers were skipped so they wouldn't be counted in the total lines being reviewed. To count up all the votes,   a variable was initialized, which is called an accumulator, this will increment by 1 as each row is read in the for loop. The variable called total_votes was set to start in  zero. Then using a for loop. Then we declared a new list under the variable candidate_name to capture the candidate options in the data on the third column, then this variable was used within the "for" loop already in place to collect the names of the candidates in the third column (row[2]) and add the names to the list only if the names were new in the list. If the name already exist on the list, then the name won't be added again. Then a candidate_votes variable was created to hold an empty dictionary. Then this variable was used to add the candidate votes to this dictionary to every corresponding candidate as it encounters them in the data. A Total_votes variable was created to initialize the toatl vote counter at 0 for all the candidates then we incremented the votes by 1 everytime a candidate name appears in a row. 


