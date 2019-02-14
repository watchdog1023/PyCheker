import sys
filename = sys.argv[1]
source = open(filename, 'r').read() + '\n'
exe = compile(source, filename, 'exec')
exec(exe)