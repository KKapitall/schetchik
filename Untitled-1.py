from pynput import keyboard

sum_of_codes = 0

def on_release(key):
    global sum_of_codes
    print(f'{key} released')
    try:
        sum_of_codes += ord(key.char)
    except AttributeError:
        print("клавиша не имееет числового значения")
    if key == keyboard.Key.esc:
        print("Сумма кодов всех нажатых клавиш:", sum_of_codes)
        return False

with keyboard.Listener(on_press=on_release) as listener:
    listener.join()