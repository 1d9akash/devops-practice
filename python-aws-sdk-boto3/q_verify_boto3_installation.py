import subprocess
pkg = "boto3"
result = subprocess.run(["pip", "show", pkg], capture_output=True, text=True)
if result.returncode == 0:
    print('"boto3 is installed!"')
else:
    print('Please install boto3 using "pip install boto3"')