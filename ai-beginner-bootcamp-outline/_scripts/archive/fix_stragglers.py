import json

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb['cells']:
        new_source = []
        for line in cell['source']:
            line = line.replace('with the google_search tool', 'with the search_wikipedia tool')
            line = line.replace('Use the google_search tool', 'Use the search_wikipedia tool')
            new_source.append(line)
        cell['source'] = new_source
        
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)

fix_file('day_2/Day_2_Notebook.ipynb')
fix_file('day_4/Day_4_Notebook.ipynb')
