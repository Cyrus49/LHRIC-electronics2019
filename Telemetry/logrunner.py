import subprocess
while(True):
    out = subprocess.Popen(['python3','logger.py'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    print("IN RUNNER")
    print(stdout.decode("utf-8"))
    f = open("log3.log", "a")

    f.write(stdout.decode("utf-8"))

    f.close()