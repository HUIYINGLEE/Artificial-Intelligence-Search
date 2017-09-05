
from agents import Agent
import util
from actions import Directions

from search_problems import AdversarialSearchProblem

class MinimaxAgent(Agent):
    """ The agent you will implement to compete with the black bird to try and
        save as many yellow birds as possible. """

    def __init__(self, max_player, depth="2"):
        """ Make a new Adversarial agent with the optional depth argument.
            (MinimaxAgent, str) -> None
        """
        self.max_player = max_player
        self.depth = int(depth)

    def evaluation(self, problem, state):
        """
            (MinimaxAgent, AdversarialSearchProblem,
                (int, (int, int), (int, int), ((int, int)), number, number))
                    -> number
        """
        player, red_pos, black_pos, yellow_birds, score, yb_score = state
        playerAnticipate = 0
        opponentAnticipate = 0
        for yel_pos in yellow_birds:
            if problem.maze_distance(red_pos,yel_pos)<= problem.maze_distance(black_pos, yel_pos):
                playerAnticipate+=1
            else: opponentAnticipate+=1
        return score+(playerAnticipate-opponentAnticipate)*yb_score


    def maximize(self, problem, state, current_depth):
        """
            This method should return a pair (max_utility, max_action).

             (MinimaxAgent, AdversarialSearchProblem,
                 (int, (int, int), (int, int), ((int, int)), number, number)
                     -> (number, str)
        """

        "*** YOUR CODE GOES HERE ***"
        if current_depth == self.depth:
            if not problem.terminal_test(state):
                return (self.evaluation(problem,state),Directions.STOP)
            else:
                return (problem.utility(state),Directions.STOP)
        else:
            # nextMove = [(self.minimize(problem, nextState, current_depth + 1), action) for nextState, action, _ in
            #             problem.get_successors(state)]
            # return max(nextMove)
            return max([(self.minimize(problem, nextState, current_depth + 1), action) for nextState, action, _ in problem.get_successors(state)])


    def minimize(self, problem, state, current_depth):
        """
            This function should just return the minimum utility.

            (MinimaxAgent, AdversarialSearchProblem,
                 (int, (int, int), (int, int), ((int, int)), number, number)
                     -> number
        """

        "*** YOUR CODE GOES HERE ***"

        if current_depth == self.depth:
            return problem.utility(state)
        else:
            nextMove = [self.maximize(problem, nextState, current_depth + 1) for nextState, _, _ in
                        problem.get_successors(state)]
            return min(nextMove)[0]
            # return min([self.maximize(problem, nextState, current_depth + 1) for nextState, _, _ in problem.get_successors(state)])


    def get_action(self, game_state):
        """ This method is called by the system to solicit an action from
            MinimaxAgent. It is passed in a State object.

            Like with all of the other search problems, we have abstracted
            away the details of the game state by producing a SearchProblem.
            You will use the states of this AdversarialSearchProblem to
            implement your minimax procedure. The details you need to know
            are explained at the top of this file.
        """
        #We tell the search problem what the current state is and which player
        #is the maximizing player (i.e. who's turn it is now).
        problem = AdversarialSearchProblem(game_state, self.max_player)
        state = problem.get_initial_state()
        utility, max_action = self.maximize(problem, state, 0)
        print("At Root: Utility:", utility, "Action:", max_action, "Expanded:", problem._expanded)
        return max_action
