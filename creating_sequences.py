'''
Simple script that creates a random set of bead samples and agent choices for a given number of trials

'''

import numpy as np

class generateTrials:
    def __init__(self, num_trials):
        self.num_trials = num_trials
        self.trials = 0

    def round_5(self, x):
        remainder = round(x) % 5
        if remainder >= 3:
            num = x + 5 - remainder
        else:
            num = x - remainder
        if num < 5:
            return 5
        elif num > 95:
            return 95
        else:
            return num

    def main(self):
        np.random.seed(34)
        bead_samples = np.arange(1, 8)
        agent_choices = np.zeros(self.num_trials)
        for trial in range(self.num_trials):
            agent_choices[trial] = self.round_5((bead_samples[trial % 7] / 7 + np.random.normal(0, 0.2)) * 100)
        self.trials = agent_choices


test = generateTrials(100)
test.main()
