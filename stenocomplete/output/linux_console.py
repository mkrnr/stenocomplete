import os
import re
import shutil
import atexit


class ConsoleWriter():
    def __init__(self):
        os.system("setterm -cursor off")

    def write(self, dictionary):
        num_columns, num_rows = shutil.get_terminal_size((80, 20))

        os.system('clear')
        print('\033[3J', end="")

        current_suggestions = ""

        # calculate max key length
        max_key_length = 0
        for key in dictionary:
            key_length = len(key)
            if key_length > max_key_length:
                max_key_length = key_length

        for key in dictionary:
            line = add_spaces(key, max_key_length)

            # TODO add parameter for this one?
            # if key == self.current_input:
            #     continue

            separator_space = "    "
            for translation in dictionary[key]:
                if len(line) + len(translation) + len(
                        separator_space) > num_columns:
                    current_suggestions += line + "\n"
                    line = add_spaces("", max_key_length)
                    line += separator_space
                line += separator_space
                line += translation
            current_suggestions += line + "\n"
        if not current_suggestions:
            num_suggestion_lines = 0
        else:
            num_suggestion_lines = len(current_suggestions.split("\n"))

        num_empty_lines_above = 0
        if num_suggestion_lines > 0 and num_suggestion_lines <= num_rows:
            num_empty_lines_above = num_rows - num_suggestion_lines + 1

        for _ in range(0, num_empty_lines_above):
            current_suggestions = "\n" + current_suggestions

        if dictionary:
            current_suggestions = re.sub("\n$", "", current_suggestions)

        print(current_suggestions, end="\r")


def add_spaces(line, max_key_length):
    while len(line) < max_key_length:
        line += " "
    return line


@atexit.register
def reset_console():
    os.system('setterm -cursor on')
