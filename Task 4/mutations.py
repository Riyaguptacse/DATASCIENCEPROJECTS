def mutate_string(string, position, character):
    lists = list(string)
    lists[position] = character;
    string = ''.join(lists);
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)