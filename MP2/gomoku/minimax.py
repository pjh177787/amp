from copy import deepcopy

class Minimax:
    def __init__(self, player, board):
        self.blue_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.red_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'e', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.bd = board
        self.move = 0
        if player == 'blue':
            self.player = 'blue'
            self.opponent = 'red'
            self.all_alfa = self.blue_alfa
        elif player == 'red':
            self.player = 'red'
            self.opponent = 'blue'
            self.all_alfa = self.red_alfa
        else:
            print('I don\'t know you.')
    
    def force_move(self, row, col):
        alfa = self.all_alfa[self.move]
        self.move += 1
        return row, col, alfa
    
    def evaluate(self, board):
        one_away = board.check_one_away(self.player)
        two_away = board.check_two_away(self.player)
        three_away = board.check_three_away(self.player)
        
        value = one_away*100 + two_away*20 + three_away*5
        return value
    
    def find_move(self):
        alfa = self.all_alfa[self.move]
        self.move += 1
        
        row, col = self.bd.check_has_four(self.player)
        if self.bd.is_movable(row, col):
            return row, col, alfa
        row, col = self.bd.check_has_four(self.opponent)
        if self.bd.is_movable(row, col):
            return row, col, alfa
        row, col = self.bd.check_has_three(self.player)
        if self.bd.is_movable(row, col):
            return row, col, alfa
        
        new_bd = deepcopy(self.bd)
        next_move = self.minimax(2, new_bd)
        
        if next_move == (-1, -1):
            print('WHAT')
            next_move = self.bd.pick_random()
        
        row, col = next_move
        return row, col, alfa
    
    def minimax(self, depth, board):
        if depth == 0:
            result_score = 0
            result_move = (-1, -1)
            for next_move in moves:
                new_bd = deepcopy(self.bd)
                row, col = next_move
                new_bd.make_move(row, col, alfa)
                score = evaluate(new_bd)
                if (score > result_score):
                    result_score = score
                    result_move = next_move
            return result_move, result_score
        
        moves = self.bd.find_winning_block(self.player)
        if depth%2 == 0:
            # max node
            result_score = 0
            result_move = (-1, -1)
            for next_move in moves:
                new_bd = deepcopy(self.bd)
                row, col = next_move
                new_bd.make_move(row, col, alfa)
                _, score = minimax(depth - 1, new_bd)
                if (score > result_score):
                    result_score = score
                    result_move = next_move
        else:
            # min node
            result_score = 9999
            result_move = (-1, -1)
            for next_move in moves:
                new_bd = deepcopy(self.bd)
                row, col = next_move
                new_bd.make_move(row, col, alfa)
                _, score = minimax(depth - 1, new_bd)
                if (score < result_score):
                    result_score = score
                    result_move = next_move
            
        return result_move, result_score
            
            