#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # route = [None] * length
    route = []

    """
    YOUR CODE HERE
    """

    for i in range(len(tickets)):
        source = tickets[i].source
        dest = tickets[i].destination
        hash_table_insert(hashtable, source, dest)

        # if source == start:

    current = hash_table_retrieve(hashtable, "NONE")
    route.append(current)
    while current != "NONE":
        current = hash_table_retrieve(hashtable, current)
        route.append(current)

    return route
