import argparse
import os
import random as rd
import math
from jsonpickle import encode, decode
from datetime import datetime

class Pong:
    VOID = 0
    UP = 1
    DOWN = 2
    PADDLE_HEIGHT = 0.2
    PADDLE_STEP = 0.04
    PADDLE_X = 1
    REWARDS = {'rebounce': 1, 'pass': -1, 'other': 0, 'best':2}

    class State:
        def __init__(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y, board_size):
            self.ball_x = ball_x
            self.ball_y = ball_y
            self.velocity_x = velocity_x
            self.velocity_y = velocity_y
            self.paddle_y = paddle_y
            self.board_size = board_size
            self.score = 0
            self.bounce_count = 0

        def move_paddle(self, pad_move):
            if pad_move > 0:
                if self.paddle_y < 1 - Pong.PADDLE_HEIGHT - Pong.PADDLE_STEP:
                    self.paddle_y += pad_move
                else:
                    self.paddle_y = 1 - Pong.PADDLE_HEIGHT
            elif pad_move < 0:
                if self.paddle_y > Pong.PADDLE_STEP:
                    self.paddle_y += pad_move
                else:
                    self.paddle_y = 0

        def rand_v(self):
            while True:
                velocity_x_new = -self.velocity_x + rd.uniform(-0.015, 0.015)
                if abs(velocity_x_new) > 0.03:
                    self.velocity_x = velocity_x_new
                    break
            self.velocity_y += rd.uniform(-0.03, 0.03)

        def get_state(self):
            ball_x = math.floor(self.ball_x*(self.board_size[0] - 1))
            ball_y = math.floor(self.ball_y*(self.board_size[1] - 1))
            velocity_x = 1 if self.velocity_x > 0 else -1
            velocity_y = (1 if self.velocity_y > 0 else -1) if abs(self.velocity_y) >= 0.015 else 0
            disc_pad = math.floor((self.board_size[1] - 1)*self.paddle_y/(1 - Pong.PADDLE_HEIGHT))
            paddle_y = disc_pad if disc_pad < self.board_size[1] else self.board_size[1] - 1
            return (ball_x, ball_y, velocity_x, velocity_y, paddle_y)

        def is_good_game(self):
            return self.ball_x > 1

    class Agent:
        class Utility:
            def __init__(self, utility, frequency):
                self.utility = utility
                self.frequency = frequency

        def __init__(self, board_size, alpha, gamma, ne):
            self.action_utility = [[Pong.Agent.Utility(0, 0) for action in range(3)] 
                            for item in range(board_size[0]*board_size[1]*board_size[1]*2*3)]
            self.prev_state = None
            self.prev_action = None
            self.prev_reward = None
            self.alpha = alpha
            self.gamma = gamma
            self.ne = ne
            self.board_size = board_size
            self.is_explore = True

        def locate(self, utility, state):
            (ball_x, ball_y, velocity_x, velocity_y, paddle_y) = state
            return utility[(((ball_y*self.board_size[0] + ball_x)*self.board_size[0] + paddle_y)*3 + velocity_y + 1)*2 + (velocity_x + 1)//2]

        def get_max_pairs(self, utility_pair):
            sorted_list = sorted(utility_pair, key = lambda mypair: -mypair[1])
            max_pairs = list(filter(lambda x: x[1] == sorted_list[0][1], sorted_list))
            return max_pairs[math.floor(rd.uniform(0, len(max_pairs)))][0]

        def explore(self, state, action):
            if self.is_explore:
                if self.locate(self.action_utility, state)[action].frequency < self.ne:
                    return Pong.REWARDS['best']
            return self.locate(self.action_utility, state)[action].utility

        def set_explore(self, boo):
            self.is_explore = boo

        def policy(self, curr_state):
            return self.get_max_pairs(list(map(lambda each_action: (each_action, self.explore(curr_state, each_action)), range(0, 3))))

        def update_utility(self, curr_state, next_state, action, reward):
            # print(self.locate(self.action_utility, curr_state)[action].frequency, self.locate(self.action_utility, curr_state)[action].utility)
            self.locate(self.action_utility, curr_state)[action].frequency += 1
            # print(self.locate(self.action_utility, curr_state)[action].frequency, self.locate(self.action_utility, curr_state)[action].utility)
            max_q = max(list(map(lambda each_util: each_util.utility, self.locate(self.action_utility, next_state)))) if reward != Pong.REWARDS['pass'] else 0
            self.locate(self.action_utility, curr_state)[action].utility += \
                self.alpha(self.locate(self.action_utility, curr_state)[action].frequency) \
                *(reward + self.gamma*max_q - self.locate(self.action_utility, curr_state)[action].utility)

    def __init__(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y, board_size):
        self.board_size = board_size
        self.restart(ball_x, ball_y, velocity_x, velocity_y, paddle_y)

    def restart(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y):
        self.state = Pong.State(ball_x, ball_y, velocity_x, velocity_y, paddle_y, self.board_size)

    def game(self, agent):
        while not self.state.is_good_game():
            self.curr_state = self.state.get_state()
            # print(self.curr_state)
            curr_state = 0
            next_action = agent.policy(self.curr_state)
            # print(next_action)
            self.proceed(next_action)
            self.next_state = self.state.get_state()
            agent.update_utility(self.curr_state, self.next_state, next_action, self.state.score)

    def proceed(self, action):
        self.state.score = 0
        prev_x = self.state.ball_x
        prev_y = self.state.ball_y
        self.state.ball_x += self.state.velocity_x
        self.state.ball_y += self.state.velocity_y

        if action == Pong.UP:
            self.state.move_paddle(-Pong.PADDLE_STEP)
        elif action == Pong.DOWN:
            self.state.move_paddle(Pong.PADDLE_STEP)

        if self.state.ball_y < 0:
            self.state.ball_y *= -1
            self.state.velocity_y *= -1
        if self.state.ball_y > 1:
            self.state.ball_y = 2 - self.state.ball_y
            self.state.velocity_y *= -1
        if self.state.ball_x < 0:
            self.state.ball_x *= -1
            self.state.velocity_x *= -1
        if self.rebounce(prev_x, prev_y):
            self.state.score = Pong.REWARDS['rebounce']
            self.state.bounce_count += 1
            self.state.ball_x = 2*Pong.PADDLE_X - self.state.ball_x
            self.state.rand_v()
        if self.state.is_good_game():
            self.state.score = Pong.REWARDS['pass']
        return self.state.score

    def rebounce(self, prev_x, prev_y):
        intersection = prev_y + (self.state.ball_y - prev_y)/(self.state.ball_x - prev_x)*(1 - prev_x)
        return self.state.ball_x >= 1 and intersection >= self.state.paddle_y \
            and intersection <= self.state.paddle_y + Pong.PADDLE_HEIGHT

def find(dir, file):
    for root, dir, files in os.walk(dir):
        if file in files:
            return True
    return False

def parse_utility(utility):
    return [[Pong.Agent.Utility(item[action]['utility'], item[action]['frequency'])
            for action in range(3)] for item in utility]
