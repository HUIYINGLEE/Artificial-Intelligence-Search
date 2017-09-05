# heuristics.py
# ----------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

""" This class contains heuristics which are used for the search procedures that
    you write in search_strategies.py.

    The first part of the file contains heuristics to be used with the algorithms
    that you will write in search_strategies.py.

    In the second part you will write a heuristic for Q4 to be used with a
    MultiplePositionSearchProblem.
"""

#-------------------------------------------------------------------------------
# A set of heuristics which are used with a PositionSearchProblem
# You do not need to modify any of these.
#-------------------------------------------------------------------------------

def null_heuristic(pos, problem):
    """ The null heuristic. It is fast but uninformative. It always returns 0.
        (State, SearchProblem) -> int
    """
    return 0

def manhattan_heuristic(pos, problem):
  """ The Manhattan distance heuristic for a PositionSearchProblem.
      ((int, int), PositionSearchProblem) -> int
  """
  return abs(pos[0] - problem.goal_pos[0]) + abs(pos[1] - problem.goal_pos[1])

def euclidean_heuristic(pos, problem):
    """ The Euclidean distance heuristic for a PositionSearchProblem
        ((int, int), PositionSearchProblem) -> float
    """
    return ((pos[0] - problem.goal_pos[0]) ** 2 + (pos[1] - problem.goal_pos[1]) ** 2) ** 0.5

#Abbreviations
null = null_heuristic
manhattan = manhattan_heuristic
euclidean = euclidean_heuristic

#-------------------------------------------------------------------------------
# You have to implement the following heuristics for Q4 of the assignment.
# It is used with a MultiplePositionSearchProblem
#-------------------------------------------------------------------------------

#You can make helper functions here, if you need them

def bird_counting_heuristic(state, problem) :
    position, yellow_birds = state

    """ *** YOUR CODE HERE *** """
    heuristic_value = len(yellow_birds)
    return heuristic_value

bch = bird_counting_heuristic


# def every_bird_heuristic(state, problem):
#     """
#         (((int, int), ((int, int))), MultiplePositionSearchProblem) -> number
#     """
#     position, yellow_birds = state
#     """ *** YOUR CODE HERE *** """
#     distanceList = []
#
#     for bird in yellow_birds:
#         distanceList.append(problem.maze_distance(position, bird))
#
#     if distanceList:
#         return max(distanceList)
#     return 0

def every_bird_heuristic(state, problem):

    position, yellow_birds = state
    distanceList = []
    for bird in yellow_birds:
        distanceList.append(problem.maze_distance(position, bird))
    # sort the position of yellow birds according to its distance from the player
    # the idea of sorting yellow birds is comes from u5998517 SIHAN HE
    yellow_birds = [v for (k, v) in sorted(zip(distanceList,yellow_birds))]


    h=0
    for bird in yellow_birds:
        h+= problem.maze_distance(position,bird)
        position=bird
    if h >0:
        # hmmmmmmmm don't know why it expands less nodes when 0.8/0.2 applied....LOL
        # just have a try and then it performs better than returning only h
        return h*0.8+max(distanceList)*(len(distanceList))*0.2
        # return h+max(distanceList)
    else: return h




every_bird = every_bird_heuristic

