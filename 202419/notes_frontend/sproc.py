import subprocess
result=subprocess.run(['python3','-c',
                       'print(2**8)'],capture_output=True,text=True)
print(result.stdout)