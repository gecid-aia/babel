from cprint import cprint

from babel.translation import from_google


def translation_steps(start_codelang, codelang, two_way=True):
    pipeline = {}
    if two_way:
        pipeline['codes'] = [start_codelang['codes']] + codelang['codes'] + codelang['codes'][-2::-1] + [start_codelang['codes']]
        pipeline['languages'] = [start_codelang['languages']] + codelang['languages'] + codelang['languages'][-2::-1] + [start_codelang['languages']]
    else:
        pipeline['codes'] = [start_codelang['code']] + codelang['codes'] + [start_codelang['codes']]
        pipeline['languages'] = [start_codelang['languages']] + codelang['languages'] + [start_codelang['languages']]

    for i, code in enumerate(pipeline['codes'][:-1]):
        size = len(pipeline['codes'])
        next_code = pipeline['codes'][i + 1]
        lang = pipeline['languages'][i]
        next_lang = pipeline['languages'][i + 1]
        yield TranslationStep(code, next_code, lang, next_lang, it = i + 1, size = size - 1)


class TranslationStep:

    def __init__(self, from_code, to_code, from_lang, to_lang, it, size):
        self.iteration = it
        self.size = size
        self.from_code = from_code
        self.to_code = to_code
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, text):
        cprint.info(f"Step {self.iteration}/{self.size}\n>> {self.from_lang} - {self.to_lang}")
        text = from_google(text, source=self.from_code, target=self.to_code)
        cprint.info(f'\t{text}\n')
        return text