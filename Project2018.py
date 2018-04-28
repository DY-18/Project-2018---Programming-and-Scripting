###################################
## Darren Young, 2018-04-23  ######
## Iris Dataset analysis     ######
## Calculate the maximium,   ######
## minimium and mean of      ######
## each column               ######
###################################

# Import numpy library

import numpy

# read datafile into array

data=numpy.genfromtxt('Data\iris.csv',delimiter=',')

# Select all the the values in the first column, and then caluclate the mean, max and min of those values

firstcol=data[:,0]
meanfirstcol=numpy.mean(data[:,0])
maxfirstcol=numpy.max(data[:,0])
minfirstcol=numpy.min(data[:,0])

# Print to screen the mean, max and min values of the first column

print ("Average of first column:",meanfirstcol)
print ("Maximium of first column:",meanfirstcol)
print ("Minimium of first column:",meanfirstcol)

# To calulate for the second colum, repeat above but change the 0 to 1 

secondcol=data[:,1]
meansecondcol=numpy.mean(data[:,1])
maxsecondcol=numpy.max(data[:,1])
minsecondcol=numpy.min(data[:,1])

# To print calculations for the second column change text to reflect python script for secondcol

print ("Average of second column:",meansecondcol)
print ("Maximium of second column:",maxsecondcol)
print ("Minimium of second column:",minsecondcol)

#  To calulate for the third column, repeat above but change the 1 to 2

thirdcol=data[:,2]
meanthirdcol=numpy.mean(data[:,2])
maxthirdcol=numpy.max(data[:,2])
minthirdcol=numpy.min(data[:,2])

# To print calculations for the third column change text to reflect python script for thirdcol

print ("Average of third column:",meanthirdcol)
print ("Maximium of third column:",maxthirdcol)
print ("Minimium of third column:",minthirdcol)

#  To calulate for the fourth column, repeat above but change the 2 to 3

fourthcol=data[:,3]
meanfourthcol=numpy.mean(data[:,3])
maxfourthcol=numpy.max(data[:,3])
minfourthcol=numpy.min(data[:,3])

# To print calculations for the fourth column change text to reflect python script for fourthcol

print ("Average of fourth column:",meanfourthcol)
print ("Maximium of fourth column:",maxfourthcol)
print ("Minimium of fourth column:",minfourthcol)
