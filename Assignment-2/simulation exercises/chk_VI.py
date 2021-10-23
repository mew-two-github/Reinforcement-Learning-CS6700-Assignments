taxienv = TaxiEnv_HW2(**kwargs)
gamma = 0.9
states = taxienv.possible_states
# Initial values
values = {s: 0 for s in states}

# This is a dictionary of states to policies -> e.g {'A': '1', 'B': '2', 'C': '1'}
policy = taxienv.initial_policy.copy()
diff_max = 1
N = len(states)
J = np.zeros(shape=N)
count = 0
while diff_max>=1e-8:
  count +=1
  Jprev_VI = np.copy(J)
  diff_max = 0
  for i in range(N):
    state = states[i]
    action = policy[state]
    pij = np.array(taxienv.ride_probabilities(state,action))
    g = np.array(taxienv.ride_rewards(state,action))
    J[i] = sum(np.multiply(pij,g+gamma*Jprev_VI))
    diff_max = max(abs(J[i]-Jprev_VI[i]),diff_max)
# Checking
print(Jprev_VI[i])
for i in range(N):
    state = states[i]
    action = policy[state]
    pij = np.array(taxienv.ride_probabilities(state,action))
    g = np.array(taxienv.ride_rewards(state,action))
    J[i] = sum(np.multiply(pij,g+gamma*Jprev_VI))
print(J[i])
print(count)