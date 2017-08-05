import collections


class Completer:
    def __init__(self, dictionary_reader, console_writer):
        self.translation_dict, self.trie = dictionary_reader.read()
        self.console_writer = console_writer
        self.current_input = ""
        self.case_insensitive = True

    def complete_letter(self, letter):
        self.current_input += letter.lower()
        self.complete()

    def complete_whitespace(self):
        if self.trie.keys(self.current_input):
            self.current_input += " "
        else:
            self.current_input = ""
        self.complete()

    def complete_backspace(self):
        self.current_input = self.current_input[:-1]
        self.complete()

    def complete(self):
        # remove first word if word sequence not found
        while not self.trie.keys(
                self.current_input) and " " in self.current_input:
            self.current_input = self.current_input.split(' ', 1)[1]

        keys = list(set(self.trie.keys(self.current_input)))

        keys.sort(key=len, reverse=True)

        if len(self.current_input) > 1:
            dictionary = collections.OrderedDict()
            for key in keys:
                for translation in self.trie[key]:
                    decoded_translation = translation.decode("utf-8")
                    translations = self.translation_dict[decoded_translation]
                    translations.sort(key=len)
                    dictionary[decoded_translation] = translations
            self.console_writer.write(dictionary)
