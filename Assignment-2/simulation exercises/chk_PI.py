taxienv = TaxiEnv_HW2(**kwargs)
gamma = 0.9
states = taxienv.possible_states
# Initial values
values = {s: 0 for s in states}

# This is a dictionary of states to policies -> e.g {'A': '1', 'B': '2', 'C': '1'}
policy = taxienv.initial_policy.copy()
diff_max = 1
N = len(states)
done = 0
J = np.zeros(shape=N)
count = 0
while not done:
# Policy evaluation
  count +=1
  diff_max = 1
  J = np.zeros(shape=N)
  while diff_max>=1e-8:
    Jprev_VI = np.copy(J)
    diff_max = 0
    for i in range(N):
      state = states[i]
      action = policy[state]
      pij = np.array(taxienv.ride_probabilities(state,action))
      g = np.array(taxienv.ride_rewards(state,action))
      J[i] = sum(np.multiply(pij,g+gamma*Jprev_VI))
      diff_max = max(abs(J[i]-Jprev_VI[i]),diff_max)

  done = 1

  # Policy Update
  
  for i in range(N):
  # Initialise state value and available actions
    state = states[i]
    actions = taxienv.possible_actions(state)

    # Set best action and value as current action and values
    max_val = J[i]
    best_action = policy[state]

    for action in actions:
      pij = np.array(taxienv.ride_probabilities(state,action))
      g = np.array(taxienv.ride_rewards(state,action))
      a_value = sum(np.multiply(pij,g+gamma*J))
      if max_val < a_value:
        max_val = a_value
        best_action = action
    if policy[state] != best_action:
      done = 0
    policy[state] = best_action
  print(policy)
print(count)