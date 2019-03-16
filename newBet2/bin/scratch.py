import subprocess
file = open("testFile.txt", "r")
p = subprocess.Popen(('gedit',"testFile"))
p.wait()
print file("testFile").readlines()