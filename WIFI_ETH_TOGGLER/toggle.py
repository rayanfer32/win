import subprocess

def getDeviceState(device="Ethernet"):
	_getCmd = f"netsh interface show interface name=\"{device}\""
	_out = subprocess.check_output(_getCmd, shell= True).decode().split()
	return _out

def isDeviceEnabled(device="Ethernet"):
	# return true if enabled
	if getDeviceState(device)[5] == "Enabled":
		return True
	return False

def setDeviceState(device="Ethernet", state="enabled"):
	states = ["enabled", "disabled"]
	_setCmd = f"netsh interface set interface name=\"{device}\" admin={state}"
	print(f"{state[:-2]}ing -- {device}")
	subprocess.run(_setCmd, shell=True)

def toggleDeviceState(device):
	if isDeviceEnabled(device):
		setDeviceState(device, state="disabled")
	else:
		setDeviceState(device,state="enabled")

toggleDeviceState("Ethernet")
toggleDeviceState("Wi-Fi")