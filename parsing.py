import sys

fd = open(sys.argv[1], 'r')
img_ct = int(fd.readline())
rl = fd.readline()
while(rl):
	line = rl[0: len(rl) - 1].split(" ")
	rl = fd.readline()
