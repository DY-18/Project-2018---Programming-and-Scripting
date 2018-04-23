# Darren Young, 2018-04-23
# Iris Dataset analysis
# Calculate the maximium, minimium and mean of each column

import numpy

# read datafile into array

data=numpy.genfromtxt('Data\iris.csv',delimiter=',')

firstcol=data[:,0]
meanfirstcol=numpy.mean(data[:,0])
maxfirstcol=numpy.max(data[:,0])
minfirstcol=numpy.min(data[:,0])

print ("Average of first column:",meanfirstcol)
print ("Maximium of first column:",meanfirstcol)
print ("Minimium of first column:",meanfirstcol)

secondcol=data[:,1]
meansecondcol=numpy.mean(data[:,1])
maxsecondcol=numpy.max(data[:,1])
minsecondcol=numpy.min(data[:,1])

print ("Average of second column:",meansecondcol)
print ("Maximium of second column:",maxsecondcol)
print ("Minimium of second column:",minsecondcol)

thirdcol=data[:,2]
meanthirdcol=numpy.mean(data[:,2])
maxthirdcol=numpy.max(data[:,2])
minthirdcol=numpy.min(data[:,2])

meanthirdcol=numpy.mean(data[:,2])
print ("Average of third column:",meanthirdcol)
print ("Maximium of third column:",maxthirdcol)
print ("Minimium of third column:",minthirdcol)

fourthcol=data[:,3]
meanfourthcol=numpy.mean(data[:,3])
maxfourthcol=numpy.max(data[:,3])
minfourthcol=numpy.min(data[:,3])

print ("Average of fourth column:",meanfourthcol)
print ("Maximium of fourth column:",maxfourthcol)
print ("Minimium of fourth column:",minfourthcol)

import matplotlib.pyplot as pl

pl.hist(firstcol)
pl.show()