line1 = input()
line2 = input()

n, s, m = map(int, line1.split(" ")) 
board = [int(k) for k in line2.split(" ")]

def return_el_at_board(index: int):
    return board[index]
    
def game(hops: int, n: int, s: int, m: int,  visited: set):
    # check left, right, cycle
    if s in visited:
        return hops, 'cycle'
        
    if s < 0:
        return hops, 'left'
        
    if s > n:
        return hops, 'right'
        
    val_at_board = return_el_at_board(s)
    
    if val_at_board== m:
        return hops, 'magic'
    
    visited.add(s)
    new_s = s + abs(val_at_board) if val_at_board > 0 else s - abs(val_at_board)
    return game(hops+1, n, new_s, m, visited)
    
# hops = 0, n,s = n - 1, s -1 for 0 based indexed array, visisted is a set of indexes 
answer = game(0, n-1,s-1, m,set())    
print(answer[1])
print(answer[0])
