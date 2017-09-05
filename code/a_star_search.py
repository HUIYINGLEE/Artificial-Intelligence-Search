"""
    Enter your details below:

    Name: Huiying Li
    Student Code: u6015465
    email: u6015465@anu.edu.au
"""
import frontiers
import search_strategies



def solve(problem, heuristic):
    closed = dict()
    frontier = frontiers.PriorityQueue()

    startNode = search_strategies.SearchNode(problem.get_initial_state())
    frontier.push(startNode, 0)

    while not frontier.is_empty():
        node = frontier.pop()
        if problem.goal_test(node.state):
            return actionsList(node)

        if node.state not in closed or node.path_cost + heuristic(node.state,problem) < closed[node.state]:
            closed[node.state] = node.path_cost + heuristic(node.state,problem)
            for state, action, cost in problem.get_successors(node.state):

                    successorNode = search_strategies.SearchNode(state, action, node.path_cost + cost,
                                                                 node, node.depth + 1)
                    frontier.push(successorNode, successorNode.path_cost + heuristic(state, problem))


def actionsList(node):
    actions = []
    linkedNode = node
    while linkedNode.parent != None:
        actions.append(linkedNode.action)
        linkedNode = linkedNode.parent
    actions.reverse()
    return actions