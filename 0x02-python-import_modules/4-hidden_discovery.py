#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for i in names:
        if i.startswith("__", 0, 2):
            continue
        else:
            print(i)
