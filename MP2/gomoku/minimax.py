from copy import deepcopy

class Minimax:
    def __init__(self, player):
        self.blue_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.red_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'e', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.move = 0
        if player == 'blue':
            self.player = 'blue'
            self.opponent = 'red'
            self.all_alfa = self.blue_alfa
            self.alt_alfa = self.red_alfa
        elif player == 'red':
            self.player = 'red'
            self.opponent = 'blue'
            self.all_alfa = self.red_alfa
            self.alt_alfa = self.blue_alfa
        else:
            print('I don\'t know you.')
    
    def force_move(self, row, col):
        alfa = self.all_alfa[self.move]
        self.move += 1
        return row, col, alfa
    
    def find_move(self, board):
        alfa = self.all_alfa[self.move]
        self.move += 1

        if self.move == 1:
            if board.is_movable(3, 3):
                return 3, 3, alfa, 0
        
        row, col = board.check_has_four(self.player)
        if board.is_movable(row, col):
            return row, col, alfa, 0
        row, col = board.check_has_four(self.opponent)
        if board.is_movable(row, col):
            return row, col, alfa, 0
        row, col = board.check_has_three(self.opponent)
        if board.is_movable(row, col):
            return row, col, alfa, 0
        
        new_bd = deepcopy(board)

        next_move, score, expanded = self.minimax(2, new_bd, 0)
        
        if next_move == (-1, -1):
            # print('WHAT')
            next_move = board.pick_random()
        
        row, col = next_move
        # print(next_move)
        return row, col, alfa, expanded

    def evaluate(self, board):
        complete_self = board.check_complete(self.player)
        one_away_self = board.check_one_away(self.player)
        two_away_self = board.check_two_away(self.player)
        three_away_self = board.check_three_away(self.player)
        # print('Self: 4:', one_away_self, '3:', two_away_self, '2:', three_away_self)
        complete_oppo = board.check_complete(self.opponent)
        one_away_oppo = board.check_one_away(self.opponent)
        two_away_oppo = board.check_two_away(self.opponent)
        three_away_oppo = board.check_three_away(self.opponent)
        # print('Oppo: 4:', one_away_oppo, '3:', two_away_oppo, '2:', three_away_oppo)
        
        value = complete_self*200 + one_away_self*100 + two_away_self*20 + three_away_self*5 - complete_oppo*195 - one_away_oppo*95 - two_away_oppo*15 - three_away_oppo*3
        return value

    def minimax(self, depth, board, expanded):
        _, sub_moves_0 = board.find_winning_block(self.player)
        _, sub_moves_1 = board.find_winning_block(self.opponent)
        sub_moves = sub_moves_0 + sub_moves_1
        if depth == 0:
            if sub_moves[0] == (-1, -1):
                if board.check_winner() == self.player:
                    return (-1, -1), 9999, expanded
                else:
                    return (-1, -1), 0, expanded
            # print('Player:', self.player, 'Depth:', depth, 'with', sub_moves)
        
            result_score = -9999
            result_move = (-1, -1)
            for next_move in sub_moves:
                expanded += 1
                new_bd = deepcopy(board)
                row, col = next_move
                new_bd.make_move(row, col, self.all_alfa[self.move])
                # new_bd.prt()
                score = self.evaluate(new_bd)
                if (score > result_score):
                    result_score = score
                    result_move = next_move
                # print('Score:', score, 'Move:', next_move)
            # print('Max Score:', result_score, 'Max Move:', result_move)
            return result_move, result_score, expanded
        
        if depth%2 == 0:
            if sub_moves[0] == (-1, -1):
                if board.check_winner() == self.player:
                    return (-1, -1), 9999, expanded
                else:
                    return (-1, -1), 0, expanded
            # print('Player:', self.player, 'Depth:', depth, 'with', sub_moves)
            
            # max node
            result_score = -9999
            result_move = (-1, -1)
            expaned_local = 0
            for next_move in sub_moves:
                new_bd = deepcopy(board)
                row, col = next_move
                new_bd.make_move(row, col, self.all_alfa[self.move])
                _, score, r_expanded = self.minimax(depth - 1, new_bd, expanded)
                if (score > result_score):
                    result_score = score
                    result_move = next_move
                expaned_local += r_expanded
                # print('Score(max):', score, 'Move(max):', next_move)
        else:
            if sub_moves[0] == (-1, -1):
                if board.check_winner() == self.opponent:
                    return (-1, -1), 9999, expanded
                else:
                    return (-1, -1), 0, expanded
            # print('Player:', self.opponent, 'Depth:', depth, 'with', sub_moves)
        
            # min node
            result_score = 9999
            result_move = (-1, -1)
            expaned_local = 0
            for next_move in sub_moves:
                new_bd = deepcopy(board)
                row, col = next_move
                new_bd.make_move(row, col, self.alt_alfa[self.move])
                _, score, r_expanded = self.minimax(depth - 1, new_bd, expanded)
                if (score < result_score):
                    result_score = score
                    result_move = next_move
                # print('Score(min):', score, 'Move(min):', next_move)
                expaned_local += r_expanded
        # print('Result Score:', result_score, 'Result Move:', result_move)
        return result_move, result_score, expaned_local + 1
            
            
