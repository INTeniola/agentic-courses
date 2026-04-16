# Agentic AI Development: Machine Learning Foundations
### AgenticLabs.ng — Free Courses Programme

Welcome to the foundational curriculum for Agentic AI. This repository contains a complete, 3-module introduction to Machine Learning, designed to take learners from Python basics to foundational ML algorithms.

All materials are written as hands-on Google Colab notebooks. No local installation is required.

---

## 🎓 Curriculum Overview

The curriculum is divided into three sequential modules. Each module contains 5 practical lessons, clear learning outcomes, and a dedicated "bridge" section connecting traditional ML to modern AI workflows.

### [Module 00: Coding Essentials for Agents](Module_00_Coding_Essentials_for_Agents.ipynb)
**Focus**: Prerequisite skills · Python, Data Structures, APIs

- **1.1 Python Fundamentals Refresher**: Variables, loops, functions, and conditionals. Emphasis on clean, readable code.
- **1.2 Working with Data Structures**: Lists, dictionaries, DataFrames — the backbone of every ML workflow.
- **1.3 Libraries and Environment Setup**: Using NumPy, pandas, and scikit-learn in Jupyter/Colab.
- **1.4 Reading and Writing Data**: Loading CSVs/JSONs with pandas and handling missing values.
- **1.5 Calling External APIs**: Using `requests` to call LLM endpoints (Anthropic Claude demo).

> [!TIP]
> **The API Bridge**: Module 0.5 is a strategic bridge. By showing how to call an LLM API early on, we connect core Python skills directly to the GenAI content where agents take action.

**Learning Outcomes**:
- Set up a Python environment and install key ML libraries.
- Read, clean, and inspect a dataset using pandas.
- Write a Python script that calls an external API and processes the response.

---

### [Module 01: Building Your First ML Model](Module_01_Building_Your_First_ML_Model.ipynb)
**Focus**: End-to-end workflow · From data to prediction

- **2.1 What is Machine Learning?**: Supervised vs unsupervised learning with real-world examples.
- **2.2 Preparing Your Dataset**: Feature selection, train/test split, and handling outliers.
- **2.3 Training a Model**: Using scikit-learn for Linear Regression and Decision Trees.
- **2.4 Evaluating Performance**: Accuracy, precision, recall, and the confusion matrix.
- **2.5 Improving Your Model**: Tuning hyperparameters and the iteration loop (Train → Evaluate → Improve).

**Learning Outcomes**:
- Explain the difference between supervised and unsupervised learning.
- Prepare a real dataset and split it for training and testing.
- Train, evaluate, and iterate on a model using scikit-learn.

---

### [Module 02: Foundational ML Algorithms](Module_02_Foundational_ML_Algorithms.ipynb)
**Focus**: Core concepts · How algorithms learn and decide

- **3.1 Linear and Logistic Regression**: Predicting values vs classifying outcomes; gradient descent intuition.
- **3.2 Decision Trees and Random Forests**: How trees split data and why ensemble methods are stronger.
- **3.3 KNN and Clustering**: Instance-based learning and unsupervised grouping (K-Means).
- **3.4 Support Vector Machines**: Finding optimal boundaries between classes.
- **3.5 Choosing the Right Algorithm**: A practical decision guide based on data size and interpretability.

> [!TIP]
> **The Deep Learning Bridge**: Module 3.5 is intentionally designed to link traditional ML concepts to neural networks, setting learners up perfectly for the "Deep Learning Foundations" section that follows.

**Learning Outcomes**:
- Describe how 4+ core ML algorithms work and when to use each.
- Implement and compare multiple algorithms on the same dataset.
- Explain how traditional ML concepts extend into deep learning and neural networks.

---

## 🚀 Advanced Curriculum (Coming Soon)

The following modules represent the next phase of the AgenticLabs roadmap:

- **Module 03 — Neural Networks and Backpropagation**
- **Module 04 — Convolutional Neural Networks**
- **Module 05 — Recurrent Networks and Sequence Modelling**
- **Module 06 — Introduction to Transformers**
- **Capstone — End-to-End Image Classification Pipeline**

---

## 🛠️ Technology Stack
| Tool | Purpose |
|---|---|
| **Python 3** | Core logic and scripting |
| **pandas** | Tabular data manipulation |
| **NumPy** | Numerical computing and array operations |
| **scikit-learn** | Classical ML algorithms and evaluation |
| **matplotlib / seaborn** | Data visualisation |
| **requests** | REST API interaction |

## 📖 How to Use
1. Open [colab.research.google.com](https://colab.research.google.com).
2. Go to **File** → **Open notebook** → **GitHub**.
3. Paste this repository URL and select the Module you wish to start.
4. Set the runtime to **GPU** (for later modules) or **Standard** via *Runtime → Change runtime type*.

## About AgenticLabs
AgenticLabs ([agenticlabs.ng](https://agenticlabs.ng)) is building the next generation of AI professionals in Africa. This course is part of our commitment to accessible, high-quality technical education.

*Curriculum authored by the AgenticLabs AI/ML team.*
