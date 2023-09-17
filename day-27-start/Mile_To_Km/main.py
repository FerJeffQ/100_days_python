from  tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to Km")
window.minsize(width=200, height=100)

value = 0

def mile_to_km():
    value = float(input.get())
    new_text = str(value * 1.609344)
    label_result.config(text=new_text)



label_info_1 = Label(text="is equal to")
label_info_1.grid(column=0,row=2)

label_info_2 = Label(text="Miles")
label_info_2.grid(column=3,row=0)

label_info_3 = Label(text="Km")
label_info_3.grid(column=3,row=1)

label_result = Label(text=f"{value}")
label_result.grid(column=2,row=2)

#Button
button = Button(text="Calculate",command=mile_to_km)
button.grid(column=2,row=3)

#Entry
input = Entry(width=10)

input.grid(column=2, row=0)
















window.mainloop()



