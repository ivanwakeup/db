import fileinput

def get_key(f, args):
    if not args:
        return -1
    f.seek(0)
    for line in f.readlines():
        line_arr = line.split(":")
        if line_arr[0] == args[0]:
            return line_arr[1]
    return -1


def set_key(f, args):
    if len(args) != 2:
        return -1
    f.seek(0)
    for line in f.readlines():
        line_arr = line.split(":")
        if line_arr[0] == args[0]:
            return line_arr[1]
    f.write(f"{args[0]}:{args[1]}\n")
    return 0


if __name__ == "__main__":
    switch = {
      "set": set_key,
      "get": get_key
    }

    file = open("db.ivn", "a+")
    while True:
        cmd = input(">")
        if cmd == "exit":
            break
        cmd_parts = cmd.split()
        fxn = switch[cmd_parts[0]]
        ret = fxn(file, cmd_parts[1:])
        if isinstance(ret, str):
            print(ret)
    file.close()

    


