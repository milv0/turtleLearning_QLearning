import numpy as np
import random
import copy
from TurtleGraphic import TurtleGraph
import turtle

class QLearning:
    def __init__(self, map_info, episodes = 1000, gamma=0.5, learning_rate=0.7):
        # setting model
        self.map = map_info
        self.start_state = self.get_state_number(map_info.turtle_pos[0],map_info.turtle_pos[1])
        self.q_table = np.zeros([self.map.states_space, self.map.action_space])

        # setting hyper-parameter
        self.episodes = episodes
        self.max_episode_steps = 100
        self.exploration = 0.9
        self.gamma = gamma
        self.lr = learning_rate

        # setting reward function
        self.reward = {'0': -0.01, 'G': 10.0, 'T': -10.0, 'P': -0.01, '1': np.NaN}
        self.reward_func = self.get_reward_table()

    def run(self):
        for e in range(self.episodes):
            state = self.map.turtle_pos
            total_reward = 0
            done = False

            # calculate a episode
            for _ in range(self.max_episode_steps):
                # get next step
                action = self.get_action(state)
                next_state, reward, done = self.step(state, action)
                total_reward += reward

                # pos to state number
                state_num = self.get_state_number(state[1], state[0])
                next_state_num = self.get_state_number(next_state[1], next_state[0])

                # update the q table
                ## insert code !





                # update next state
                ## insert code !
                

                if done:
                    break
            print(f"Episode {e + 1}: total reward -> {total_reward}")

    def step(self, state, action):
        ns = copy.deepcopy(state) # next state
        
        # get next state
        if action == 0: # UP
            pass ## insert code !
        elif action == 1: # DOWN
            pass ## insert code !
        elif action == 2: # LEFT
            pass ## insert code !
        elif action == 3: # RIGHT
            pass ## insert code !

        if self.map.map[ns[0]][ns[1]] == '1':
            ns = state

        # get reward
        ## insert code ! nr (next reward)

        # get done
        ## insert code ! done


        # return
        return ns, nr, done

    def get_action(self, state):
        # return 1 ~ 4
        ## insert code !
        return action

    def get_reward_table(self):
        reward_table = np.zeros(self.map.states_space)
        for y in range(self.map.num_rows):
            for x in range(self.map.num_cols):
                s = self.get_state_number(x, y)
                reward_table[s] = self.reward[self.map.map[y][x]]
        return reward_table
    
    def get_state_number(self, x, y):
        return y * self.map.num_cols + x
    
    def get_result(self):
        state = copy.deepcopy(self.map.turtle_pos)
        act_list = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}
        total_reward = 0
        done = False
        t_graph = TurtleGraph(self.map)

        while not done:
            state_num = self.get_state_number(state[1], state[0])

            action = np.argmax(self.q_table[state_num])
            print(act_list[action])

            next_state, reward, done = self.step(state, action)
            total_reward += reward

            state = next_state
            t_graph.move_turtle(state[1], state[0], action)
        
        print(f"Total reward -> {total_reward}")
        turtle.mainloop()