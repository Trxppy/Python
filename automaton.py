
class Automaton:
    'A custom library for constructing a modular finite automaton'
    states = []
    loops = []
    completedLoops = [];

    def testString(self, string, position = -1, redirect = False):
        'Tests string to see if it reaches final state'

        # If redirect detected, don't cache string
        if(redirect):
            self.cachedString = string;

        finalStateReached = False
        for x in string:
            position += 1
            matches = 0
            symbol = int(x)
            for state in self.states:
                # Set variables for current state
                currentState = state[0]
                acceptedInput = state[1]
                acceptedPosition = state[2]
                endState = None
                if(matches == 0):
                    # If symbol accepted by state and position in sequence is valid, mark as match
                    if(symbol in acceptedInput and acceptedPosition is position) :
                        matches += 1
                        # Check to see if state is final
                        print("\nPosition->" + str(position) + "Len->" +  str(len(string)-1))
                        if(state[3] == True and position == (len(string)-1)):
                            finalStateReached = True
                            endState = state[0]
                        print(str(symbol) + " leads to " + state[0])
            if(matches == 0):
                # Check to determine if redirect loop exists
                loopExists = False
                for loop in self.loops:
                    loopInput = loop[0]
                    loopStart = loop[1][0]
                    loopEnd = loop[1][1]

                    # Check if redirect loop start matches current position and symbol matches criteria
                    if((symbol in loopInput) and (position == (loopStart+1))):
                        loopExists = True
                if(loopExists == False):
                    print("No path found for symbol \"" + str(symbol) + "\" at position " + str(position))
                else: 
                    print("\nLoop found at position " + str(position) + " for symbol " + str(symbol) + " -> Redirects to State \""+str(self.states[loopEnd][0])+"\"")

                    if(redirect == False):
                        postString = string[position:]
                        print(postString)
                    # If redirect not set, test looping postString
                    if(redirect == False):
                        self.testString(postString, loopEnd-1, True)
                        return
        if(finalStateReached):
            print("Input " + string + " is accepted")
        else: 
            print("Input " + string + " is not accepted")
                        

                

    def computeWordsOfLength(self, k):
        'Compute the number of words of length k that this automaton accepts'


    def addState(self, previousState, acceptedInput, stateSequence, finalState=False):
        'Add a state to the automaton'
        self.states.append([previousState, acceptedInput, stateSequence, finalState])

    def addRedirect(self, acceptedInput, redirectKeys):
        'Add a redirect loop to the automaton'
        self.loops.append([acceptedInput, redirectKeys])

    def buildAutomaton(self, output):
        'Build the automaton and print the output'
        self.states.sort(key=lambda tup: tup[2])
        if(output):
            print("Automaton Constructor")
            print("Author: Matthew Grant")
            print("Copyright Study3 2019 \n")
            for key, state, sequence, finalstate in self.states:
                print("State: " + str(key))
                print("-Position in Sequence: " + str(sequence))
                print("Final State: ", str(finalstate))
                print("-Accepted Input(s): ", end = "")
                for detail in state:
                    print(detail, end="")
                print("\n")
            for loop, redirectKeys in self.loops:
                print("Automaton Loop")
                print("-Start State: " + str(redirectKeys[0]))
                print("-End State: " + str(redirectKeys[1]))
                print("-Accepted Input(s): ", end = "")
                for detail in loop:
                    print(detail, end="")
                print("\n")





dfa = Automaton()
dfa.addState("A", [0, 1], 0)
dfa.addState("B", [0], 1)
dfa.addState("C", [1], 1)
dfa.addState("D", [0, 1], 2, True)
dfa.addRedirect([0], [2, 0])
dfa.addRedirect([1], [2, 1])
dfa.buildAutomaton(True)
dfa.testString("01101")
