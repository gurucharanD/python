# myfile = open('myfile.txt')
# print(myfile.read())
# print(myfile.read())
# myfile.seek(0)
# print(myfile.read())
# myfile.seek(0)
# print(myfile.readlines())


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
