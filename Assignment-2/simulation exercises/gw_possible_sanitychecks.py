  """Possible Sanity Checks to be made(if Needed)"""
  # Check if params exist (YT)
  def _verify_params(self,kwargs):
    assert "low_salary" in kwargs, "no param for low_salary"
    assert "high_salary" in kwargs, "no param for high_salary"
    assert "low_quit_prob" in kwargs, "no param for low_quit_prob"
    assert "high_quit_prob" in kwargs, "no param for high_quit_prob"
    assert "self_edit_cost" in kwargs, "no param for self_edit_cost"
    assert "low_add_cost" in kwargs, "no param for low_add_cost"
    assert "high_add_cost" in kwargs, "no param for high_add_cost"
    assert "low_add_success_prob" in kwargs, "no param for low_add_success_prob"
    assert "high_add_success_prob" in kwargs, "no param for high_add_success_prob"
# Shapes and sum of probabs check (Taxi)
    def _verify(self):
        """ 
        Verify that data conditions are met:
        Number of actions matches shape of next state and actions
        Every probability distribution adds up to 1 
        """
        ns = len(self.possible_states)
        for state in self.possible_states:
            ac = self._possible_actions[state]
            na = len(ac)
            rp = self._ride_probabilities[state]
            assert np.all(rp.shape == (na, ns)), "Probabilities shape mismatch"
        
            rr = self._ride_rewards[state]
            assert np.all(rr.shape == (na, ns)), "Rewards shape mismatch"

            assert np.allclose(rp.sum(axis=1), 1), "Probabilities don't add up to 1"