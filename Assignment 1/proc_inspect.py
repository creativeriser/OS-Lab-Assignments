pid = input("Enter PID: ")

status_file = f"/proc/{pid}/status"
exe_file = f"/proc/{pid}/exe"
fd_path = f"/proc/{pid}/fd"

with open(status_file) as f:
    lines = f.readlines()
    for line in lines[:10]:
        print(line.strip())

print("Executable Path:", exe_file)
print("Open FDs:", fd_path)
