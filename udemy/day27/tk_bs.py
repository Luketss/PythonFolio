# tkinter faz parte do pacote padrão do Python. Para utilizá-lo basta usar o import
import tkinter

window = tkinter.Tk()
window.title('gui program')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Arroz com arroz de arroz", font=('Arial', 24))
my_label.pack()

window.mainloop()
