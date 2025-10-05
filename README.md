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
uploaded = files.upload()  # upload app.py, indexer.py , and the pdfs in a folder called pdfs if not uploaded earlier.
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
❓ Question: What are the main components of the Cybersecurity Framework?

📘 Auto-detected document: NIST.CSWP.04162018.pdf

[1] 🔎 From NIST.CSWP.04162018.pdf (score=0.2759):
• Ultimately, the Framework is aimed at reducing and better managing cybersecurity risks.
• April 16, 2018 Cybersecurity Framework Version 1.1 This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018 3 To account for the unique cybersecurity needs of organizations, there are a wide variety of ways to use the Framework.
• The decision about how to apply it is left to the implementing organization.
• For example, one organization may choose to use the Framework Implementation Tiers to articulate envisioned risk management practices.
• Another organization may use the Framework’s five Functions to analyze its entire risk management portfolio; that analysis may or may not rely on more detailed companion guidance, such as controls catalogs.

[2] 🔎 From NIST.CSWP.04162018.pdf (score=0.2725):
• people or organizations that consume a given product or service.
• Category The subdivision of a Function into groups of cybersecurity outcomes, closely tied to programmatic needs and particular activities.
• Examples of Categories include “Asset Management,” “Identity Management and Access Control,” and “Detection Processes.” Critical Infrastructure Systems and assets, whether physical or virtual, so vital to the United States that the incapacity or destruction of such systems and assets would have a debilitating impact on cybersecurity, national economic security, national public health or safety, or any combination of those matters.
• Cybersecurity The process of protecting information by preventing, detecting, and responding to attacks.
• Cybersecurity Event A cybersecurity change that may have an impact on organizational operations (including mission, capabilities, or reputation).

❓ Question: What is multi-head attention and why is it useful?

📘 Auto-detected document: 1706.03762v7.pdf

[1] 🔎 From 1706.03762v7.pdf (score=0.2446):
• of Figure 1, respectively.
• 3.1 Encoder and Decoder Stacks Encoder: The encoder is composed of a stack of N = 6 identical layers.
• Each layer has two sub-layers.
• The first is a multi-head self-attention mechanism, and the second is a simple, position- wise fully connected feed-forward network.
• We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1].

[2] 🔎 From 1706.03762v7.pdf (score=0.2130):
• softmax function to obtain the weights on the values.
• In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix Q.
• The keys and values are also packed together into matrices K and V .
• We compute the matrix of outputs as: Attention(Q, K, V ) = softmax(QKT √dk )V (1) The two most commonly used attention functions are additive attention [2], and dot-product (multi- plicative) attention.
• Dot-product attention is identical to our algorithm, except for the scaling factor of 1 √dk .

❓ Question: What are the two training objectives of BERT?

📘 Auto-detected document: 1810.04805v2.pdf

[1] 🔎 From 1810.04805v2.pdf (score=0.2118):
• The training loss is the sum of the mean masked LM likelihood and the mean next sentence prediction likelihood.
• Training of BERTBASE was performed on 4 Cloud TPUs in Pod conﬁguration (16 TPU chips total).13 Training of BERTLARGE was performed on 16 Cloud TPUs (64 TPU chips total).
• Each pre- training took 4 days to complete.
• Longer sequences are disproportionately expen- sive because attention is quadratic to the sequence length.
• To speed up pretraing in our experiments, we pre-train the model with sequence length of 128 for 90% of the steps.

[2] 🔎 From 1810.04805v2.pdf (score=0.1828):
• possible so that the two methods could be minimally compared.
• The core argument of this work is that the bi-directionality and the two pre- training tasks presented in Section 3.1 account for the majority of the empirical improvements, but we do note that there are several other differences between how BERT and GPT were trained: • GPT is trained on the BooksCorpus (800M words); BERT is trained on the BooksCor- pus (800M words) and Wikipedia (2,500M words).
• • GPT uses a sentence separator ([SEP]) and classiﬁer token ([CLS]) which are only in- troduced at ﬁne-tuning time; BERT learns [SEP], [CLS] and sentence A/B embed- dings during pre-training.
• • GPT was trained for 1M steps with a batch size of 32,000 words; BERT was trained for 1M steps with a batch size of 128,000 words.
• • GPT used the same learning rate of 5e-5 for all ﬁne-tuning experiments; BERT chooses a task-speciﬁc ﬁne-tuning learning rate which performs the best on the development set.




