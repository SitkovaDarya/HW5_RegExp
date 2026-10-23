import os
import shutil
import re

def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    for filename in os.listdir(dir):
        if not os.path.isfile(os.path.join(dir, filename)) or '.ipynb_checkpoints' in filename:
            continue
            
        new_name = filename
        
        if new_pattern:
            new_name = re.sub(pattern, new_pattern, new_name)
            
        if sample_names:
            for old_sample, new_sample in sample_names.items():
                new_name = new_name.replace(old_sample, new_sample)
                
        old_path = os.path.join(dir, filename)
        new_path = os.path.join(dir, new_name)
        
        if old_path != new_path:
            if to_replace:
                os.rename(old_path, new_path)
            else:
                shutil.copy2(old_path, new_path)


def get_chords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    chords = re.findall(r'\b[A-G][#b]?(?:m|maj|min|dim|aug)?\d*\b', text)
    return set(chords)


def salty_language(text):
    def translate_word(match):
        word = match.group(0)
        vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"     
        if word[0] in vowels:
            return word + "с" + word[0].lower() + "й"
        else:
            return word[1:] + word[0].lower() + "ай"
    result = re.sub(r'[А-Яа-яЁё]+', translate_word, text)
    return result