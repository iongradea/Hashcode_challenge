import sys

img_list = []
v_list = []
h_list = []
x_list = []
end_list = []
slide_list = []




def create_v_2_x():
	i = 0
	tab = []
	while (i < len(v_list) - 1):
		tab = v_list[i]['tags'].copy()
		tab.extend(v_list[i + 1]['tags'])
		tab = list(set(tab))
		obj = {'id1': v_list[i]['id1'], 'id2': v_list[i + 1]['id1'], 'fmt': 'X', 'nb': len(tab), 'tags': tab}
		x_list.append(obj)
		i += 2
	print(x_list)

fd = open(sys.argv[1], 'r')
img_ct = int(fd.readline())
rl = fd.readline()
i = 0
while(rl):
	line = rl[0: len(rl) - 1].split(" ")
	if (line[0] == 'V'):
		v_list.append({'id1': i, 'id2': None, 'fmt': line[0], 'nb': line[1], 'tags': line[2:]})
	elif (line[0] == 'H'):
		h_list.append({'id1': i, 'id2': None, 'fmt': line[0], 'nb': line[1], 'tags': line[2:]})
	rl = fd.readline()
	i += 1
create_v_2_x()
end_list = h_list.copy()
end_list.extend(x_list)
print(end_list)
end_list = sorted(end_list, key=lambda k: int(k['nb']), reverse=True)
print(end_list)

def create_vertical_slide():
	pass

def calc_i(slide_a, slide_b):
	pass



def calc_score(slide_list):
	pass
