import re, sys
# why do i make this
sys.excepthook = lambda exctype,exc,traceback : print("{}: {}".format(exctype.__name__,exc),file=sys.stderr)
code = open(sys.argv[1], "r+").read()
if re.findall("^(?:#\(lalalagrrrrrrrkaboom\)pffffzipcodeadressdenied<.+?, AUTHOR\([A-Z]+?\)> and then start; define start as this big thing past the colon: )",code):
	code = "".join(re.findall("((?:.|end\.)(?= and then ))",re.match("(?:#\(lalalagrrrrrrrkaboom\)pffffzipcodeadressdenied<.+?, AUTHOR\([A-Z]+?\)> and then start; define start as this big thing past the colon: )(.+)",code).group(1)))
else: raise SyntaxError("Invalid preamble")
# print(code)
# le copy from my list of esolang interpreters
i = 0
pointer = 0
cells = {}
while True:
	#print(code[i],end="")
	if pointer not in cells: cells[pointer] = 0
	if code[i].upper() == "+":
		cells[pointer]+=1
		cells[pointer]%=256
	elif code[i].upper() == "-":
		cells[pointer]-=1
		cells[pointer]%=256
	elif code[i].upper() == ">":
		pointer+=1
	elif code[i].upper() == "<":
		pointer-=1
	elif code[i].upper() == ".":
		print(chr(cells[pointer]),end="")
	elif code[i].upper() == ",":
		inputChar = sys.stdin.read(1)
		if inputChar != "":
			cells[pointer] = ord(inputChar)
	elif code[i].upper() == "[":
		if cells[pointer] == 0:
			count = 1
			while count > 0:
				i+=1
				if code[i].upper() == "[":
					count+=1
				elif code[i].upper() == "]":
					count-=1
	elif code[i].upper() == "]":
		if cells[pointer] != 0:
			count = -1
			while count < 0:
				i-=1
				if code[i].upper() == "[":
					count+=1
				elif code[i].upper() == "]":
					count-=1
	i+=1
	if i == len(code):
		break
# print(cells)
