'''
Created on Mar 2, 2013

@author: Sanjeev Srivatsa
'''
import sys
try:
    f = open(sys.argv[1])
except IOError:
    print "Invalid file name specified"

epm = int(f.readline()) # energy per mile

jetstreams = []
endpoints = []

# parse input
for line in f:
    data = line.split(' ')
    stream = (int(data[0]), int(data[1]), int(data[2])) # streams in the form (start, end, energy)
    jetstreams.append(stream)
    endpoints.append(stream[1])
    if(stream[0] != 0):
        endpoints.append(stream[0])

# sort the jetstreams by their start point and sort the points
jetstreams.sort(key = lambda x: x[0])
endpoints.sort()

# dictionary for the energy up to a certain point and the path to a certain point
energy = { }
paths = { }
start = 0
energy[0] = 0
paths[0] = []

# find the optimum path up to every endpoint
for end in endpoints:
    energy[end] = (end - start)*epm + energy[start] # energy to go without using any jetstreams
    paths[end] = paths[start]
    for jetstream in jetstreams:
        if jetstream[0] <= end:
            if jetstream[1] == end:
                e = jetstream[2] # energy to ride that jetstream
                e += energy[jetstream[0]] # energy it takes to get to that jetstream
                if jetstream[0] > start:
                    e += (jetstream[0] - start)*epm # add energy it takes to get to the jetstream if theres a gap
                if e < energy[end]:
                    energy[end] = e
                    # take the previous path until this point and then add the new jetstream
                    stream = jetstream
                    new_path = []
                    for k in xrange(len(paths[jetstream[0]])):
                        new_path.append(paths[jetstream[0]][k])
                    new_path.append((stream[0], stream[1])) #remove energy component only want the path
                    paths[end] = new_path
                    jetstreams.remove(jetstream) #remove the jetstream since it cannot be taken anymore
                else:
                    break
    start = end

# Print the total energy expended and the jetstreams taken
print energy[endpoints[-1]]
print paths[endpoints[-1]]
