import argparse

# Create a parser
parser = argparse.ArgumentParser(description='My script')

# Add arguments
# The add_argument() function is used to specify what command-line arguments the script is expecting.
# The first add_argument below specifies a required positional argument 'name'.
# The 'help' parameter provides a description for the argument, which will show up if the user runs the script with --help.
parser.add_argument('name', help='Your name')

# The second add_argument defines an optional argument '--age'.
# The 'type=int' ensures the value passed is treated as an integer.
# The 'default=25' means that if the user does not provide '--age', it will default to 25.
# The 'help' parameter explains what this argument means.
parser.add_argument('--age', type=int, default=25, help='Your age')

# Parse the arguments
args = parser.parse_args()

# Use them
print(f"Hello {args.name}, you are {args.age} years old")
print(args)