# Introduction to Deep Learning
### AgenticLabs.ng — Free Courses Programme

A complete, hands-on introduction to deep learning built for the AgenticLabs course platform. The course takes learners from the mathematical foundations of neural networks all the way to fine-tuning large pretrained language models, with every concept implemented in code from scratch before being applied using modern frameworks.

All materials are written as Google Colab notebooks. No local installation is required — learners only need a Google account and a browser.

---

## Course Overview

**Level:** Beginner to Intermediate  
**Duration:** Approximately 40 hours  
**Framework:** PyTorch  
**Environment:** Google Colab (GPU recommended)  
**Prerequisites:** Basic Python, high school mathematics  

---

## Modules

### Module 0 — Setup and Orientation
Environment verification, tensor operations, and the NumPy-to-PyTorch bridge. Every learner runs this first to confirm their Colab runtime is correctly configured before proceeding.

Key topics: PyTorch installation, tensor creation and operations, GPU detection, activation function preview.

---

### Module 1 — From Machine Learning to Deep Learning
Builds the foundational intuition for neural networks by implementing the core concepts manually in NumPy, with no framework abstraction.

Key topics: Linear regression from scratch, the perceptron algorithm, loss functions (MSE, cross-entropy), gradient descent, decision boundary visualisation.

---

### Module 2 — Neural Networks and Backpropagation
The most important module in the course. Learners implement backpropagation by hand before using PyTorch's autograd, so the framework is never a black box.

Key topics: Multi-layer perceptrons, activation functions (ReLU, Sigmoid, GELU), the chain rule, manual backpropagation on the XOR problem, PyTorch training loop, SGD vs Adam, MNIST classification, confusion matrix analysis.

---

### Module 3 — Convolutional Neural Networks
Covers the architecture that powers nearly all modern computer vision. Begins with manual convolution to build filter intuition, then scales up to a full CNN trained on CIFAR-10.

Key topics: Convolution and pooling, feature maps, batch normalisation, dropout, data augmentation, transfer learning with pretrained ResNet-18.

---

### Module 4 — Recurrent Networks and Sequence Modelling
Introduces sequential data and the architectures designed to handle it. The vanishing gradient problem is demonstrated empirically before LSTMs are introduced as the solution.

Key topics: Vanilla RNN from scratch, vanishing gradient visualisation, LSTM gating mechanisms, bidirectional LSTMs, word embeddings, sentiment analysis on the IMDb dataset.

---

### Module 5 — Training Best Practices
The production engineering module. Covers everything a practitioner needs to train models reliably, diagnose problems, and avoid common pitfalls.

Key topics: Overfitting and underfitting diagnosis, dropout vs L2 regularisation comparison, batch normalisation impact on convergence speed, learning rate schedulers (StepLR, CosineAnnealing, OneCycleLR), early stopping implementation, a full production training checklist.

---

### Module 6 — Introduction to Transformers
Introduces the architecture that underpins all modern large language models, building up from self-attention to a full fine-tuned BERT classifier.

Key topics: Self-attention from scratch, multi-head attention, positional encoding, the Transformer architecture, BERT vs GPT, fine-tuning DistilBERT on IMDb using Hugging Face Transformers.

---

### Capstone — End-to-End Image Classification Pipeline
A full project that brings together every skill from the course. Learners design, train, evaluate, and export a complete image classifier, then write a structured reflection on their results.

Key topics: Exploratory data analysis, custom CNN design, training with early stopping and cosine annealing, confusion matrix and per-class accuracy analysis, error analysis on high-confidence mistakes, model checkpointing and reload, written reflection.

---

## Technology Stack

| Library | Purpose |
|---|---|
| PyTorch | Primary deep learning framework |
| torchvision | Computer vision datasets and pretrained models |
| Hugging Face Transformers | Pretrained language models (Module 6) |
| Hugging Face Datasets | IMDb and other benchmark datasets |
| NumPy | Numerical computing and manual implementations |
| Matplotlib / Seaborn | Visualisation and training curve plotting |
| scikit-learn | Evaluation metrics and preprocessing |

---

## Recommended Resources

The following freely available resources are recommended alongside this course:

- **Andrej Karpathy — Neural Networks: Zero to Hero** (`karpathy.ai/zero-to-hero`) — Modules 1 to 3
- **Andrew Ng — Deep Learning Specialization** (`deeplearning.ai`) — Modules 1 to 5
- **MIT 6.S191 — Introduction to Deep Learning** (`introtodeeplearning.com`) — Modules 1, 2, and 6
- **fast.ai — Practical Deep Learning for Coders** (`course.fast.ai`) — Modules 3 to 5 and Capstone
- **Dive into Deep Learning** (`d2l.ai`) — Full course reference
- **PyTorch Official Tutorials** (`docs.pytorch.org/tutorials`) — Modules 2 to 4
- **Hugging Face NLP Course** (`huggingface.co/learn`) — Module 6

---

## How to Use These Notebooks

1. Open [colab.research.google.com](https://colab.research.google.com)
2. Go to **File → Open notebook → GitHub**, paste this repository URL, and select a notebook
3. Set the runtime to GPU: **Runtime → Change runtime type → T4 GPU**
4. Run all cells from top to bottom — each notebook is fully self-contained

Alternatively, download any `.ipynb` file and upload it directly to Colab via **File → Upload notebook**.

---

## Repository Structure

```
intro-to-deep-learning/
├── README.md
├── Module_00_Setup_and_Orientation.ipynb
├── Module_01_From_ML_to_Deep_Learning.ipynb
├── Module_02_Neural_Networks_and_Backpropagation.ipynb
├── Module_03_Convolutional_Neural_Networks.ipynb
├── Module_04_RNNs_and_Sequence_Modelling.ipynb
├── Module_05_Training_Best_Practices.ipynb
├── Module_06_Introduction_to_Transformers.ipynb
└── Capstone_End_to_End_Image_Classifier.ipynb
```

---

## About AgenticLabs

AgenticLabs (agenticlabs.ng) is building the next generation of AI professionals in Africa through in-depth courses, expert-led programmes, hackathons, and a thriving learning community. This course is part of the free courses programme currently in development.

For instructors: course creation tools are available at `/studio`.

---

*Course authored by the AgenticLabs AI/ML team. All notebooks are open for learner use and modification.*
