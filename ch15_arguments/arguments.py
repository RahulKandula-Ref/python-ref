import argparse

parser = argparse.ArgumentParser(
    description="Parser to read a name into the program"
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="Provide the name"
)

parser.add_argument(
    "-a", "--age", metavar="age",
    required=True, help="Age too is mandatory"
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)