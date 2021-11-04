       rew = self.non_terminal_reward
        probs = self.action_stochasticity
        transition_map = {}
        coords = state[0]
        
        for i in range(len(self.perpendicular_order)):
            if self.perpendicular_order[i]==action:
              transition_map['forward'] = self.actions[action]
              transition_map['right'] =self.actions[self.perpendicular_order[(i+1)%4]]
              transition_map['backward'] =self.actions[self.perpendicular_order[(i+2)%4]]
              transition_map['left'] =self.actions[self.perpendicular_order[(i+3)%4]]
              break

        i = 0
        p_invalid = 0
        for dn,action in transition_map.items():
          # perform the transition 
          ncoords = [coords[0]+action[0],coords[1]+action[1]]
          nextstate = [(ncoords[0],ncoords[1]),state[1].copy()]
          # check whether it goes out of grid
          if self._out_of_grid(ncoords):
            p_invalid = probs[i]
            rew = self.non_terminal_reward
            if p_invalid:
              nextstates_prob_rews.append((state.copy(),p_invalid,rew))
          elif self._grid_state((ncoords[0],ncoords[1]))=='goal':
            rew = self.terminal_reward
            p = probs[i]
            if p:
              nextstates_prob_rews.append((nextstate,p,rew))
          else:
            p = probs[i]
            rew = self.non_terminal_reward
            # Check if it is a subgoal
            if (ncoords[0],ncoords[1]) in self.subgoal_location:
              sgidx = self.subgoal_location.index((ncoords[0],ncoords[1]))
              if not state[1][sgidx]:
                nextstate[1][sgidx] = 1
                rew = self.subgoal_reward[sgidx]
            if p:
              nextstates_prob_rews.append((nextstate,p,rew))
          i += 1