visited = {'0,0'}

f = open('./03-input.txt', 'r')
x = 0
y = 0
def updateLocation(coor, char):
	if char == '<':
		coor[0]-=1
	if char == '^':
		coor[1]+=1
	if char == '>':
		coor[0]+=1
	if char == 'v':
		coor[1]-=1
	return coor

robot = [0,0]
santa = [0,0]
human = True
for char in f.read():
	newLocation = updateLocation(santa if human else robot, char)
	visited.add(str(newLocation[0])+','+str(newLocation[1]))
	human = not human
print(len(visited))