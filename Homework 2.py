# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:10:00 2020

@author: kayla
"""

# %%

# Initial version - "standard programming"
#
# Define a list for the data.  Will be a list of lists.
data = []
# open the file
fname = "data/14_Foreign_Exchange_Rates_PureNumeric.csv"
f = open(fname, "r")
# ignore the first 5 lines
for i in range(6):
    line = f.readline()
# loop until we run out of lines
while (line):
    # strip the newline and tokenize (split on commas, in this case)
    tokens = line.rstrip().split(',')
    # append this record to the dataset
    data.append([(tokens[0]), tokens[1], (tokens[3]), (tokens[14])])
    tokens[0]=int(tokens[0])
    tokens[1]=str(tokens[1])
    tokens[3]=float(tokens[3])
    tokens[14]=float(tokens[14])
    # read the next line
    line = f.readline()
# close the file
f.close()
# show the data
#ShowData(data)

# %%


str.format(int(tokens[0]). srt(tokens[1]),)
print()
