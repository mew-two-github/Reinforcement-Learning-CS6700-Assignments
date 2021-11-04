        # i, j = self.perpendicular_order.index(action), 0
        # nextstates_prob_rews = []
        # while j<4:
        #   next_loc = (loc[0]+direction[0],loc[1]+direction[1])
        #   next_loc = loc if self._out_of_grid(next_loc) else next_loc
        #   if self.action_stochasticity[j]>0:
        #     next_grid_state = self._grid_state(next_loc)
        #     if next_grid_state.startswith('subgoal'):
        #       next_subgoal_ind = int(next_grid_state[7:])-1
        #     else:
        #       next_subgoal_ind =0
        #     next_subgoal_bit = 0
        #     if next_grid_state.startswith('subgoal'):
        #       next_subgoal_bit = 1 << (len(self.subgoal_location)-1-next_subgoal_ind)
        #     if next_grid_state == 'goal':
        #       reward = self.terminal_reward
        #     elif next_grid_state.startswith('subgoal') and (binv & next_subgoal_bit) == 0:
        #       reward =  self.subgoal_reward[next_subgoal_ind]
        #     else:
        #       reward = self.non_terminal_reward
        #     nextstates_prob_rews.append([(next_loc,binv|next_subgoal_bit),self.action_stochasticity[j],reward])
        #   j += 1
        #   i = (i+1)%4
        #   direction = self.actions.get(self.perpendicular_order[i])