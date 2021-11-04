def value_iteration(env, gamma=0.99):
    '''
    Code your value iteration algorithms here, the function should return a np 
    array of dimensions (10, 10, 2^(no. of sub-goals)). Also return the final
    policy grid corresponding to the final values.
    '''
    
    # extracting no. of subgoals
    n = len(env.subgoal_reward)
    n2 = 2**n

    # Initial Values
    values = np.zeros((10, 10, n2))

    # Initial policy
    policy = np.empty((10, 10, n2), object)
    policy[:] = 'N' # Make all the policy values as 'N'


    # Begin code here

    diff_max = 1
    grid_size = env.grid_size
    n = len(env.subgoal_location)

    actions = env.actions.keys()

    count = 0
    error_bnd = []

    max_rewards = []
    while diff_max >= 1e-5:
      if count%10 == 0:
        print("Iteration ",count,"diff_max",diff_max)
      count += 1
      diff_max = 0

      for i in range(env.grid_size[0]):
        for j in range(env.grid_size[1]):
          for sg in range(n2):
            jold = values[i,j,sg].copy()
            currentstate = [(i,j),num2binv(sg,n)]
            jnew = -1e9
            best_action = 'N'
            for action in actions:
              lst = env.get_transition_probabilites_and_reward(currentstate, action)
              # if count%10==0:
              #   print("currentstate:",currentstate,"nextstates:",lst,"action:",action)
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
            values[i,j,sg] = jnew
            policy[i,j,sg] = best_action
            diff_max = max(diff_max,abs(values[i,j,sg]-jold))
            error_bnd.append(diff_max)

    # Put your extra information needed for plots etc in this dictionary
    extra_info = {"Errors":error_bnd}

    # End code

    # Do not change the number of output values
    return {"Values": values, "Policy": policy}, extra_info