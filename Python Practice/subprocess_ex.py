import subprocess 

def execute(cmd):
	p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print(p.stdout.read())
	
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	outs, errs = proc.communicate(timeout=15)
	print("*** out **** \n", outs)
	print("#### Error ###\n", errs)
	
def main():
	cmd = "dir"
	execute(cmd)
	print()
	cmd = "dir1"
	execute(cmd)
	
if __name__ == "__main__":
	main()