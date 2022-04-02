'''
Simple script that creates a random set of bead samples and agent choices for a given number of trials
'''

import numpy as np

class generateTrials:

    def __init__(self, num_trials):
        self.num_trials = num_trials
        self.trials = None
        self.beads = None

    def round_5(self, x):
        x_round = round(x)
        remainder = x_round % 5
        if remainder >= 3:
            num = x_round + 5 - remainder
        else:
            num = x_round - remainder
        if num < 5:
            return 5
        elif num > 95:
            return 95
        else:
            return num

    def main(self):
        np.random.seed(34)
        bead_samples = np.arange(1, 8)
        agent_choices = []
        beads = []
        for trial in range(self.num_trials):
            agent_choices.append(100 - self.round_5((bead_samples[trial % 7] / 7 + np.random.normal(0, 0.2)) * 100))
            beads.append(bead_samples[trial % 7])
        self.agent_choice_sequence = agent_choices
        self.beads_sequence = beads

    def write_to_text(self):
        with open('agent_choices.txt', 'w') as f:
            for i in self.agent_choice_sequence:
                f.write("{}, ".format(i))
        with open('beads_sequence.txt', 'w') as f:
            for i in self.beads_sequence:
                f.write("{}, ".format(i))


if __name__ == "__main__":
    test = generateTrials(num_trials=115)
    test.main()
    test.write_to_text()





