from babel.pipeline import translation_steps

def chain_translate_text(text, start_language, translation_languages):
    steps = translation_steps(start_language, translation_languages)

    current_text = text
    for step in steps:
        current_text = step.translate(current_text)

    return text, current_text
