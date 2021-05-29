from tkinter import Tk, Frame, Entry, Button, StringVar

class Calculator:
	def __init__(self, root):
		self.root = root
		self.root.title("Calculadora")
		self.root.config(bg="black")
                self.root.resizable(width=False, height=False)
		
		frame = Frame()
		frame.pack()
		frame.config(width=350, height=350, bg="black")
		input_num = StringVar()

		Entry(frame, textvariable=input_num, width=23, justify="right").grid(row=0, column=0, padx=10, pady=10, columnspan=6)

		buttons = Calculator_buttons(frame, input_num)


class Calculator_buttons:
	def __init__(self, frame, input_num):
		self.frame = frame
		self.input_num = input_num

		#--------------first row---------------
		#button delete
		Button(self.frame, text="c", bg="#ff0000", width=1, command=self.delete_all_input).grid(row=4, column=5, padx=5, pady=5)

		#button 7
		#se utiliza lambda para que el flujo del programa no lo tome como una llamada a la función automáticamente, sino que espere a la acción de presionar el botón
		Button(self.frame, text="7", bg="#e65c00", width=1, command=lambda:self.send_info("7")).grid(row=1, column=1, padx=5, pady=5)

		#button 8
		Button(self.frame, text="8", bg="#e65c00", width=1, command=lambda:self.send_info("8")).grid(row=1, column=2, padx=5, pady=5)

		#button 9
		Button(self.frame, text="9", bg="#e65c00", width=1, command=lambda:self.send_info("9")).grid(row=1, column=3, padx=5, pady=5)

		#button product
		Button(self.frame, text="x", bg="#005ce6", width=1, command=lambda:self.send_info("*")).grid(row=1, column=4, padx=5, pady=5)

		#----------------second row------------------
		#button 4
		Button(self.frame, text="4", bg="#e65c00", width=1, command=lambda:self.send_info("4")).grid(row=2, column=1, padx=5, pady=5)

		#button 5
		Button(self.frame, text="5", bg="#e65c00", width=1, command=lambda:self.send_info("5")).grid(row=2, column=2, padx=5, pady=5)

		#button 6
		Button(self.frame, text="6", bg="#e65c00", width=1, command=lambda:self.send_info("6")).grid(row=2, column=3, padx=5, pady=5)

		#button substract
		Button(self.frame, text="-", bg="#005ce6", width=1, command=lambda:self.send_info("-")).grid(row=2, column=4, padx=5, pady=5)

		#-------------third row--------------
		#button 1
		Button(self.frame, text="1", bg="#e65c00", width=1, command=lambda:self.send_info("1")).grid(row=3, column=1, padx=5, pady=5)

		#button 2
		Button(self.frame, text="2", bg="#e65c00", width=1, command=lambda:self.send_info("2")).grid(row=3, column=2, padx=5, pady=5)

		#button 3
		Button(self.frame, text="3", bg="#e65c00", width=1, command=lambda:self.send_info("3")).grid(row=3, column=3, padx=5, pady=5)

		#button div
		Button(self.frame, text="/", bg="#005ce6", width=1, command=lambda:self.send_info("/")).grid(row=3, column=4, padx=5, pady=5)

		Button(self.frame, text="ac", bg="#ff0000", width=1, command=self.delete_one_char).grid(row=3, column=5, padx=5, pady=5)

		#--------------fourth row------------
		#button zero
		Button(self.frame, text="0", bg="#e65c00", width=1, command=lambda:self.send_info("0")).grid(row=4, column=1, padx=5, pady=5)

		#button dot
		Button(self.frame, text=".", bg="#a3a375", width=1, command=lambda:self.send_info(".")).grid(row=4, column=2, padx=5, pady=5)

		#button equal
		Button(self.frame, text="=", bg="#005ce6", width=1, command=self.total_expression_math).grid(row=4, column=3, padx=5, pady=5)

		#button add
		Button(self.frame, text="+", bg="#005ce6", width=1, command=lambda:self.send_info("+")).grid(row=4, column=4, padx=5, pady=5)


	def send_info(self, alphanum):
		#toma lo que haya en el entry (.get) y lo suma a lo que ya estaba
		#.set: le asigna un valor al entry
		self.input_num.set(self.input_num.get() + alphanum)


	def delete_all_input(self):
		#borrar todo el texto del entry, pasado en los parámetros del método delete,
		#es decir desde el índice cero hasta lo que haya
		self.input_num.set("")


	def delete_one_char(self):
		#muestra solamente lo que se encuentra en el entry menos el último cáracter
		self.input_num.set(self.input_num.get()[:-1])


	def total_expression_math(self):
		try:
			expression_math = eval(self.input_num.get())
			self.delete_all_input()
			self.input_num.set(expression_math)

		except:
			self.input_num.set("Error")


root = Tk()
main_program = Calculator(root)

root.mainloop()
