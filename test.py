from gpiozero import Button
buttonPlus = Button(20)

buttonPlus.wait_for_press()
vraag_welkestand = vraag_welkestand + 1
print("button was pressed")
