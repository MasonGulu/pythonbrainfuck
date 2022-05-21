#MIT License

#Copyright (c) 2022 Mason Gulu

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import sys

stack = []
sp = 0 # stack pointer
pc = 0 # program counter
returnstack = [] # stack of return addresses, 0 is most recent
instruction = """
>>>--------<,[<[>++++++++++<-]>>[<------>>-<+],]++>>++<--[<++[+>]>+<<+++<]<
<[>>+[[>>+<<-]<<]>>>>[[<<+>.>-]>>]<.<<<+<<-]>>[<.>--]>.>>."""

for x in range(0,3000000):
	stack.append(0)

def findclose(start): #find closing ], recursive
	while (instruction[start]) != ']':
		start += 1
		if (instruction[start] == '['):
			# We're going in another layer, call itself to find where that layer closes
			start = findclose(start+1)
	return start
	
def plus():
	stack[sp] += 1
	global pc
	pc += 1
	
def minus():
	stack[sp] -= 1
	global pc
	pc += 1

def left():
	global pc
	global sp
	sp -= 1
	pc += 1

def right():
	global pc
	global sp
	sp += 1
	pc += 1

def ioread():
	global pc
	global sp
	pc += 1
	stack[sp] = ord(input("INPUT CHAR: ")[0])

def iowrite():
	global pc
	global sp
	pc += 1
	sys.stdout.write(chr(stack[sp]))

def loopstart():
	global pc
	global sp
	if stack[sp] == 0:
		pc = findclose(pc)+1
	else:
		returnstack.insert(0, pc+1)
		pc += 1

def loopend():
	global pc
	global sp
	if stack[sp] == 0:
		pc += 1
		returnstack.pop(0)
	else:
		pc = returnstack[0]

instructions = {
	"+": plus,
	"-": minus,
	"<": left,
	">": right,
	",": ioread,
	".": iowrite,
	"[": loopstart,
	"]": loopend
}

def interpret():
	global pc
	char = instruction[pc]
	if True:
		print('['+str(pc)+']', char, '['+str(stack[sp-1])+','+str(stack[sp])+','+str(stack[sp+1])+']')
	if instructions.get(char, lambda:"Invalid")() == "Invalid":
		pc += 1
	
while (pc < len(instruction)):
	interpret()
	
# print(instructions.get("aa", lambda: "Invalid")()) # So as far as I can tell lambda is a function type, which just returns the string I give it
