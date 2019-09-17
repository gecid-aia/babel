import click
import rows
from cprint import cprint

from babel.use_cases import chain_translate_text



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

    with open("datasets/1001_noites.txt", 'r') as fd:
        phrases = [l.strip() for l in fd.readlines() if l.strip()]
        for text in phrases:
            cprint.ok(f"Translation chain: {chain_str}.")
            cprint.ok(f"Input text: {text}\n")

            start_codelang = {'codes': 'pt', 'languages': 'Portuguese'}
            text, result = chain_translate_text(text, start_codelang, codelang, monitoring = False)

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
