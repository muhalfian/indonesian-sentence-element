import spacy
import stanza
import pandas as pd

filename='sentence'

# Memuat model bahasa Indonesia dari stanza
nlp = stanza.Pipeline(lang='id', processors='tokenize,pos,constituency,lemma,depparse', package='default_accurate')

def analisis_subjek_predikat(kalimat):
    doc = nlp(kalimat)
    subjek = []
    predikat = []
    objek = []
    pelengkap = []
    keterangan = []

    subjek_dependencies = ['nsubj', 'nsubj:pass']
    subjek_pos_tags = ['NOUN', 'PROPN', 'PRON']
    predikat_dependencies = ['root', 'cop', 'attr', 'acl', 'advmod']
    predikat_pos_tags = ['VERB', 'NOUN', 'ADJ', 'NUM']
    objek_dependencies = ['obj', 'iobj']
    objek_pos_tags = ['NOUN', 'PROPN', 'PRON']
    pelengkap_dependencies = ["xcomp", "ccomp", "acomp"]
    keterangan_dependencies = ["advmod", "npadvmod", "obl"]

    # Iterasi setiap token dalam kalimat
    for sent in doc.sentences:
        
        # Menyiapkan flag untuk mendeteksi apakah predikat adalah verba transitif atau intransitif
        predikat_transitif = False

        for word in sent.words:
            # Mendeteksi subjek: biasanya nomina (NOUN atau PROPN) atau pronomina (PRON)
            if word.deprel in subjek_dependencies:
                subjek.append(word.text)
            
            # Mendeteksi predikat: biasanya verba (VERB) atau kata kerja
            if word.deprel in predikat_dependencies and word.upos in predikat_pos_tags:
                predikat.append(word.text)
                # Cek apakah predikat adalah verba transitif (memiliki objek)
                if word.deprel == "root" and any(child.deprel == "obj" for child in sent.words):
                    predikat_transitif = True

            # # Mendeteksi objek: biasanya nomina (NOUN atau PROPN) atau pronomina (PRON)
            # if word.deprel in objek_dependencies:
            #     objek.append(word.text)

            # Mendeteksi objek jika predikatnya adalah verba transitif
            if predikat_transitif and word.deprel == objek_dependencies:
                objek.append(word.text)
            
            # Mendeteksi pelengkap jika predikatnya adalah verba intransitif atau setelah objek
            if not predikat_transitif and word.deprel in pelengkap_dependencies:
                pelengkap.append(word.text)
            elif predikat_transitif and word.deprel == "obl":
                pelengkap.append(word.text)

            # Mendeteksi keterangan (adverbial modifier atau noun phrase adverbial modifier)
            if word.deprel in keterangan_dependencies:
                keterangan.append(word.text)

    return subjek, predikat, objek, pelengkap, keterangan

data = pd.read_excel(filename+".xlsx")

subjects = []
predicates = []
objects = []
pelengkaps = []
keterangans = []

n_subjects = []
n_predicates = []
n_objects = []
n_pelengkaps = []
n_keterangans = []

for i, row in data.iterrows():
    subjek, predikat, objek, pelengkap, keterangan = analisis_subjek_predikat(row["sentence"])
    subjects.append(subjek)
    predicates.append(predikat)
    objects.append(objek)
    pelengkaps.append(pelengkap)
    keterangans.append(keterangan)
    n_subjects.append(len(subjek))
    n_predicates.append(len(predikat))
    n_objects.append(len(objek))
    n_pelengkaps.append(len(pelengkap))
    n_keterangans.append(len(keterangan))

data['subjek'] = subjects
data['predikat'] = predicates
data['objek'] = objects
data['pelengkap'] = pelengkaps
data['keterangan'] = keterangans
data['n_subjek'] = n_subjects
data['n_predikat'] = n_predicates
data['n_objek'] = n_objects
data['n_pelengkap'] = n_pelengkaps
data['n_keterangan'] = n_keterangans

data.to_excel(filename+'_analysis.xlsx')