from tkinter import Frame, Entry, Button, StringVar
from button import CalcButton

class Calculator:
	def __init__(self, root):
		self.root = root
		self.root.title("Calculadora")
		self.root.config(bg="black")

		frame = Frame()
		frame.pack()
		frame.config(width=350, height=350, bg="black")
		input_num = StringVar()

		Entry(frame, textvariable=input_num, width=23, justify="right").grid(row=0, column=0, padx=10, pady=10, columnspan=6)

		CalcButton(frame, input_num)