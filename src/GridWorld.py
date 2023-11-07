import numpy as np

class GridWorld:
    def __init__(self, filename, learning_rate):
        self.map = np.array(self.read_map(filename))
        self.num_rows = self.map.shape[0]
        self.num_cols = self.map.shape[1]
        self.states_space = self.num_rows * self.num_cols
        self.action_space = 4
        self.turtle_pos = self.get_pos_tutle()

    # read grid map
    def read_map(self, filename):
        try:
            result = []
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    row = [str(s) for s in line.strip()]
                    result.append(row)
            return result

        except Exception as e:
            print(str(e))
            exit(1)
    
    def get_pos_tutle(self):
        pos = np.where(self.map == 'P')
        return [pos[0][0], pos[1][0]]