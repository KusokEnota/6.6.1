"""Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей"""

N = 8
X = []
Y = []


def cheas():
    for i in range(N):
        new_x, new_y = [int(s) for s in input("Введите координаты (x-y) через пробел: \n").split()]
        print(new_x, new_y)
        X.append(new_x)
        Y.append(new_y)
    correct = False
    for i in range(N):
        for j in range(i + 1, N):
            if X[i] == X[j] or Y[i] == Y[j] or abs(X[i] - Y[j]) == abs(X[i] - Y[j]):
                correct = True

    if correct:
        print("True")
    else:
        print("False")


cheas()

def rand(board, r):
    if r == 8:
        print(board)
        return
    for c in range(8):
        if is_valid(board, r, c):
            board[r] = c
            rand(board, r + 1)
            board[r] = None


def is_valid(board, r, c):
    for i in range(r):
        if board[i] == c or board[i] - i == c - r or board[i] + i == c + r:
            return False
    return True


board = [None] * 8
rand(board, 0)

def rand(board, r):
    if r == 8:
        print(board)
        return
    for c in range(8):
        if is_valid(board, r, c):
            board[r] = c
            rand(board, r + 1)
            board[r] = None


def is_valid(board, r, c):
    for i in range(r):
        if board[i] == c or board[i] - i == c - r or board[i] + i == c + r:
            return False
    return True


board = [None] * 8
rand(board, 0)
