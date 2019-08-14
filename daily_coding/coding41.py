from typing import Dict, Set
from heapq import heappush, heappop

# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
# and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. 
# If there are multiple possible itineraries, return the lexicographically smallest one. 
# All flights must be used in the itinerary.

def get_itinerary(flights, start):
    g = {}  # type: Dict[str, List]

    for s, t in flights:                # O(n)
        if s not in g:
            g[s] = []
        heappush(g[s], t)               # O(logn)

    curr = start
    itinerary = []

    while curr:                         # O(n)
        itinerary.append(curr)    
        if curr in g and g[curr]:
            curr = heappop(g[curr])     # Update current destination
        else:                           # No flights going out from here
            curr = None

    for s in g:                         # O(n)
        if g[s]:
            return None

    return itinerary

print(get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(get_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
print(get_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))