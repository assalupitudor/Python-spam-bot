# By Vedant Jhaveri
from pynput.keyboard import Key, Controller
import time
import urllib.request

keyboard = Controller()

# count the number of lines in the no line spacing txt file
def count_lines(file='no_line_script.txt'):
    with open(file, 'r') as file:
        for index, line in enumerate(file):
            pass
    file.close()
    return index + 1

# remove line spacing
def remove_lines(original='to_send.txt', empty='no_line_script.txt'):
    script = open(original, 'r')
    empty_script = open(empty, 'w')
    # remove spaces between lines
    script_length = count_lines(original)
    for i in range(script_length):
        line = script.readline()
        if line.replace(" ", "") not in ['\n', '\r\n']:
            empty_script.write(line)

def destroy_chat():
    lines = []
    # opening the text file
    with open('no_line_script.txt', 'r') as file:
        # reading each line
        for line in file:
            # reading each word and adding to the end of the list
            for word in line.split():
                lines.append(word)

    # delay between each message in seconds
    delay = float(input('Delay between each message: '))
    time.sleep(3)
    for line in lines:
        for char in line:
            keyboard.press(char)
            keyboard.release(char)
        # Sleep might be necessary for certain applications
        # time.sleep(0.03)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(delay)


if __name__ == '__main__':
    remove_lines()
    destroy_chat()
