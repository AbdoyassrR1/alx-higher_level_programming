#!/usr/bin/python3
if __name__ == "__main__":
    import hddien_4
    name = dir(hddien_4)

    for n in range(len(name)):
        if n[0:2] != "__":
            print(name)
