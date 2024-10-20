
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"]*trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    return V

class HMM:
    def __init__(self, states, start_prob, transition_prob, emission_prob):
        self.states = states
        self.start_prob = start_prob
        self.transition_prob = transition_prob
        self.emission_prob = emission_prob

def viterbi_algorithm(hmm, obs):
    # Step 1: Initialize Variables
    viterbi_table = [[0.0 for _ in range(len(hmm.states))] for _ in range(len(obs))]
    backpointer = [[0 for _ in range(len(hmm.states))] for _ in range(len(obs))]

    # Step 2: Calculate Probabilities
    for t in range(len(obs)):
        for s in range(len(hmm.states)):
            if t == 0:
                viterbi_table[t][s] = hmm.start_prob[hmm.states[s]] * hmm.emission_prob[hmm.states[s]].get(obs[t], 0.0001)
            else:
                max_prob = max(viterbi_table[t-1][prev_s] * hmm.transition_prob[hmm.states[prev_s]][hmm.states[s]] for prev_s in range(len(hmm.states)))
                viterbi_table[t][s] = max_prob * hmm.emission_prob[hmm.states[s]].get(obs[t], 0.0001)
                backpointer[t][s] = max(range(len(hmm.states)), key=lambda prev_s: viterbi_table[t-1][prev_s] * hmm.transition_prob[hmm.states[prev_s]][hmm.states[s]])

    # Step 3: Traceback and Find Best Path
    best_path_prob = max(viterbi_table[-1])
    best_path_pointer = max(range(len(hmm.states)), key=lambda s: viterbi_table[-1][s])
    best_path = [best_path_pointer]
    for t in range(len(obs)-1, 0, -1):
        best_path.insert(0, backpointer[t][best_path[0]])

    # Convert index-based path back to state names
    best_state_sequence = [hmm.states[index] for index in best_path]
   # Step 4: Return The Best Path
    return best_state_sequence

# Observations and HMM data
observations = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
states = ['Noun', 'Verb', 'Adjective', 'Determiner', 'Preposition']

start_probability = {
    'Noun': 0.3,
    'Verb': 0.1,
    'Adjective': 0.05,
    'Determiner': 0.5,
    'Preposition': 0.05
}

transition_probability = {
    'Noun': {'Noun': 0.1, 'Verb': 0.3, 'Adjective': 0.1, 'Determiner': 0.1, 'Preposition': 0.4},
    'Verb': {'Noun': 0.4, 'Verb': 0.1, 'Adjective': 0.1, 'Determiner': 0.1, 'Preposition': 0.3},
    'Adjective': {'Noun': 0.5, 'Verb': 0.1, 'Adjective': 0.1, 'Determiner': 0.1, 'Preposition': 0.2},
    'Determiner': {'Noun': 0.4, 'Verb': 0.1, 'Adjective': 0.4, 'Determiner': 0.05, 'Preposition': 0.05},
    'Preposition': {'Noun': 0.3, 'Verb': 0.1, 'Adjective': 0.2, 'Determiner': 0.3, 'Preposition': 0.1}
}

emission_probability = {
    'Noun': {
        'The': 0.01, 'quick': 0.01, 'brown': 0.01, 'fox': 0.3,
        'jumps': 0.05, 'over': 0.01, 'the': 0.01, 'lazy': 0.01, 'dog': 0.3
    },
    'Verb': {
        'The': 0.01, 'quick': 0.01, 'brown': 0.01, 'fox': 0.05,
        'jumps': 0.6, 'over': 0.1, 'the': 0.01, 'lazy': 0.01, 'dog': 0.05
    },
    'Adjective': {
        'The': 0.01, 'quick': 0.4, 'brown': 0.4, 'fox': 0.01,
        'jumps': 0.01, 'over': 0.01, 'the': 0.01, 'lazy': 0.4, 'dog': 0.01
    },
    'Determiner': {
        'The': 0.5, 'quick': 0.01, 'brown': 0.01, 'fox': 0.01,
        'jumps': 0.01, 'over': 0.01, 'the': 0.5, 'lazy': 0.01, 'dog': 0.01
    },
    'Preposition': {
        'The': 0.01, 'quick': 0.01, 'brown': 0.01, 'fox': 0.01,
        'jumps': 0.01, 'over': 0.8, 'the': 0.01, 'lazy': 0.01, 'dog': 0.01
    }
}

# Create an HMM object
hmm = HMM(states, start_probability, transition_probability, emission_probability)

# Use viterbi_algorithm to find the best POS tag sequence
result = viterbi_algorithm(hmm, observations)
print("Most probable POS tags sequence:")
print(observations,"\n")
print(result)
