#!/usr/bin/python

import socket
import time
import re
import commands
import sys,time
 
ADDRESS = ""
PORT = 12002

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))
 
# fetch data
data = s.recv(2048)
while True:
	print data
	water = []
	data = data.split("\n")
	size =""
	for line in data:
		print line
		if line.startswith("red"):
			print size
			size = line
			break
	data = size.split(" ")
	for line in data:
		water.append(line.split(":")[1])
	print water
	
	command = "./water_jug_solve.pl %s %s %s" % (water[0], water[1], water[2])
	print command
	command_list = commands.getoutput(command)
	command_list = command_list.split("\n")
	print command_list
	
	for command in command_list:
		command += "\n"
		print command
		s.send(command) 
		data = s.recv(2048)
		print data	 

#s.send("look red\n")
#data = s.recv(4096)
#print data
