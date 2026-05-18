# AI-Based Intelligent Phishing Email Detector

An intelligent cybersecurity analytics tool that leverages Natural Language Processing (NLP) and Supervised Machine Learning to classify emails as either **Safe** or **Phishing**. Built using Python and the `scikit-learn` ecosystem, this system models textual features to proactively mitigate social engineering and phishing vectors before execution anomalies occur.

## 🌟 Technical Core Features

- **Text Vectorization (NLP):** Implements **TF-IDF (Term Frequency-Inverse Document Frequency)** via `TfidfVectorizer` to extract statistical relevance from raw text string payloads while filtering out stop words.
- **Probabilistic Supervised Classification:** Utilizes the **Multinomial Naive Bayes (MultinomialNB)** algorithm, a highly efficient probabilistic architecture ideal for discrete text classification constraints.
- **Empirical Model Evaluation:** Auto-computes vital statistical validation metrics including **Overall Accuracy**, **Precision**, **Recall**, and **F1-Score** through a granular classification report.
- **Graphical Confusion Matrix Output:** Integrates `matplotlib` to render real-time interactive analytical graphs depicting True Positives, False Positives, True Negatives, and False Negatives for pipeline transparency.
- **Live Inference Engine:** Features an abstraction layer to pass unseen, raw email strings to the trained inference pipeline for real-time risk classification.

## 🛠️ Data Science & ML Tech Stack

- **Core Logic:** Python 3.x
- **Machine Learning & Feature Engineering:** `scikit-learn` (Scikit-learn)
- **Numerical Processing:** `numpy`
- **Data Visualization:** `matplotlib`

## 📁 Repository Structure

```text
phishing-detector/
├── phishing_detector.py   # Core monolithic Python architecture (Class & Script)
└── README.md            # Detailed academic & operational deployment guide
🚀 Installation & Setup
​Prerequisites

​Ensure you have Python 3 installed along with the required predictive analytics dependencies:

pip install numpy scipy scikit-learn matplotlib

Execution
​To train the pipeline on the contextual training array and perform evaluation, execute the main script inside your shell terminal:

python phishing_detector.py

📊 Pipeline Workflow & Architecture
​Feature Extraction: Raw emails are tokenized and transformed into high-dimensional TF-IDF matrices mapping text metrics.
​Supervised Training: The system splits data arrays (80% Training, 20% Testing) and builds a mathematical model based on the probability distribution of words in malicious versus safe communications.
​Evaluation Window: The engine evaluates mathematical performance and yields an absolute visualization plot graph (Confusion Matrix) to evaluate detection limits.
​Live Inference: The pipeline demonstrates proof-of-concept resilience by analyzing a dynamic threat example:
​Sample Payload: `"🚨 SECURITY ALERT: Someone accessed your account from Russia. Click this link to secure your funds now!"*
​Classification Result: ---> Phishing <---
​🛡️ Academic & Strategic Application
​This pipeline serves as a structural blueprint for advanced automated attack detection layers in enterprise network protection. It can be integrated into mail transfer agents (MTAs) to act as a defensive boundary element, scanning incoming data traffic payloads against social engineering patterns.
