"""Quiz3
This quiz is a simplified version of 2016 presidential election. Write a definition for a class named Candidate with the following methods:

1, An __init__ method that initializes name, winning_states and number of votes.
2, A __str__ method that returns a string representation of this candidate, including name and winning state(s).
3, A method named win_state that takes a string of state abbreviation, adds it to winning_states and update votes.
4, A special method that overloads the operator '>' to compare votes of two candidates.

DO NOT change code in main method!

Upload file to Blackboard.

--------------------------------------------------------------
The expected outputs should be like below:

Donald Trump wins 
Hillary Clinton wins CA 

After election:
Donald Trump wins FL TX 
Hillary Clinton wins CA MA 
Does Trump win?
True

"""
ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.

        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.votes = votes
        self.name = name
        self.winning_states = []
        if winning_states is not None: 
            for state in winning_states: 
                self.win_state(state)
        


    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        s = ''
        for state in self.winning_states:
            s += state + ' '

        return self.name + ' wins ' + s

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.

        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes += ELECTORS.get(state)

    def __gt__(self, other):
            return self.votes > other.votes 

def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'])
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()