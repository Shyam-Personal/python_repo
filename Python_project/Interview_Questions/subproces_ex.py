import subprocess

proc = subprocess.Popen("dir1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
outs, errs = proc.communicate(timeout=15)
print("*** out **** \n", outs)
print("#### Error ###\n", errs)