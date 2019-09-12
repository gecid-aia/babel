from babel.pipeline import translation_steps
from babel.json_monitoring import TranslationHistory
from cprint import cprint

def chain_translate_text(text, start_codelang, translation_codelangs, monitoring = False):
    steps = translation_steps(start_codelang, translation_codelangs)
    
    if monitoring:
    	step_history = TranslationHistory()
    	cprint.info(f"##### MONITORING ######\n")

    current_text = text
    for step in steps:
        if monitoring:
            step_history.add_marker(text_origin = current_text, code = step.from_code, language = step.from_lang)
        current_text = step.translate(current_text)

    if monitoring:
    	step_history.to_json('output.json')

    return text, current_text
