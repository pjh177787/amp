class Reflex:
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
    
    def find_move(self):
        alfa = self.all_alfa[self.move]
        self.move += 1
        
        row, col = self.bd.check_has_four(self.player)
        if self.bd.is_movable(row, col):
            print('found winning four')
            return row, col, alfa
        row, col = self.bd.check_has_four(self.opponent)
        if self.bd.is_movable(row, col):
            print('found losing four')
            return row, col, alfa
        row, col = self.bd.check_has_three(self.opponent)
        if self.bd.is_movable(row, col):
            print('found losing three')
            return row, col, alfa
        
        winning_moves = self.bd.find_winning_block(self.player)
        
        if len(winning_moves) == 0:
            next_move = self.bd.pick_random()
            row, col = next_move
        else:
            row, col = winning_moves[0]
        return row, col, alfa
        
        # test for consecutive four
        