"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one. All flights
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should
return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also
a valid itinerary. However, the first one is lexicographically smaller.
"""

def fn(flights, visited, start, res, curr_count, total_count):
    res += [start]
    if curr_count == total_count:
        return True
    for next in sorted(flights[start]):
        if not visited[(start, next)]:
            visited[(start, next)] = True
            return fn(flights, visited, next, res, curr_count+1, total_count)

    return False


import collections
if __name__ == '__main__':
    # flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    # start = 'YUL'
    # flights = [ ('A', 'C'),('A', 'B'), ('B', 'C'), ('C', 'A')]
    # start = 'A'
    flights = [('SFO', 'COM'), ('COM', 'YYZ')]
    start = 'COM'
    dic = collections.defaultdict(list)
    visited = {}
    for f in flights:
        dic[f[0]].append(f[1])
        visited[f] = False

    res = []
    poss = fn(dic, visited, start, res, 0, len(flights))
    if not poss:
        print(None)
    else:
        print(res)