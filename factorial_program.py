import ui
import math

def factorial(sender):
	user_input = int(view['number_input'].text)
	if user_input < 0:
		view['factorial_label'].text = '1'
	else:
		num = 1
		while user_input >= 1:
			num = num * user_input
			user_input = user_input - 1
			view['factorial_label'].text = str(num)
		
view = ui.load_view()
view.present('sheet')

