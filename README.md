Information Extraction from PDFs using QA System

 Problem Statement
Build a system that can process provided PDF documents and allow a user to ask questions about their content.
The system automatically extracts information and returns relevant answers.

Requirements
- Accept multiple PDF documents as input.
- Make the documents searchable.
- When a user asks a question in natural language, return the most relevant document sections.
- Provide a simple interface (CLI or notebook).



 Setup Instructions and how to run.

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

##tech stack

| Component         | Technology Used                  |
| ----------------- | -------------------------------- |
| Language          | Python 3                         |
| PDF Parsing       | `pdfplumber`                     |
| Vectorization     | `TfidfVectorizer` (scikit-learn) |
| Similarity Search | Cosine Similarity                |
| Model Persistence | `joblib`                         |
| CLI Interface     | Python argparse                  |
| (Optional) Web UI | Flask                            |


##example query
✅ Index loaded successfully.

💬 QA Mode started. Press ENTER on an empty line to exit.

❓ Question: What are the five core functions of the Cybersecurity Framework?

📘 Auto-detected document: NIST.CSWP.04162018.pdf

[1] 🔎 From NIST.CSWP.04162018.pdf (score=0.5080):
• as helpful in managing cybersecurity risk.
• The Core comprises four elements: Functions, Categories, Subcategories, and Informative References, depicted in Figure 1: Figure 1: Framework Core Structure The Framework Core elements work together as follows:  Functions organize basic cybersecurity activities at their highest level.
• These Functions are Identify, Protect, Detect, Respond, and Recover.
• They aid an organization in expressing its management of cybersecurity risk by organizing information, enabling risk management decisions, addressing threats, and improving by learning from previous activities.
• The Functions also align with existing methodologies for incident management and help show the impact of investments in cybersecurity.

[2] 🔎 From NIST.CSWP.04162018.pdf (score=0.4350):
• 800-398, and the Electricity Subsector Cybersecurity Risk Management Process (RMP) guideline9.
• 1.3 Document Overview The remainder of this document contains the following sections and appendices:  Section 2 describes the Framework components: the Framework Core, the Tiers, and the Profiles.
•  Section 3 presents examples of how the Framework can be used.
•  Section 4 describes how to use the Framework for self-assessing and demonstrating cybersecurity through measurements.
•  Appendix A presents the Framework Core in a tabular format: the Functions, Categories, Subcategories, and Informative References.



