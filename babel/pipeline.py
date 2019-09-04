from cprint import cprint

from babel.translation import from_google


def translation_steps(start_language, languages, two_way=True):
    if two_way:
        pipeline = [start_language] + languages + languages[-2::-1] + [start_language]
    else:
        pipeline = [start_language] + languages + [start_language]

    for i, language in enumerate(pipeline[:-1]):
        next_language = pipeline[i + 1]
        yield TranslationStep(language, next_language)


class TranslationStep:

    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, text):
        cprint.info(f"Step {self.from_lang} - {self.to_lang}")
        text = from_google(text, source=self.from_lang, target=self.to_lang)
        cprint.info(f'\t{text}\n')
        return text