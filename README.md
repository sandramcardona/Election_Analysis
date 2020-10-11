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



