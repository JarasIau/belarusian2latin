import re

def latinize(text):
    text = f'{text}'
    text = re.sub(r'(?<=[а-яіўёА-ЯІЎЁ])([СсЦц])([Кк])([Іі]|[Іі][МмЯяХхМі]|[Іі][Мм][Іі])\b', r'\1◊\2\3', text)
    iotated_vowels = { 'я': 'а', 'ё': 'о', 'ю': 'у', 'е': 'э', }
    for iotated, vowel in iotated_vowels.items():
        text = re.sub(rf'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ]){iotated}', rf'й{vowel}', text)
        text = re.sub(rf'(?<![бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ]){iotated.upper()}', rf'Й{vowel}', text)

    text = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])І', r'¤І', text)
    text = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])і', r'¤і', text)
    text = re.sub(r'\'І', r'ЙІ', text)
    text = re.sub(r'\'і', r'йі', text)
    text = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШ])і', r'¤і', text)
    for iotated, vowel in iotated_vowels.items():
        text = re.sub(rf'{iotated}', rf'¤{vowel}', text)
        text = re.sub(rf'{iotated.upper()}', rf'¤{vowel.upper()}', text)

    text = re.sub(r'[\']', r'', text)
    text = re.sub(r'[ьЬ]', r'¤', text)
    text = re.sub(r'Й', r'Й¤', text)
    text = re.sub(r'й', r'й¤', text)
    text = re.sub(r'Д[Зз]', r'Ð', text)
    text = re.sub(r'дз', r'ð', text)
    text = re.sub(r'дð', r'ðð', text)
    text = re.sub(r'Д[Ðð]', r'ÐÐ', text)
    text = re.sub(r'([СсЗзЦц])([бвджзлмнпрстфцчшБВДЖЗЛМНПРСТФЦЧШÐðйЙ]¤)', r'\1¤\2', text)
    text = re.sub(r'([Нн])([Нн]¤)', r'\1¤\2', text)
    text = re.sub(r'([Лл])([Лл]¤)', r'\1¤\2', text)
    text = re.sub(r'([СсЗзЦц])([бвджзлмнпрстфцчшБВДЖЗЛМНПРСТФЦЧШÐðйЙ]¤)', r'\1¤\2', text)
    text = re.sub(r'([Нн])([Нн]¤)', r'\1¤\2', text)
    text = re.sub(r'([Лл])([Лл]¤)', r'\1¤\2', text)
    text = re.sub(r'([СсЗзЦц])([бвджзлмнпрстфцчшБВДЖЗЛМНПРСТФЦЧШÐðйЙ]¤)', r'\1¤\2', text)
    text = re.sub(r'([Нн])([Нн]¤)', r'\1¤\2', text)
    text = re.sub(r'([Лл])([Лл]¤)', r'\1¤\2', text)
    text = re.sub(r'([СсЗзЦцÐð])([бвджзлмнпрстфцчшБВДЖЗЛМНПРСТФЦЧШÐðйЙ]¤)', r'\1¤\2', text)
    text = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðйЙ])¤І', r'І', text)
    text = re.sub(r'(?<=[бвгджзклмнпрстфхцчшБВГДЖЗКЛМНПРСТФХЦЧШÐðйЙ])¤і', r'і', text)
    palatalized_consonants = { 'л': 'ĺ', 'н': 'ń', 'с': 'ś', 'з': 'ź', 'ц': 'ć', 'ð': 'dź', }
    for cyrillic, latin in palatalized_consonants.items():
        text = re.sub(rf'{cyrillic}¤(?![аоэуыіАОЭУЫІ])', rf'{latin}', text)
        text = re.sub(rf'{cyrillic.upper()}¤(?![аоэуыіАОЭУЫІ])', rf'{latin.upper()}', text)

    text = re.sub(r'Й¤', r'Й', text)
    text = re.sub(r'й¤', r'й', text)
    cyrillic_to_latin = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'ж': 'ž', 'з': 'z',
        'і': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ў': 'ŭ', 'ф': 'f', 'х': 'ch', 'ц': 'c',
        'ч': 'č', 'ш': 'š', 'ы': 'y', 'э': 'e', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H',
        'Ґ': 'G', 'Д': 'D', 'Ж': 'Ž', 'З': 'Z', 'І': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L',
        'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ў': 'Ŭ', 'Ф': 'F', 'Х': 'Ch', 'Ц': 'C', 'Ч': 'Č', 'Ш': 'Š', 'Ы': 'Y', 'Э': 'E',
        'ð': 'dz', 'Ð': 'Dz',
    }
    for cyrillic, latin in cyrillic_to_latin.items():
        text = text.replace(cyrillic, latin)

    text = re.sub(r'¤', r'i', text)
    text = re.sub(r'◊', r'', text)
    return text
