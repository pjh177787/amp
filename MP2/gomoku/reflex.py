class Reflex:
    def __init__(self):
        pass
    
    def find_move(self, board, player):
        if player == 'x':
            opponent = 'o'
        elif player == 'o':
            opponent = 'x'
        else:
            print('I don\'t know you.')
            return -1, -1
        return 1, 1
        
        # test for consecutive four
        