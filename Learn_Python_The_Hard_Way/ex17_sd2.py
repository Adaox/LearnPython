from sys import argv
from os.path import exists

script, from_file, to_file = argv

# .close() isn't needed as python will close for us upon terminating the script
open(to_file, "w").write(open(from_file).read())
