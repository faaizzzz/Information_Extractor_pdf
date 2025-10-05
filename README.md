Information Extraction from PDFs using QA System

 Problem Statement
Build a system that can process provided PDF documents and allow a user to ask questions about their content.
The system automatically extracts information and returns relevant answers.

Requirements
- Accept multiple PDF documents as input.
- Make the documents searchable.
- When a user asks a question in natural language, return the most relevant document sections.
- Provide a simple interface (CLI or notebook).



 Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
## create a folder named 'pdfs' add the pdfs in this folder
##create a index for pdfs by running this code in your bash
python app.py --index pdfs --save-index index.pkl
##run QA mode by running this code in ypur bash
python app.py --load-index index.pkl

#will suggest to follow this steps
## follow the below steps to run in google colab
##install dependencies
!pip install pdfplumber scikit-learn numpy joblib
##upload app.py and indexer.py file after running the below code
from google.colab import files
uploaded = files.upload()  # upload app.py, indexer.py
##upload the pdfs in the Google Colab
##run the below code step by step to ask the questions
import sys
sys.path.append('/content')

main(index_folder="pdfs")    # This will build index.pkl from all PDFs


!python3 app.py
##the last step will allow you to ask questions 





