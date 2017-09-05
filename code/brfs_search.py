"""
    Enter your details below:

    Name: Huiying Li
    Student Code: u6015465
    email: u6015465@anu.edu.au
"""

import frontiers

def solve(problem) :
    """ *** YOUR CODE HERE *** """
    #create a frontier use priority queue with the function len()
    #which means that the shorest path with be ordered in the first position of the queue
    #so when pop called, queue will pop the shorest path. For example, the path with length (or depth) 2
    #(A-C) will always be expanded before (A-B-D). The agent won't expand the node on level 3 until all nodes
    #on level 2 are explored.
    #             A
    #          B     C
    #        D   E  F  G
    frontier = frontiers.PriorityQueueWithFunction(len)
    explored = []
    #                     initial state      initial action    inital cost
    frontier.push([(problem.get_initial_state(), None,            0)])

    while not frontier.is_empty():
        path = frontier.pop()
        currentState = path[-1][0]

        if problem.goal_test(currentState):
            #return all the actions except from the initial one, which is None
            return [x[1] for x in path[1:]]
        if currentState not in explored:
            explored.append(currentState)
            for successor in problem.get_successors(currentState):
                #Copy the path and append the successor to it
                successorPath = path[:]
                successorPath.append(successor)
                frontier.push(successorPath)

