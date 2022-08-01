def minion_game(string):
    p1 = 0
    p2 = 0
    s_len = len(string)
    for i in range(s_len):
        if s[i] in "AEIOU":
            p1 += (s_len)-i
        else :
            p2 += (s_len)-i
    
    if p1 > p2:
        print("Kevin", p1)
    elif p1 < p2:
        print("Stuart",p2)
    elif p1 == p2:
        print("Draw")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)