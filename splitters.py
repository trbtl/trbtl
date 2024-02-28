from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import DataFrameLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pandas as pd
from PyPDF2 import PdfReader

#--------------------------------------------------

def get_text_splits(text_file):
  """Function takes in the text data and returns the  
  splits so for further processing can be done."""
  try:
      with open(text_file,'r', encoding="utf-8") as txt:
        data = txt.read()

      textSplit = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                chunk_overlap=200,
                                                length_function=len)
      doc_list = textSplit.split_text(data)
      return doc_list
  except Exception as e:
      pass
  
#--------------------------------------------------

def get_pdf_splits(pdf_file):
    """Function takes in the pdf data and returns the  
    splits so for further processing can be done."""

    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    textSplit = RecursiveCharacterTextSplitter(chunk_size=1000,
                                            chunk_overlap=200,
                                            length_function=len)
    doc_list = []
    # Pages will be list of pages, so need to modify the loop
    for pg in reader.pages:
        pg_splits = textSplit.split_text(pg.extract_text())
        doc_list.extend(pg_splits)

    return doc_list

#--------------------------------------------------

def get_csv_splits(csv_file):
  """Function takes in the csv and returns the  
  splits so further processing can be done."""
  csvLoader = CSVLoader(csv_file)
  csvdocs = csvLoader.load()
  return csvdocs
     