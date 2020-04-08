import click
import rows
from cprint import cprint

from babel.use_cases import chain_translate_text


TEXT = """
The Khaleefeh Hároon Er-Rasheed had gone forth this night to see and hear what news he could collect, accompanied by Jaạfar his Wezeer, and Mesroor his executioner. It was his custom to disguise himself in the attire of a merchant; and this night, as he went through the city, he happened to pass, with his attendants, by the house of these ladies, and hearing the sounds of the musical instruments, he said to Jaạfar, I have a desire to enter this house, and to see who is giving this concert. They are a party who have become intoxicated, replied Jaạfar, and I fear that we may experience some ill usage from them; but the Khaleefeh said, We must enter, and I would that thou devise some stratagem by which we may obtain admission to the inmates. Jaạfar therefore answered, I hear and obey: and he advanced, and knocked at the door; and when the portress came and opened the door, he said to her, My mistress, we are merchants from Tabareeyeh, and have been in Baghdád ten days; we have brought with us merchandise, and taken lodgings in a Khán; and a merchant invited us to an entertainment this night: accordingly, we went to his house, and he placed food before us, and we ate, and sat awhile drinking together, after which he gave us leave to depart; and going out in the dark, and being strangers, we missed our way to the Khán: we trust, therefore, in your generosity that you will admit us to pass the night in your house; by doing which you will obtain a reward in heaven.
""".strip()


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def from_idh_csv(filename):
    entries = rows.import_from_csv(filename)
    # lista de codes
    codes = [e.code.strip() for e in entries]
    #lista de language
    languages = [e.language.strip() for e in entries]

    codelang = remove_consecutives({'codes': codes, 'languages': languages})

    chain_str = ' - '.join(codes)
    cprint.ok(f"Translation chain: {chain_str}.")
    cprint.ok(f"Input text: {TEXT}\n")

    start_codelang = {'codes': 'en', 'languages': 'English'}
    text, result = chain_translate_text(TEXT, start_codelang, codelang, monitoring = True)

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
