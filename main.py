import PySimpleGUI as sg

def create_window(theme):
		sg.theme(theme)
		sg.set_options(font = 'Franklin 14') #(6,3) means 6 character wide and 6 character height(NOT PIXELS).
		button_size = (4,3)
		layout = [
			[sg.Text("output", 
				font = 'Franklin 26', 
				justification = 'right', 
				expand_x = True, 
				pad = (10, 20),
				right_click_menu = theme_menu,
				key = "-TEXT-")
			#sg.Push(), sg.Text("output", font = 'Franklin 26') - making element stick to the right side with sg.Push() elemenet
			],
			[sg.Button("Clear", expand_x = True), sg.Button("Enter", expand_x = True)],
			[sg.Button("7", size = button_size), sg.Button("8", size = (6, 3)), sg.Button("9", size = button_size), sg.Button("*", size = button_size)],
			[sg.Button("4", size = button_size), sg.Button("5", size = (6, 3)), sg.Button("6", size = button_size), sg.Button("/", size = button_size)],
			[sg.Button("1", size = button_size), sg.Button("2", size = (6, 3)), sg.Button("3", size = button_size), sg.Button("-", size = button_size)],
			[sg.Button("0", expand_x = True, expand_y = True), sg.Button(".", size = (6, 3)), sg.Button("+", size = button_size)],
		]
		return sg.Window("Calculator", layout)
#sg.theme('dark') - set theme after creating elemetns(elements won't change their theme) 

theme_menu = ['menu', ['dark', 'LightGrey1', 'dark', 'DarkGray8', 'random']]
window = create_window('dark')
current_exp = ""
while True:
	event, value = window.read()
	if event == sg.WIN_CLOSED:
		break 
	if event in theme_menu[1]:
		window.close()
		window = create_window(event)
	if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+", "-", "*", "/"]:
		current_exp += event
		window["-TEXT-"].update(current_exp.split("+")[-1].split("*")[-1].split("/")[-1].split("-")[-1])
	if event in ["Enter"]:
		window["-TEXT-"].update(eval(current_exp))
		current_exp = ""
	if event in ["Clear"]:
		current_exp = ""
		window["-TEXT-"].update("")
window.close()