# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

"""
Author: Emely Chuy
Date: 10/18/2024
"""
#The authors that will be mentioned in the output when they have passed away
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889", }

#This will help begin a loops
for authors, date in authors.items():
    #This will print the authors' names and the year they have passed
   print("%s" % authors + " died in", date + ".")

