#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    hid = dir(hidden_4)
    for x in range(len(hid)):
        if hid[x][0] != "_":
            print(hid[x])
