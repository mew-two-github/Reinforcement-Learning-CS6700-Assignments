def policy_iteration(env, gamma=0.99):
    '''
    Code a policy iteration algorithms here, the function should return a np 
    array of dimensions (10, 10, 2^(no. of sub-goals)) as the value gird and
    the final policy grid corresponding to the final values.
    '''

    # extracting no. of subgoals
    n = len(env.subgoal_reward)
    n2 = 2**n

    # Initial Values
    values = np.zeros((10, 10, n2))

    # Initial policy
    policy = np.empty((10, 10, n2), object)
    policy[:] = 'N' # Make all the policy values as 'N'


    #### Begin your code below this line
    n = len(env.subgoal_location)
    actions = env.actions.keys()
    done = 0
    picount = 0
    while not done:
      picount += 1
      Jold = values.copy()
      values = np.zeros((10, 10, n2))
      # Policy evaluation
      diff_max = 1
      count = 0
      while diff_max >= 1e-2:
        # if count%10 == 0:
        #   print("Iteration ",count,"diff_max",diff_max)
        count += 1
        diff_max = 0
        for i in range(env.grid_size[0]):
          for j in range(env.grid_size[1]):
            for sg in range(n2):
              jold = values[i,j,sg].copy()
              currentstate = [(i,j),num2binv(sg,n)]
              action = policy[i,j,sg]
              jnew = -1e9
              lst = env.get_transition_probabilites_and_reward(currentstate, action)
              sums = 0
              for tup in lst:
                nextstate = tup[0]
                [coords_tuple,sgidx] = nextstate
                ridx = coords_tuple[0]
                colidx = coords_tuple[1]
                subgoal_idx = binv2num(sgidx)
                p = tup[1]
                reward = tup[2]
                sums += p*(gamma*values[ridx,colidx,subgoal_idx] + reward)
                if jnew < sums:
                  jnew = sums
              values[i,j,sg] = jnew
              diff_max = max(diff_max,abs(values[i,j,sg]-jold))

      done = 1
      # Policy update
      for i in range(10):
        for j in range(10):
          for sg in range(n2):      
            currentstate = [(i,j),num2binv(sg)]
            max_val = 0
            jnew = -1e9
            best_action = policy[i,j,sg]
            for action in actions:
              lst = env.get_transition_probabilites_and_reward(currentstate, action)
              sums = 0
              for tup in lst:
                nextstate = tup[0]
                [coords_tuple,sgidx] = nextstate
                ridx = coords_tuple[0]
                colidx = coords_tuple[1]
                subgoal_idx = binv2num(sgidx)
                p = tup[1]
                reward = tup[2]
                sums += p*(gamma*values[ridx,colidx,subgoal_idx] + reward)
                if jnew < sums:
                  best_action = action
                  jnew = sums
            # Check if policy is different
            if policy[i,j,sg] != best_action:
              done = 0
              policy[i,j,sg] = best_action
      if picount%1 == 0:
        print("Iteration ",picount,"improvement",np.amax(abs(values-Jold)))
    # Put your extra information needed for plots etc in this dictionary
    extra_info = {    }

    # End code

    # Do not change the number of output values
    return {"Values": values, "Policy": policy}, extra_info