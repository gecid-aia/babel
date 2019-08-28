from babel.use_cases import chain_translate_text

text = "Para ele, cada leitura de qualquer texto sempre proporcionará um novo redimensionamento e entendimento desse texto. Metaforicamente falando, ele se posiciona diante dos textos como o banhista do rio de Heráclito, no qual é impossível entrar duas vezes devido a seu curso estar em constante mutação."
languages = ['en', 'es', 'ja']
text, result = chain_translate_text(text, 'pt', languages)

print()
print(text)
print()
print(result)
