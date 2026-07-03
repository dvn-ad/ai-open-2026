# AI-Powered Customs Declaration Automation Platform

An automated AI-driven platform for extracting, validating, and submitting Indonesian customs declarations (PIB) based on international trade documents. 

This platform processes trade documents—**Commercial Invoice (CI)**, **Packing List (PL)**, **Bill of Lading (BL)**, **Pemberitahuan Impor Barang (PIB)**, and **Form E Certificate of Origin**—reconciles them, evaluates them against Indonesian **Permendag import rules**, runs an **Explainable Machine Learning Risk Classifier** (XGBoost + SHAP), and maps them into a simulated **CEISA 4.0 Host-to-Host submission payload**.

---

## Key Features

1. **OCR & Layout Intelligence**: Integrates **Docling**, **PaddleOCR**, **LayoutLMv3**, and **TableTransformer** to parse unstructured documents, extract table grids, and classify semantic document blocks.
2. **LLM Structuring Layer**: Maps raw text, bounding boxes, and tabular structures into structured Pydantic schemas using local LLMs via **Ollama**.
3. **Permendag Rule Validation**: Custom rules engine to validate mandatory fields, HS Code restrictions, and required import permits (e.g., `PI_Besi_Baja`, `LS_Tekstil`).
4. **Cross-Document Reconciliation**: Reconciles fields across PIB, Form E, Invoice, Packing List, and Bill of Lading (e.g., verifying weights, quantities, invoice numbers, and BL numbers, highlighting discrepancies).
5. **Explainable ML Classifier**: Uses a custom-trained **XGBoost model** to predict rejections and runs **SHAP explanations** to explain the exact risk factor attribution.
6. **CEISA 4.0 Integration**: Maps validated documents to simulated CEISA payloads and issues government clearance status (Green/Yellow/Red lanes).

---

## System Architecture & Process Flow

A detailed flow diagram and step-by-step technical explanation of the document extraction, validation, and submission flow can be found in the [SYSTEM_FLOW.md](file:///home/mendoan/Projects/ai-open-2026/SYSTEM_FLOW.md) document.

---

## Input & Output Specifications

### 1. Inputs
* **API Ingestion**: Upload individual files (`commercial_invoice`, `packing_list`, `bill_of_lading`) or a **single combined PDF** (e.g., the complete dataset package containing PIB, CI, PL, BL, Form E, etc.).
* **CLI Ingestion**: Target local image/PDF files (e.g., `images/4.png` or `dataset/UEU-Master-16519-lampiran.Image.Marked.pdf`).

### 2. Outputs
* **Data Extraction**: Conforms to the `ExtractedDocuments` schema containing structured fields and OCR confidence scores.
* **Validation Intelligence**:
  * **Confidence Score** (0-100%): Derived from OCR quality, cross-document consistency, compliance, and ML risk probability.
  * **Compliance Score** (0-100%): Based on Permendag rules compliance.
  * **Risk Level** (`Low`, `Medium`, `High`) and **ML Risk Probability**.
  * **Warnings**: List of detailed warnings with `severity`, `rule_id`, `message`, `affected_fields`, and `suggested_fix`.
  * **SHAP Risk Attributions**: Feature attributions explaining *why* a particular risk level was predicted.
* **CEISA Mapping**: Simulated Host-to-Host submission response with simulated Status (`RECEIVED`), assigned PIB Number, and estimated clearance lane (`GREEN`, `YELLOW`, `RED`).

---

## Installation & Setup (Without Docker)

Follow these steps to run the complete system locally.

### Prerequisites
* Python 3.11+
* CUDA Toolkit (optional, for GPU acceleration)
* [Ollama](https://ollama.com/) (installed and running)

### Step 1: Install Python Dependencies
Set up a virtual environment and install the required libraries:
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install packages
pip install --upgrade pip
pip install -r requirements.txt
pip install python-multipart
```

### Step 2: Set Up Ollama
Start Ollama and pull the required Qwen model (uses `qwen3.5:9b` by default):
```bash
# Pull the model
ollama pull qwen3.5:9b
```

### Step 3: Generate Synthetic Data & Train ML Model
Before running the main application, generate the synthetic training records and train the XGBoost risk classification model:
```bash
# Generate synthetic dataset
python3 src/validation/synthetic_data.py

# Train the XGBoost risk model
python3 src/validation/train_model.py
```

---

## How to Run

### 1. Run the Dataset Test Suite (Recommended)
We have integrated a comprehensive dataset test script that uploads the multi-page Indonesian customs dataset PDF ([UEU-Master-16519-lampiran.Image.Marked.pdf](file:///home/mendoan/Projects/ai-open-2026/dataset/UEU-Master-16519-lampiran.Image.Marked.pdf)) directly through the API endpoints. It validates the documents, detects number mismatches, maps them to CEISA, and queries the HS Code predictor:
```bash
python3 src/test_dataset_run.py
```

### 2. Run the Command-Line Pipeline
To process the local target image (`images/4.png`) end-to-end through the OCR and local LLM modules:
```bash
python3 src/main.py
```

### 3. Start the FastAPI REST API Server
To spin up the platform as a backend REST API service:
```bash
uvicorn src.validation.api:app --host 0.0.0.0 --port 8000
```
Once started, you can access the interactive Swagger documentation and test endpoints at **http://localhost:8000/docs**.

---

## Docker Setup (Optional)

Alternatively, you can build and run the platform using Docker:
```bash
# 1. Build the GPU-enabled Docker image
docker build -t customs-ai .

# 2. Run the FastAPI validation server (exposed on port 8000)
docker run --gpus all -p 8000:8000 customs-ai

# 3. Run the end-to-end pipeline script directly inside the container
docker run --gpus all -it customs-ai python3 src/main.py
```
