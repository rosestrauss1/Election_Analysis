# Election Analysis

## Overview of Project

### Purpose

The purpose of this project is to use python to determine the outcomes of a congressional election. Using for loops and if then statements and data from a csv file indicating name of candidates, county, and votes, I calculated the win number for the election, number of votes per county, and locations where turnout was the highest among voters.

## Election-Audit Results

* How many votes were cast in this congressional election?

The total number of votes that were cast was 369,711.
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

In the three counties in the district, Jefferson county accounted for 38,855 votes, which was 10.5% of the total voter turnout. Denver accounted for 306,055 votes, which was 82.8% of total votes. Finally, Arapahoe accounted for 6.7% of voter turnout and 24,801 voters. 

* Which county had the largest number of votes?

Denver was the county with the largest number of votes. 

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

The total number of votes Charles Casper Stockham recieved was 85,213, which was 23% of the voter turnout. Diane DeGette recieved 73.8% of the vote, with 272,892 voters. Raymon Anthony Doane got the smallest amount of votes, 11,606, which was 3.1% of the total turnout. 

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Diane DeGette won the election with 73.8% of the vote and 272,892 voters.

## Election-Audit Summary

The script used in this election analysis could be used for any election with some modifications. The first step the election commission would need to take is to create a csv file that could be utilized by the script. Once there is a csv file inputed, all the election commission would need to do is change the file path to draw from the csv file for the relevant election. After this is complete, depending on the type of election, whether it be state, local or federal, the election commission can analyze the results using this script. For example, in a local election, voter turnout can be calculated for smaller geographic locations than counties in specific precincts, which would give the commission more precise data on voter turnout. An additional for loop would have to be created for precincts, exactly like it was done for counties. An additional modification that could be made for a federal presidential election is if the election commission wanted to find what party voters were associated with. The election commission could add an additional column to the csv file with the header 'Political Party' and track which precincts voted primarily for which party, and which party had the largest turnout. The election commission could do this by adding an additional for loop.


