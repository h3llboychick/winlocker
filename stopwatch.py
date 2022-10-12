import PySimpleGUI as sg
from time import time

sg.theme('black')
def create_window():
	layout = [
		[sg.Push(), sg.Image('cross.png', pad = 0, key = '-CLOSE-', enable_events = True)], #use enable_events = True to enable onclick communication with widget
		[sg.VPush()],
		[sg.Text('0.0', font = 'Young 50', key = "-TIME-")],
		[
			sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = "-STARTSTOP-"), 
			sg.Button('Lap', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = "-LAP-", visible = False)
		],
		[sg.Column([[]], key = '-LAPS-')],
		[sg.VPush()]
	]

	window = sg.Window("Stopwatch", layout, size = (300, 300), no_titlebar = False, element_justification = 'center')
	return window

window = create_window()
start_time = 0
active = False
lap_amount = 1
while True:
	event, values = window.read(timeout = 10) #timeout in milisecond. sets the frequency of updating cycle.

	if event in (sg.WIN_CLOSED, '-CLOSE-'):
		break
	if event == '-STARTSTOP-':
		if active:
			active = False
			start_time = 0
			window["-TIME-"].update("0.0")
			window['-STARTSTOP-'].update(text = 'Start')
			window["-LAP-"].update(visible = False)
			window.close()
			window = create_window()
			lap_amount = 1
		else:
			start_time = time()
			active = True
			window['-STARTSTOP-'].update(text = 'Stop')
			window["-LAP-"].update(visible = True)
	if active:
		elapsed_time = round(time() - start_time, 1)
		window['-TIME-'].update(elapsed_time)
	if event == '-LAP-' and active:
		window.extend_layout(window["-LAPS-"], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(round(time() - start_time, 1))]])
		print(window["-LAPS-"].layout)
		lap_amount += 1
window.close()