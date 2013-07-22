#! /usr/bin/python

import random,commands,sys,time

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def create(num):
	while True:
		s = random.randint(1,num)
		l = random.randint(1,num)
		m = min([s,l])
		n = random.randint(1,m)
	
	
		if n % gcd(s,l) == 0:
			break	

#	command = "/home/elab/bin/water/water_jug.pl %d %d %d" % (s,l,n)
#	print commands.getoutput(command)

	return [s,l,n]

def look(obj, gallon, size):
	print "You look at a %s jug in the room.\nThis shiny %s jug appears to be a container made for holding water.\nA %s jug holds %d of %d gallons.\n" % (obj, obj, obj, gallon, size)

def look_inscription(gallon):
	print "You look at an inscription.\nIt reads:\nTo get to the next stage put %d gallons on the scale.\n" % (gallon)

def fill(obj, size):
	print "You fill a %s jug with %d gallons.\nA %s jug now has %d gallons.\n" % (obj, size, obj, size)
def empty(obj):
	print "You empty a %s jug.\n" % (obj)
def pour(src, dist, move, state):
	if state == "empty":
		print "You pour %d gallons into a %s jug from a %s jug.\nA %s jug is now empty.\n" % (move, dist, src, src)
	elif state == "fill":
		print "You pour %d  gallons into a %s jug from a %s jug.\nA %s jug is now full.\n" % (move, dist, src, dist)
def put_jug(obj):
	print "You put a %s jug onto a scale.\nThe scale balances perfectly and a door opens to the next room!\n" % (obj)

def problem(num):
	print "Room %d" % ( num + 1)
	problem = create(100)
	size = {"red":problem[0], "blue":problem[1]}
	scale = problem[2]
	jug = {"red":0, "blue":0}
	print "red:%s blue:%s scale:%s\n" % (problem[0], problem[1], problem[2])
	print "Please input a command.\ncommand:look,put,pour,fill,empty\n"
	sys.stdout.flush()
	
	while True:
		s = sys.stdin.readline()
		s = s.rstrip()
		s = s.split(" ")
	
		if s[0] == "look":
			if len(s) != 2:
				print "usage: look [jug,inscription]\n"
			elif s[1] == "red" or s[1] == "blue":
				look(s[1], jug[s[1]], size[s[1]])
			elif s[1] == "inscription":
				look_inscription(scale)
			else:
				print "usage: look [jug,inscription]\n"
		elif s[0] == "fill":
			if len(s) != 2:
				print "usage: fill [jug]\n"
			elif s[1] == "red" or s[1] == "blue":
				fill(s[1], size[s[1]])
				jug[s[1]] = size[s[1]]
			else:
				print "usage: fill [jug]\n"
		elif s[0] == "empty":
			if len(s) != 2:
				print "usage: empty [jug]\n"
			elif s[1] == "red" or s[1] == "blue":
				empty(s[1])
				jug[s[1]] = 0
			else:
				print "usage: empty [jug]\n"
		elif s[0] == "pour":
			if len(s) != 4:
				print "usage: pour [jug] into [jug]\n"
			elif s[1] == "red" or s[1] == "blue":
				if s[1] != s[3] and (s[3] == "red" or s[3] == "blue"):
					space = size[s[3]] - jug[s[3]]
					if space >= jug[s[1]]:
						pour(s[1], s[3], jug[s[1]], "empty")
						jug[s[3]] += jug[s[1]] 	
						jug[s[1]] = 0
					else:
						pour(s[1], s[3], space, "fill")
						jug[s[3]] = size[s[3]]
						jug[s[1]] -= space
			else:
				print "usage: pour [jug] into [jug]\n"
		elif s[0] == "put":
			if len(s) != 4:
				print "usage: put [jug] onto scale\n"
			elif (s[1] == "red" or s[1] == "blue") and s[2] == "onto" and s[3] == "scale":
				if scale == jug[s[1]]:
					put_jug(s[1])
					return True
				else:
					print "You have failed!\n"
					return False
			else:
				print "usage: put [jug] onto scale\n"
		elif s[0] == "exit":
			break
		else:
			print "Invalid\n"
						
	
		sys.stdout.flush()
	
print "\n"
print "You see a large room with sleek black walls on every side.  The ceiling overhead is smooth and devoid of features. In the center of the room is a small scale that links to a closed door.\nA small fountain is gurgling water in the corner. The scale has a small inscription on it.\nA red jug is sitting in the room.\nA blue jug is sitting in the room.\nA fountain is sitting in the room.\nA scale is sitting in the room.\n"

starttime = time.time()
for i in range(0,100):
	current = int(time.time() - starttime)
	print "time:%dsec" % (current)
	if current > 30:
		print "too slow..."
		sys.exit()
	elif problem(i):
		continue
	else:
		sys.exit()
print "Conglaturations!!!\n"
print "flag:Water is delicious."
sys.exit()
