from pwn import *
import os, sys
import traceback

ID = raw_input("Your input file(.PA3): ")[:-1] + ".PA3"
your_run_text = raw_input("Your output filename(.txt): ")[:-1] + ".txt"
run_file = ID
args = ['tcsh', run_file]

run_list = []

# run_listPA1
run_list.append(['e','w','l','x shovel','x trees','x tree','x palms','x palm','x coconuts','x coconut','i','get coconut','get shovel','i','l','e','l','x trees','e','x ground','dig','l','x card','x cpu','x board','get cpu','l','ne','ne','ne','sw','sw','se','x food','get food','se','x bear','x key','drop food','l','x bear','x key','get key','sw ','x emerald','x bracelet','get bracelet','i','ne','nw','nw','ne','ne','ne','n','e','x bins','x bin','get bin','w','w','e','w','x computer','x vax','x cabinet','x lights','x panel','x steady','put card in computer','e','w','l','quit'])

run_list.append(['climb tree', 'climb trees','climb palm','climb palms',
'xyz','x','get','drop','eat','climb','shake','put',
'x xyz','get xyz','drop xyz','eat xyz','shake xyz','climb xyz','put xyz',
'x key','get key','drop key','eat key','shake key','climb key','put key',
'put lamp','put lamp in','put lamp lamp','put lamp in lamp',
'x shovel','x lamp','x tree','x boulder','x xyz',
'get shovel','get boulder','get xyz','get lamp','get tree','take tree','drop lamp','throw shovel','l',
'shake hand','take lamp','shake','shake boulder','shake shovel','get shovel','i','shake lamp','shake shovel', 
'e','climb tree','climb boulder',
'e','dig','get cpu',
'se','get food',
'se','climb bear','drop food','get key',
'sw','get bracelet',
'ne','nw','nw','ne','ne',
'drop key','ne','get key','ne',
'w','put lamp','put lamp on vax','put lamp in shovel','put lamp on tree','put tree on lamp','put card','e','w','put card in vax','e','w','put card in vax','i','get card','l','quit'])
run_list.append(['quit'])
run_list.append(['get shovel dfff h 123', 'eat shovel'])
run_list.append(['e', 'e', 'se', 'se', 'shake bear'])
run_list.append(['e', 'e', 'se', 'x food', 'eat food', 'get food', 'eat food', 'eat lamp'])
run_list.append(['e','e','dig','get all','se','get food', 'se','sw','get emerald','ne','i','shake lamp', 'shake shovel', 'shake cpu','shake food','shake emerald','throw food','shake key','get key','i','shake key','se','eat key'])

c = 0

with open(your_run_text, 'w') as f:
	try:
		for i in range(len(run_list)):
			p = process(argv=args)
			msg = p.recvuntil('>')

			header = "\n------------ * Debug Type "+ str(i) +" * ------------\n"
			f.write(header)
			f.write(msg)
			L = len(run_list[i])

			for cmd_count in range(L):
				p.sendline(run_list[i][cmd_count])
				cmd = run_list[i][cmd_count] + '\n'
				if cmd_count == L-1 or cmd == 'quit\n':
					msg = p.recvuntil('points.')
				else:
					msg = p.recvuntil('>')
				f.write(cmd+msg)

			print("Write success!")
			c += 1
			p.close()
	except Exception as e:
		#print("Error: ", e)
		#error_class = e.__class__.__name__ # error type
		#detail = e.args[0] # detail error content
		#cl, exc, tb = sys.exc_info() # get Call Stack
		#lastCallStack = traceback.extract_tb(tb)[-1] # get last data of Call Stack
		#fileName = lastCallStack[0] # event filename
		#lineNum = lastCallStack[1] # error line no.
		#funcName = lastCallStack[2] # function name
		#errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
		#print(errMsg)
		
		print("Something wrong. \nWhen you run: ")
		print("\t\t" + cmd)
		print("Maybe you should debug and run again.")
	else:
		if c == len(run_list):
			print("\nRun success!")
			print("Now you can try this on your terminal: ")
			print("# diff -bwc " + your_run_text + ".txt ~/auto_debug_for_unix/debug.txt`")
