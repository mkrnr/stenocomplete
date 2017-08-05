import json
import marisa_trie


class DictionaryReader:
    def __init__(self, dictionary_file_paths):
        self.dictionary_file_paths = dictionary_file_paths

    def read(self):
        translations = []
        lower_translations = []

        # translation to stroke dict
        translation_stroke_dict = {}

        for dictionary_file_path in self.dictionary_file_paths:
            with open(dictionary_file_path) as dictionary_file:
                dictionary_json = json.load(dictionary_file)
                for stroke in dictionary_json:
                    translation = dictionary_json[stroke]
                    translation = translation.replace("{", "").replace("}", "")

                    lower_translation = translation.lower()

                    strokes = []
                    if translation not in translation_stroke_dict:
                        translation_stroke_dict[translation] = strokes
                    else:
                        strokes = translation_stroke_dict[translation]
                    strokes.append(stroke)

                    translations.append(bytes(translation, "utf-8"))
                    lower_translations.append(lower_translation)
        # lower case translation to translation trie for fast completion
        trie = marisa_trie.BytesTrie(zip(lower_translations, translations))
        return translation_stroke_dict, trie
