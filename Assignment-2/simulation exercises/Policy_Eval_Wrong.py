      # Policy Evaluation
      A = np.zeros(shape=(N,N))
      b = np.zeros(shape=(N,1))
      for i in range(N):
        #actions = taxienv.possible_actions(state)
        state = states[i]
        action = policy[state]
        pij = taxienv.ride_probabilities(state,action)
        rewards = taxienv.ride_rewards(state,action)
        coeffs = pij
        coeffs[i] = 1-coeffs[i]
        c = 0
        for j in range(N):
          c += rewards[j]*pij[j]
        A[i,:] = coeffs
        b[i] = c
      
      J = np.linalg.solve(A,b)
      Jprev = np.zeros(shape(N,1),dtype='float')-1