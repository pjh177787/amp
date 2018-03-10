import numpy as np

class Board:
    def __init__(self):
        self.board = np.array([['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.']])
    
    def prt(self):
        for row in self.board:
            prt_str = ''
            for cell in row:
                prt_str += cell + ' '
            print(prt_str)
        
    def get_board(self):
        return self.board
        
    def get_space(self):
        spaces = []
        for row in self.board:
            for cell in row:
                if cell == '.':
                    spaces.append((row, cell))
        return spaces
    
    def is_movable(self, row, col):
        if row < 0 or row > 6 or col < 0 or col > 6:
            return False
        return self.board[row][col] == '.'
    
    def make_move(self, player, row, col):
        if not self.board[row][col] == '.':
            print('Can\'t  play here.')
        else:
            if player == 'x' or player == 'o':
                self.board[row][col] = player
            else:
                print('I don\'t know you.')
                
    def get_player_places(self, player):
        places = []
        if player == 'x' or player == 'o':
            for row in self.board:
                for cell in row:
                    if cell == player:
                        spaces.append((row, cell))
        else:
            print('I don\'t know you.')
        return places
    
    def row_has_four(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for row in range(7):
            for col in range(4):
                flag = True
                for cell in bd[row, col:col+4]:
                    if not cell == player:
                        flag = False
                        break
                if flag:       
                    return row, col
        print('Not found')
        return -1, -1
    
    def col_has_four(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for col in range(7):
            for row in range(3):
                flag = True
                for cell in bd[row:row+4, col]:
                    if not cell == player:
                        flag = False
                        break
                if flag:       
                    return row, col
        print('Not found')
        return -1, -1
    
    def l2r_has_four(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for col in range(4):
            for row in range(4):
                flag = True
                for i in range(4):
                    if not bd[row+i, col+i] == player:
                        flag = False
                        break
                if flag:
                    return row, col
        print('Not found')
        return -1, -1
    
    def r2l_has_four(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for col in range(3, 7):
            for row in range(4):
                flag = True
                for i in range(4):
                    if not bd[row+i, col-i] == player:
                        flag = False
                        break
                if flag:
                    return row, col
        print('Not found')
        return -1, -1
    
    def row_has_three(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for row in range(7):
            for col in range(5):
                flag = True
                for cell in bd[row, col:col+3]:
                    if not cell == player:
                        flag = False
                        break
                if flag:       
                    return row, col
        print('Not found')
        return -1, -1
    
    def col_has_three(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for col in range(7):
            for row in range(5):
                flag = True
                for cell in bd[row:row+3, col]:
                    if not cell == player:
                        flag = False
                        break
                if flag:       
                    return row, col
        print('Not found')
        return -1, -1
    
    def l2r_has_three(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for col in range(5):
            for row in range(5):
                flag = True
                for i in range(3):
                    if not bd[row+i, col+i] == player:
                        flag = False
                        break
                if flag:
                    return row, col
        print('Not found')
        return -1, -1
    
    def r2l_has_three(self, player):
        if not (player == 'x' or player == 'o'):
            print('I don\'t know you.')
            return -1, -1
        bd = self.get_board()
        for col in range(2, 7):
            for row in range(5):
                flag = True
                for i in range(3):
                    if not bd[row+i, col-i] == player:
                        flag = False
                        break
                if flag:
                    return row, col
        print('Not found')
        return -1, -1
                
        