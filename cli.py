import click
import rows
from cprint import cprint

from babel.use_cases import chain_translate_text


TEXT = """
Para ele, cada leitura de qualquer texto sempre proporcionará um novo redimensionamento e entendimento desse texto. Metaforicamente falando, ele se posiciona diante dos textos como o banhista do rio de Heráclito, no qual é impossível entrar duas vezes devido a seu curso estar em constante mutação.
""".strip()


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def from_idh_csv(filename):
    entries = rows.import_from_csv(filename)
    # lista de codes
    codes = [e.code.strip() for e in sorted(entries, key=lambda x: x.idh, reverse=True)]
    #lista de language
    languages = [e.language.strip() for e in sorted(entries, key=lambda x: x.idh, reverse=True)]

    codelang = remove_consecutives({'codes': codes, 'languages': languages})

    chain_str = ' - '.join(codes)
    cprint.ok(f"Translation chain: {chain_str}.")
    cprint.ok(f"Input text: {TEXT}\n")

    start_codelang = {'codes': 'pt', 'languages': 'Portuguese'}
    text, result = chain_translate_text(TEXT, start_codelang, codelang, monitoring = False)

    cprint.ok("\n##### RESULTS ######\n")
    cprint.ok(text)
    print()
    cprint.ok(result)

def remove_consecutives(codelang):
    new_codelang = {'codes': [], 'languages': []}
    codes = codelang['codes']
    langs = codelang['languages']
    
    last = 0
    new_codelang['codes'].append(codes[0])
    new_codelang['languages'].append(langs[0])
    for i in range(1, len(codes)):
        if codes[i] == new_codelang['codes'][last]:
            continue
        else:
            new_codelang['codes'].append(codes[i])
            new_codelang['languages'].append(langs[i])
            last += 1
    return new_codelang

if __name__ == '__main__':
    from_idh_csv()
