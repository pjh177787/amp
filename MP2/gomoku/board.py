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
        print()
        
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
    
    def make_move(self, row, col, alfa):
        if not self.board[row][col] == '.':
            print('Can\'t  play here.')
        else:
            self.board[row][col] = alfa
                
    def get_player_places(self, player):
        if player == 'red':
            red_places = []
            for row in self.board:
                for cell in row:
                    if cell.islower():
                        red_places.append((row, cell))
            return red_places
        elif player == 'blue':
            blue_places = []
            for row in self.board:
                for cell in row:
                    if cell.isupper():
                        blue_places.append((row, cell))
            return blue_places
        else:
            print('I don\'t know you.')
        return places
    
    def row_has_four(self, player):
        bd = self.get_board()
        for row in range(7):
            for col in range(4):
                flag = True
                for cell in bd[row, col:col+4]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def col_has_four(self, player):
        bd = self.get_board()
        for col in range(7):
            for row in range(4):
                flag = True
                for cell in bd[row:row+4, col]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def l2r_has_four(self, player):
        bd = self.get_board()
        for col in range(4):
            for row in range(4):
                flag = True
                for i in range(4):
                    cell = bd[row+i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    return row, col
        # print('Not found')
        return -1, -1
    
    def r2l_has_four(self, player):
        bd = self.get_board()
        for col in range(3, 7):
            for row in range(4):
                flag = True
                for i in range(4):
                    cell = bd[row+i, col-i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    return row, col
        # print('Not found')
        return -1, -1
    
    def row_has_three(self, player):
        bd = self.get_board()
        for row in range(7):
            for col in range(5):
                flag = True
                for cell in bd[row, col:col+3]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def col_has_three(self, player):
        bd = self.get_board()
        for col in range(7):
            for row in range(5):
                flag = True
                for cell in bd[row:row+3, col]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def l2r_has_three(self, player):
        bd = self.get_board()
        for col in range(5):
            for row in range(5):
                flag = True
                for i in range(3):
                    cell = bd[row+i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    return row, col
        # print('Not found')
        return -1, -1
    
    def r2l_has_three(self, player):
        bd = self.get_board()
        for col in range(2, 7):
            for row in range(5):
                flag = True
                for i in range(3):
                    cell = bd[row+i, col-i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    return row, col
        # print('Not found')
        return -1, -1
    
    def row_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(7):
            for col in range(3):
                count = 0
                flag = True
                for cell in bd[row, col:col+5]:
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row, col + 4)))
        return wb_list
    
    def col_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(3):
            for col in range(7):
                count = 0
                flag = True
                for cell in bd[row:row+5, col]:
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row + 4, col)))
        return wb_list 
    
    def l2r_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(3):
            for col in range(3):
                count = 0
                flag = True
                for i in range(5):
                    cell = bd[row+i, col+i]
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row + 4, col + 4)))
        return wb_list
    
    def r2l_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(3):
            for col in range(4, 7):
                count = 0
                flag = True
                for i in range(5):
                    cell = bd[row+i, col-i]
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row + 4, col - 4)))
        return wb_list
                     
    def find_winning_block(self, player):
        row_wb_list = sorted(self.row_has_winning_block(player), reverse = True)
        # print(row_wb_list)
        col_wb_list = sorted(self.col_has_winning_block(player), reverse = True)
        # print(col_wb_list)
        l2r_wb_list = sorted(self.l2r_has_winning_block(player), reverse = True)
        # print(l2r_wb_list)
        r2l_wb_list = sorted(self.r2l_has_winning_block(player), reverse = True)
        # print(r2l_wb_list)
        
        max_wb_list = max(row_wb_list[0][0], col_wb_list[0][0], l2r_wb_list[0][0], r2l_wb_list[0][0])
        
        if row_wb_list[0][0] == max_wb_list:
            row_s, col_s = row_wb_list[0][1]
            row_t, col_t = row_wb_list[0][2]
            if self.is_movable(row_s, col_s - 1) and not self.is_movable(row_s, col_s):
                return row_s, col_s - 1
            else:
                for col in range(col_s, col_t + 1):
                    if self.is_movable(row_s, col):
                        return row_s, col        
        if col_wb_list[0][0] == max_wb_list:
            row_s, col_s = col_wb_list[0][1]
            row_t, col_t = col_wb_list[0][2]
            if self.is_movable(row_s - 1, col_s) and not self.is_movable(row_s, col_s):
                return row_s - 1, col_s
            else:
                for row in range(row_s, row_t + 1):
                    if self.is_movable(row, col_s):
                        return row, col_s        
        if l2r_wb_list[0][0] == max_wb_list:
            row_s, col_s = l2r_wb_list[0][1]
            row_t, col_t = l2r_wb_list[0][2]
            if self.is_movable(row_s - 1, col_s - 1) and not self.is_movable(row_s, col_s):
                return row_s - 1, col_s - 1
            else:
                for i in range(5):
                    if self.is_movable(row_s + i, col_s + i):
                        return row_s + i, col_s + i       
        if r2l_wb_list[0][0] == max_wb_list:
            row_s, col_s = r2l_wb_list[0][1]
            row_t, col_t = r2l_wb_list[0][2]
            if self.is_movable(row_s - 1, col_s + 1) and not self.is_movable(row_s, col_s):
                return row_s - 1, col_s + 1
            else:
                for i in range(5):
                    if self.is_movable(row_s + i, col_s + i):
                        return row_s + i, col_s + i
         
        