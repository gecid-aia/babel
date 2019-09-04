from babel.pipeline import translation_steps
from babel.json_monitoring import TranslationHistory
from cprint import cprint

def chain_translate_text(text, start_language, translation_languages, monitoring = False):
    steps = translation_steps(start_language, translation_languages)
    
    if monitoring:
    	step_history = TranslationHistory()
    	cprint.info(f"##### MONITORAMENTO ATIVO ######\n")

    current_text = text
    for step in steps:
        temp = step.translate(current_text)
        if monitoring:
        	step_history.add_marker(text_origin = current_text, code = step.from_lang)
       	current_text = temp

    if monitoring:
    	step_history.to_json('test.json')

    return text, current_text
