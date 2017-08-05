import sys

from output import linux_console
from key_log import linux_pyxhook
import complete
from dictionary import json_dictionary


class Stenocomplete:
    def run(self, dictionary_file_paths):
        platform = sys.platform
        if platform.startswith('linux'):
            console_writer = linux_console.ConsoleWriter()
            dictionary_reader = json_dictionary.DictionaryReader(
                dictionary_file_paths)
            completer = complete.Completer(dictionary_reader, console_writer)
            logger = linux_pyxhook.Logger(completer)
            logger.run()
        elif platform.startswith('cygwin') or platform.startswith('win'):
            raise OSError('windows is not yet supported, sorry')
        elif platform.startswith('darwin'):
            raise OSError('windows is not yet supported, sorry')
        else:
            raise OSError(platform + ' is not yet supported, sorry')


if __name__ == '__main__':
    Stenocomplete().run(sys.argv[1:])
