import pandas as pd
import matplotlib.pyplot as plt

data_pc = []
with open('Bicleaner AI/Paracrawl.en-es.classifiedAI', 'r', encoding='utf-8') as file:
    for line in file:
        columns = line.strip().split('\t')
        
        if len(columns) == 3:
            en = columns[0]
            es = columns[1]
            prob = columns[2]
            data_pc.append([prob, en, es])

data_xl= []
with open('Bicleaner AI/Lite/XLEnt.classifiedAI', 'r', encoding='utf-8') as file:
    for line in file:
        columns = line.strip().split('\t')
        
        if len(columns) == 3:
            en = columns[0]
            es = columns[1]
            prob = columns[2]
            data_xl.append([prob, en, es])


df_pc= pd.DataFrame(data_pc, columns=['prob', 'en', 'es'])
df_xl= pd.DataFrame(data_xl, columns=['prob', 'en', 'es'])

threshold = [0.1,0.2,0.3,0.4,0.5, 0.6, 0.7, 0.8, 0.9]
items_pc = []
items_xl = []

glob_pc = []
glob_xl = []

items_pc = []
items_xl = []
    
for t in threshold:
    cont = 0
    for index, s in df_pc['prob'].iteritems():
        if isinstance(s, str):
            if len(s)<=5:
                s = float(s)
                if s < t:
                    cont += 1
        elif s < t:
            cont += 1
    percent = (cont*100)/100000
    items_pc.append(percent)
glob_pc.append(items_pc)

percent = 0
for t in threshold:
    cont = 0
    for index, s in df_xl['prob'].iteritems(): # type: ignore
        if isinstance(s, str):
            if len(s)<=5:
                s = float(s)
                if s < t:
                    cont += 1
        elif s < t:
            cont += 1
    percent = (cont*100)/100000
    items_xl.append(percent)
glob_xl.append(items_xl)

glob_pc = pd.DataFrame(glob_pc)
glob_xl = pd.DataFrame(glob_xl)

fig, ax = plt.subplots()
ax.plot(threshold, items_pc, marker='o', label = 'Paracrawl')
ax.plot(threshold, items_xl, marker='o', label = 'XLEnt')
ax.set_ylabel("% Pares de oraciones")
ax.set_xlabel("Umbral")
ax.legend(loc = 'lower right')
plt.show()

