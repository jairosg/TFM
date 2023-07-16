## TFM: Uso de grafos de conocimiento para la mejora de la calidad de los datos de entrenamiento en traducción automática
El objetivo de este trabajo es la reducción del porcenatje de ocurrencia de errores relacionados con la traducción de Entidades Nombradas.
## Instalación
Para poder ejecutar todos los scripts se debe usar las siguientes librerías, en su versión más reciente:
pandas
matplotlib.pyplot
numpy
seaborn
random
spacy
posixpath
SPARQLWrapper

## Extracción de datos y muestras
En la carpeta /first_tus, se encuentran los datos paralelos, de los subconjuntos Paracrawl y XLEnt, usados a lo largo del proceso. Tras el procesamiento de estos datos paralelos por las herramientas Bicleaner y Bicleaner AI (Lite y Full), se obtienen los datos clasificados por las herramientas. Los archivos clasificados se encuentran en /Data test/Classic/Paracrawl.en-es.classified para la versión clásica de Bicleaner, /Data test/Lite/Paracrawl.en-es.classfiedAI para Bicleaner AI Lite y /Data test/Full/Paracrawl.en-es.full.classified para Bicleaner AI Full.

A partir de estos ficheros se van a extraer el resto de ellos necesarios para realizar los experimentos y más tarde comprobar el funcionamiento del método propuesto.
Primeramente, con el fichero /scripts/lectura.py, se va a sacar la longitud media de los pares de oraciones y división del dataset en oraciones largas o cortas. Además de realizar un último filtrado con el umbral 0.5/0.7 y obtener los ficheros con el conjunto de oraciones que superan el umbral impuesto.

Para poder realizar el análisis y pruebas con un número de unidades de traducción manejable, con el fichero /scripts/genTest.py, se extraen 100 muestras aleatorias de segmentos paralelos. 
En la carpeta /Data test según la versión de Bicleaner, se encuentran todos los archivos resultantes de las operaciones anteriores descritas.

Por último, para visualizar el procentaje de unidades de traducción que no superan el umbral y ver de esta manera que dataset es de mayor calidad se utiliza el fichero /scripts/umbra-gx.py. Cuyo resultado, con los subconjutos de datos usados, son: Poner imágenes.

## Mejora de la calidad de datos
Para poder utilizar el método es necesario realizar las siguientes instalaciones:
```python
!pip install spacy-transformers
!python -m spacy download en_core_web_trf
!pip install spacy-dbpedia-spotlight
!pip install https://huggingface.co/sdocio/es_spacy_ner_cds/resolve/main/es_spacy_ner_cds-any-py3-none-any.whl
!pip install sparqlwrapper
```
El siguiente paso será definir el pipeline para cada idioma:
```python
nlp = spacy.load('en_core_web_trf')
nlp.add_pipe('dbpedia_spotlight')

nlp_es= spacy.load("es_spacy_ner_cds")
nlp_es.add_pipe('sentencizer')
```
Una vez se tengan instaladas las herramientas necesarias y definidos los pipeline, se podrá ejecutar el método. El cuaderno spacy_NER.ipynb, incluye todos los pasos necesarios para ello, por lo que a través de su descarga se podrá usar directamente.

Los ficheros de entrada para este método se encuentran en la carpeta /Data test, los ficheros tienen el mismo nombre para las tres herramientas pero distribuidos en su carpeta correspondiente a la herramienta. Mediante el uso de estos fihceros de entrada se deberá obtener los ficheros de salida encontrados en la carpeta /Outputs

## Autor
Jairo Sánchez García.

## Contacto
jairosg23@gmail.com

