import hidden_4


def print_names():
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)


if __name == "__main__":
    print_names()
