import csv
import os


# Assign a variable for the file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Open the election_results.csv and read the file
with open(file_to_load) as election_data:

# To do: perform analysis
    print(election_data)
# Close the file
election_data.close()

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('analysis','election_analysis.txt')

# Using the with statement to open the file as a text file
with open(file_to_save, 'w') as txt_file:

# Write some data to the file
    txt_file.write('Counties in the election\n------------\nArapahoe\nDenver\nJefferson')

# close the file


#Data we need to retrieve

#1 total votes cast

#2 list of candidates who received votes

#3 percentage of votes each candidate won

#4 total votes each candidate won

#5 winner of each election