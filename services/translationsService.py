import os
import polib
import config.conf as conf

class Localization:
    def __init__(self, lang=conf.lang):
        self.lang = lang
        self.translations = self.load_translations()

    def load_translations(self):
        file_path = os.path.join('locales', f'{self.lang}.po')
        return polib.pofile(file_path)

    def get(self, key):
        entry = self.translations.find(key)
        return entry.msgstr if entry else key

localization = Localization()
