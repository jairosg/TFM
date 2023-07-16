import random

random.seed(2023)

# Dividir los datos de test en oraciones en español e inglés
data_es = []
data_en = []
with open('Bicleaner AI/Full/Paracrawl.AIFull.shortPhrases.threshold05_shuffled.txt', 'r', encoding='utf-8') as file:
    for line in file:
        columns = line.strip().split('\t')
        
        if len(columns) == 3:
            en = columns[1]
            es = columns[2]

            data_es.append(es)
            data_en.append(en)

with open('Data test/Full/prueba.short05.test.en', 'w', encoding='utf-8') as file:
    for s in data_en:
        file.writelines(s + "\n")

with open('Data test/Full/prueba.short05.test.es', 'w', encoding='utf-8') as file:
    for s in data_es:
        file.writelines(s + "\n")

# Generar datos de test a partir de la semilla
"""
with open('first_tus/XLEnt.en-es.en', 'r', encoding='utf-8') as file:
    data_en = file.readlines()

with open('first_tus/XLEnt.en-es.es', 'r', encoding='utf-8') as file:
    data_es = file.readlines()


index = random.sample(range(len(data_en)), 100000)
choosen_lines = [data_en[i] for i in index]
choosen_lines_es = [data_es[i] for i in index]


random.shuffle(data_es)
choosen_lines = data_en[:100000]
choosen_lines_es = data_es[:100000]


with open('first_tus/XLEnt100k.en-es.en', 'w', encoding='utf-8') as file:
    file.writelines(choosen_lines)

with open('first_tus/XLEnt100k.en-es.es', 'w', encoding='utf-8') as file:
    file.writelines(choosen_lines_es)
"""