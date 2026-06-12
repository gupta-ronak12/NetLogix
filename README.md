# 🚀 NetLogix: Hybrid Log Classification Framework

## 📖 Overview

**NetLogix** is a robust and modular hybrid log classification system designed to intelligently categorize log messages using a multi-layered classification architecture.

The framework combines:

* Rule-based pattern matching
* Machine Learning-based semantic classification
* Large Language Model (LLM) reasoning

This hybrid approach ensures high accuracy, scalability, and reliability when handling both structured and previously unseen log data.

---

# 🏗️ Classification Architecture

Each log message passes through a tiered decision pipeline:

## 1️⃣ Regex Classification

The first layer performs high-speed deterministic classification using predefined regular expression patterns.

### Benefits

* Extremely fast execution
* High precision for known log formats
* Low computational cost

---

## 2️⃣ BERT-Based Classification

For logs that cannot be classified through regex patterns, the framework uses:

* Sentence Transformer embeddings
* Logistic Regression classifier

This layer provides semantic understanding of log messages and is effective when historical training data is available.

### Benefits

* Context-aware classification
* Handles variations in wording
* Improves accuracy for semi-structured logs

---

## 3️⃣ LLM-Based Fallback Classification

If the first two layers fail to confidently classify a log message, NetLogix leverages a Large Language Model through the **Groq API**.

The LLM performs context-aware reasoning to classify unknown or previously unseen log entries.

### Benefits

* Handles edge cases
* Supports unseen patterns
* Provides intelligent fallback classification

---

# 📂 Project Structure

```text
NetLogix/
│
├── models/
│   ├── *.joblib
│   └── Trained ML models
│
├── resources/
│   ├── Sample datasets
│   ├── CSV outputs
│   └── Documentation assets
│
├── training/
│   ├── Jupyter notebooks
│   └── Model training scripts
│
├── server.py
├── processor_llm.py
├── bert_model_processor.py
├── requirements.txt
├── .env
└── README.md
```

### Directory Description

| Folder/File               | Purpose                                              |
| ------------------------- | ---------------------------------------------------- |
| `models/`                 | Stores serialized machine learning models            |
| `resources/`              | Contains datasets, outputs, and supporting resources |
| `training/`               | Training and evaluation notebooks/scripts            |
| `server.py`               | FastAPI application entry point                      |
| `processor_llm.py`        | LLM classification module                            |
| `bert_model_processor.py` | BERT-based classification module                     |

---

# ⚙️ Setup & Installation

## Prerequisites

* Python 3.10+
* Pip
* Groq API Key

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/gupta-ronak12/NetLogix.git
cd NetLogix
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_api_key_here
```

### Security Note

Always add `.env` to `.gitignore` to prevent exposing sensitive credentials.

```gitignore
.env
```

---

# Running the Application

Start the FastAPI server:

```bash
python server.py
```

---

# 🌐 API Endpoints

### Main Endpoint

```text
http://127.0.0.1:8000/
```

### Interactive Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# 📊 Usage

The system accepts CSV uploads containing the following columns:

| Column        | Description       |
| ------------- | ----------------- |
| `source`      | Source of the log |
| `log_message` | Raw log message   |

### Processing Flow

* Upload CSV file
* Logs pass through Regex Classification
* Unclassified logs move to BERT Classification
* Remaining logs are handled by the LLM Fallback Layer
* Output CSV is generated

### Output

The returned CSV contains:

* Original columns
* Predicted classification label

Additional column:

```text
target_label
```

---

# ✨ Key Features

* Hybrid multi-layer log classification
* Regex-based fast pattern matching
* BERT semantic understanding
* LLM-powered intelligent fallback
* FastAPI integration
* CSV upload and processing support
* Modular and scalable architecture
* Easy deployment and extensibility

---

# 🛠️ Technology Stack

* Python
* FastAPI
* Sentence Transformers
* Scikit-Learn
* Logistic Regression
* Regular Expressions (Regex)
* Groq API
* Pandas
* Joblib

---

# 📈 Future Enhancements

* Confidence score reporting
* Real-time log stream processing
* Model retraining pipeline
* Dashboard for classification analytics
* Multi-language log support

