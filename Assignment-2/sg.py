           # for sgidx in range(len(self.subgoal_location)):
            #   if ncoords[0] == self.subgoal_location[sgidx][0] and ncoords[1] == self.subgoal_location[sgidx][1]:
            #     # If already reached ignore
            #     if state[1][sgidx]:
            #       rew = self.non_terminal_reward
            #       break
            #     else:
            #       nextstate[1][sgidx] = 1
            #       rew = self.subgoal_reward[sgidx]
            #       break