import random as rd
import math

class Pong:
    VOID = 0
    UP = 1
    DOWN = 2
    PADDLE_HEIGHT = 0.2
    PADDLE_STEP = 0.4
    PADDLE_X = 1
    REWARDS = {'rebounce': 1, 'pass': -1, 'other': 0, 'best':2}

    class State:
        def __init__(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y, board_size):
            self.ball_x = ball_x
            self.ball_y = ball_y
            self.v_x = velocity_x
            self.v_y = velocity_y
            self.pad_y = paddle_y
            self.b_size = board_size
            self.score = 0
            self.bounce_count = 0

        def move_paddle(self, pad_move):
            if pad_move > 0:
                if self.pad_y < (1 - Pong.PADDLE_HEIGHT - Pong.PADDLE_STEP):
                    self.pad_y += pad_move
                else:
                    self.pad_y = 1 - PADDLE_HEIGHT
            if pad_move < 0:
                if self.pad_y > Pong.PADDLE_STEP:
                    self.pad_y += pad_move
                else:
                    self.pad_y = 0

        def rand_v(self):
            while True:
                v_x_new = -self.v_x + rd.uniform(-0.015, 0.015)
                if abs(v_x_new) > 0.03:
                    self.v_x = v_x_new
                    break
            self.v_y += rd.uniform(-0.03, 0.03)

        def get_state(self):
            ball_x = math.floor(self.ball_x*(self.b_size[0] - 1))
            ball_y = math.floor(self.ball_y*(self.b_size[1] - 1))
            v_x = 1 if self.v_x > 0 else -1
            v_y = (1 if self.v_y > 0 else -1) if abs(self.v_y) >= 0.015 else 0
            disc_pad = math.floor((self.b_size[1] - 1)*self.pad_y/(1 - Pong.PADDLE_HEIGHT))
            pad_y = disc_pad if disc_pad < self.b_size[1] else self.b_size[1] - 1
            reture (ball_x, ball_y, v_x, v_y, pad_y)

        def is_good_game(self):
            return self.ball_x > 1

    class Agent:
        
