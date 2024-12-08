# Sentence Analysis with NLP
This repository provides a Python script for performing syntactic analysis of sentences in the Indonesian language. The script uses stanza and spacy for natural language processing tasks and generates detailed syntactic analysis, including subject, predicate, object, complement, and adverbial components.

## Features
Extracts syntactic components (subject, predicate, object, complement, and adverbials).
Outputs the analysis into an Excel file for further exploration.
Supports the Indonesian language using the stanza NLP library.

## Installation
### Prerequisites
1. Python 3.7+
Ensure you have Python installed. If not, download it from the official Python website.

2. Libraries
Install the required libraries by running the following command:
```
pip install spacy stanza pandas openpyxl
```

3. Stanza Model
Download the Indonesian language model for stanza:
```
import stanza
stanza.download('id')
```

## How to Run
1. Prepare Input Data
Create an Excel file containing a column named sentence, where each row represents a sentence for analysis. Save the file as sentence.xlsx in the same directory as the script.

2. Run the Script
Execute the script using Python:
```
python subject_predicate_analysis.py
```
3. Output
The script will generate an output file named sentence_analysis.xlsx, containing:
- Extracted syntactic components (subject, predicate, object, complement, adverbials).
- Count of each component per sentence.

## What You Get
The output Excel file will include the following columns:

- __subjek__: Extracted subjects.
- __predikat__: Extracted predicates.
- __objek__: Extracted objects.
- __pelengkap__: Extracted complements.
- __keterangan__: Extracted adverbials.
- __n_subjek__: Number of subjects per sentence.
- __n_predikat__: Number of predicates per sentence.
- __n_objek__: Number of objects per sentence.
- __n_pelengkap__: Number of complements per sentence.
- __n_keterangan__: Number of adverbials per sentence.

## Notes
- Ensure the input file (sentence.xlsx) is in the correct format and contains a sentence column.
- The script may need adjustments for sentences with complex syntactic structures.

Feel free to contribute or report issues!