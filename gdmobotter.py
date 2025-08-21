from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

print("Starte in 5 Sekunden...")
time.sleep(5)

last_mana_time = time.time()

try:
    while True:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)

        keyboard.press('1')
        keyboard.release('1')
        time.sleep(2)

        if time.time() - last_mana_time >= 100:
            keyboard.press('7')
            keyboard.release('7')
            last_mana_time = time.time()
except KeyboardInterrupt:
    print("Gestoppt.")

# bot von m0nky

