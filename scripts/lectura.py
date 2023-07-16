
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Sacar la longitud media de los pares de oraciones y división del dataset en oraciones largas o cortas
data = []
with open('Bicleaner AI/Full/Paracrawl.en-es.full.classified', 'r', encoding='utf-8') as file:
    for line in file:
        columns = line.strip().split('\t')
        
        if len(columns) == 3:
            en = columns[0]
            es = columns[1]
            prob = columns[2]
            
            length = (len(en) + len(es)) / 2
            
            data.append([prob, en, es, length])

df = pd.DataFrame(data, columns=['prob', 'en', 'es', 'length'])
mean_length = df['length'].mean()

unique_lengths = sorted(df['length'].unique())
plt.hist(df['length'], bins=unique_lengths)
plt.axvline(mean_length, color='red', linestyle='--', linewidth=2, label='Media')
plt.legend()
plt.xlabel('Longitud de las oraciones')
plt.ylabel('Frecuencia')
plt.title('Histograma de longitud de oraciones')
plt.show()

short = []
large = []
for index, row in df.iterrows():
    item = str(row['prob']) + '\t' + str(row['en']) + '\t' + str(row['es'])
    if  row['length'] <= mean_length:
        short.append(item)
    else:

        large.append(item)

with open('Bicleaner AI/Full/Paracrawl.AIFull.shortPhrases.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(short))

with open('Bicleaner AI/Full/Paracrawl.AIFull.largePhrases.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(large))

#Último filtrado con el umbral 0.5/0.7 y obtención de fichero con el par de oraciones que no superan el umbral
data = []
with open('Bicleaner AI/Full/Paracrawl.AIFull.largePhrases.txt', 'r', encoding='utf-8') as file:
    for line in file:
        columns = line.strip().split('\t')
        
        if len(columns) == 3:
            prob = columns[0]
            en = columns[1]
            es = columns[2]
            data.append([prob, en, es])

df = pd.DataFrame(data, columns=['prob', 'en', 'es'])
input = []
for index, s in df['prob'].iteritems(): # type: ignore

    try:
        valor = float(s)
        if valor >= 0.5:
            item = str(s) + '\t' + df['en'][index] + '\t' + df['es'][index]
            input.append(item)
    except ValueError:
        pass 

with open('Bicleaner AI/Full/Paracrawl.AIFull.largePhrases.threshold05.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(input))













        

