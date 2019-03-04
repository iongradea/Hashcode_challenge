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
	##print(x_list)

def calc_i(a, b):
	tot = a['tags'].copy()
	tot.extend(b['tags'])
	tot = list(set(tot))
	lst = []
	lst = list(set(a['tags']).intersection(b['tags']))
	x_i = len(lst)
	b_i = len(list(set(tot) - set(a['tags'])))
	a_i = len(list(set(tot) - set(b['tags'])))
	return (min(x_i, a_i, b_i))

def calc_slide(end_list):
	slides = []
	while (len(end_list) > 0):
		i = 0
		fact_i_max = 0
		i_max = 1
		while (i < len(end_list)):
			if (calc_i(end_list[0], end_list[i]) > fact_i_max):
				fact_i_max = calc_i(end_list[0], end_list[i])
				i_max = i
			i += 1
		if (len(end_list) == 1):
			first = end_list.pop(0)
			slides.append(first)
		else:
			second = end_list.pop(i_max)
			first = end_list.pop(0)
			slides.append(first)
			slides.append(second)
	return (slides)

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
	print("LOL")
print("LOL2")
create_v_2_x()
end_list = h_list.copy()
end_list.extend(x_list)
end_list = sorted(end_list, key=lambda k: int(k['nb']), reverse=True)
slides = calc_slide(end_list)

print(len(slides))
for i in slides:
	line = str(i['id1'])
	if (i['id2']):
		line += " "
		line += str(i['id1'])
	print(line)
