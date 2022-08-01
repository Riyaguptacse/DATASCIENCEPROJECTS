def split_and_join(line):
    Op = line.split();
    Op = "-".join(Op)
    return Op;

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)