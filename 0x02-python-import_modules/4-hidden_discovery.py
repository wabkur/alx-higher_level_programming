#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    besh = dir(hidden_4)
    for x in besh:
        if x[:2] != "__":
            print(x)
