import subprocess
subprocess.run(["touch", "test.txt"])
subprocess.run(["ls"])
subprocess.run(["rm", "test.txt"])
print("---------------")
subprocess.run(["ls"])
print("end")
