TRACKS = {
    "track1_aiml_foundations": {
        "label": "AI / ML Foundations",
        "description": (
            "Core concepts in ML, deep learning, computer vision, NLP, and model training. "
            "Prerequisite knowledge for the Agentic AI track."
        ),
        "courses": [

            {
                "id": "F-01",
                "title": "Explore the GenAI Universe",
                "description": "A broad, accessible introduction to generative AI — what it is, how it works at a high level, and where the field stands in 2026.",
                "prerequisites": "None",
                "audience": "Anyone curious about AI",
                "sections": [
                    {
                        "title": "What is Generative AI?",
                        "lessons": [
                            {"id": "F01-L01", "title": "Welcome and course overview", "type": "intro"},
                            {"id": "F01-L02", "title": "From discriminative to generative models", "type": "concept"},
                            {"id": "F01-L03", "title": "Key modalities: text, image, audio, code, multimodal", "type": "concept"},
                            {"id": "F01-L04", "title": "Quiz: What is Generative AI?", "type": "quiz"},
                        ]
                    },
                    {
                        "title": "The GenAI Landscape",
                        "lessons": [
                            {"id": "F01-L05", "title": "Foundational model families: LLMs, diffusion, multimodal", "type": "concept"},
                            {"id": "F01-L06", "title": "Key players and open-source ecosystem (2026 landscape)", "type": "concept"},
                            {"id": "F01-L07", "title": "The AI development stack: data, compute, frameworks, APIs", "type": "concept"},
                            {"id": "F01-L08", "title": "Real-world applications and industry use cases", "type": "concept"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "F01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "F-02",
                "title": "Responsible AI in the Generative AI Era",
                "description": "Ethics, safety, and governance for generative AI — built for practitioners who need to ship responsibly.",
                "prerequisites": "F-01 or basic AI familiarity",
                "audience": "Developers, product teams, AI practitioners",
                "sections": [
                    {
                        "title": "Core Principles",
                        "lessons": [
                            {"id": "F02-L01", "title": "Welcome and course overview", "type": "intro"},
                            {"id": "F02-L02", "title": "Why responsible AI matters now more than ever", "type": "concept"},
                            {"id": "F02-L03", "title": "Bias, fairness, and representation in generative models", "type": "concept"},
                            {"id": "F02-L04", "title": "Hallucination, factuality, and reliability challenges", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Risk and Governance",
                        "lessons": [
                            {"id": "F02-L05", "title": "Safety, alignment, and RLHF: the basic picture", "type": "concept"},
                            {"id": "F02-L06", "title": "AI regulations and compliance landscape (EU AI Act, Nigeria NDPC)", "type": "concept"},
                            {"id": "F02-L07", "title": "Evaluating your own AI products responsibly", "type": "concept"},
                            {"id": "F02-L08", "title": "Quiz: Responsible AI principles", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "F02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "ML-01",
                "title": "Coding Essentials for Agents",
                "description": "Python and tooling skills specifically needed to build AI agents and ML pipelines.",
                "prerequisites": "Basic programming literacy",
                "audience": "Beginners transitioning into AI engineering",
                "sections": [
                    {
                        "title": "Python Foundations for AI",
                        "lessons": [
                            {"id": "ML01-L01", "title": "Course overview and environment setup (Colab/VS Code)", "type": "intro"},
                            {"id": "ML01-L02", "title": "Python data structures agents rely on: lists, dicts, sets", "type": "concept"},
                            {"id": "ML01-L03", "title": "Functions, classes, and modular code design", "type": "concept"},
                            {"id": "ML01-L04", "title": "Exercise: build a simple data pipeline in Python", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Working with Data",
                        "lessons": [
                            {"id": "ML01-L05", "title": "NumPy essentials: arrays, broadcasting, vectorisation", "type": "concept"},
                            {"id": "ML01-L06", "title": "Pandas for structured data manipulation", "type": "concept"},
                            {"id": "ML01-L07", "title": "Reading and writing JSON, CSV, and API responses", "type": "concept"},
                            {"id": "ML01-L08", "title": "Exercise: explore and clean a real dataset", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Practical Python for AI Workflows",
                        "lessons": [
                            {"id": "ML01-L09", "title": "Async programming basics: why agents need it", "type": "concept"},
                            {"id": "ML01-L10", "title": "HTTP requests, REST APIs, and error handling", "type": "concept"},
                            {"id": "ML01-L11", "title": "Environment variables and secrets management", "type": "concept"},
                            {"id": "ML01-L12", "title": "Exercise: call a public API and parse the response", "type": "exercise"},
                            {"id": "ML01-L13", "title": "Quiz: coding essentials", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "ML01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "ML-02",
                "title": "Building Your First ML Model",
                "description": "End-to-end introduction to supervised machine learning with scikit-learn.",
                "prerequisites": "ML-01 or Python proficiency",
                "audience": "Developers new to machine learning",
                "sections": [
                    {
                        "title": "The ML Workflow",
                        "lessons": [
                            {"id": "ML02-L01", "title": "Course overview and the end-to-end ML pipeline", "type": "intro"},
                            {"id": "ML02-L02", "title": "Supervised vs unsupervised learning", "type": "concept"},
                            {"id": "ML02-L03", "title": "Train, validation, and test splits", "type": "concept"},
                            {"id": "ML02-L04", "title": "Feature engineering fundamentals", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Your First Model",
                        "lessons": [
                            {"id": "ML02-L05", "title": "Linear regression: intuition and implementation with scikit-learn", "type": "concept"},
                            {"id": "ML02-L06", "title": "Logistic regression for classification", "type": "concept"},
                            {"id": "ML02-L07", "title": "Model evaluation metrics: accuracy, precision, recall, F1, AUC", "type": "concept"},
                            {"id": "ML02-L08", "title": "Exercise: build and evaluate a classification model", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Improving Your Model",
                        "lessons": [
                            {"id": "ML02-L09", "title": "Overfitting and underfitting", "type": "concept"},
                            {"id": "ML02-L10", "title": "Cross-validation and hyperparameter tuning", "type": "concept"},
                            {"id": "ML02-L11", "title": "Baseline models and the iteration mindset", "type": "concept"},
                            {"id": "ML02-L12", "title": "Exercise: tune a model with GridSearchCV", "type": "exercise"},
                            {"id": "ML02-L13", "title": "Quiz: ML workflow", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "ML02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "ML-03",
                "title": "Foundational ML Algorithms",
                "description": "A practical tour of classical ML algorithms every AI engineer should know.",
                "prerequisites": "ML-02",
                "audience": "ML beginners building algorithmic literacy",
                "sections": [
                    {
                        "title": "Tree-Based Methods",
                        "lessons": [
                            {"id": "ML03-L01", "title": "Course overview", "type": "intro"},
                            {"id": "ML03-L02", "title": "Decision trees: splitting, depth, pruning", "type": "concept"},
                            {"id": "ML03-L03", "title": "Random forests and ensemble learning", "type": "concept"},
                            {"id": "ML03-L04", "title": "Gradient boosting: XGBoost and LightGBM in practice", "type": "concept"},
                            {"id": "ML03-L05", "title": "Exercise: compare tree models on a tabular dataset", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Distance and Probability-Based Methods",
                        "lessons": [
                            {"id": "ML03-L06", "title": "K-Nearest Neighbours: intuition and use cases", "type": "concept"},
                            {"id": "ML03-L07", "title": "Naive Bayes for text classification", "type": "concept"},
                            {"id": "ML03-L08", "title": "Support Vector Machines: margins and kernels", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Unsupervised Methods",
                        "lessons": [
                            {"id": "ML03-L09", "title": "K-Means clustering: algorithm and evaluation", "type": "concept"},
                            {"id": "ML03-L10", "title": "Dimensionality reduction: PCA and UMAP", "type": "concept"},
                            {"id": "ML03-L11", "title": "Exercise: segment a customer dataset with clustering", "type": "exercise"},
                            {"id": "ML03-L12", "title": "Quiz: foundational ML algorithms", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "ML03-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "DL-01",
                "title": "Introduction to Deep Learning using PyTorch",
                "description": "Build and train neural networks from scratch using PyTorch, from perceptrons to CNNs.",
                "prerequisites": "ML-02, Python proficiency",
                "audience": "ML engineers moving into deep learning",
                "sections": [
                    {
                        "title": "Neural Network Foundations",
                        "lessons": [
                            {"id": "DL01-L01", "title": "Course overview and PyTorch setup", "type": "intro"},
                            {"id": "DL01-L02", "title": "Tensors, autograd, and computation graphs", "type": "concept"},
                            {"id": "DL01-L03", "title": "Perceptrons to multilayer networks", "type": "concept"},
                            {"id": "DL01-L04", "title": "Activation functions: ReLU, sigmoid, softmax", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Training Neural Networks",
                        "lessons": [
                            {"id": "DL01-L05", "title": "Loss functions and the backpropagation algorithm", "type": "concept"},
                            {"id": "DL01-L06", "title": "Optimisers: SGD, Adam, learning rate scheduling", "type": "concept"},
                            {"id": "DL01-L07", "title": "Batch training, epochs, and the training loop", "type": "concept"},
                            {"id": "DL01-L08", "title": "Exercise: build and train a feedforward network on MNIST", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Deep Learning Best Practices",
                        "lessons": [
                            {"id": "DL01-L09", "title": "Overfitting in deep learning: dropout and batch normalisation", "type": "concept"},
                            {"id": "DL01-L10", "title": "Weight initialisation strategies", "type": "concept"},
                            {"id": "DL01-L11", "title": "Early stopping and model checkpointing", "type": "concept"},
                            {"id": "DL01-L12", "title": "Exercise: improve a model with regularisation techniques", "type": "exercise"},
                            {"id": "DL01-L13", "title": "Quiz: deep learning fundamentals", "type": "quiz"},
                        ]
                    },
                    {
                        "title": "Introduction to CNNs",
                        "lessons": [
                            {"id": "DL01-L14", "title": "Convolutional layers, pooling, and receptive fields", "type": "concept"},
                            {"id": "DL01-L15", "title": "Classic architectures: LeNet, AlexNet overview", "type": "concept"},
                            {"id": "DL01-L16", "title": "Transfer learning: using pretrained weights", "type": "concept"},
                            {"id": "DL01-L17", "title": "Exercise: classify images with a pretrained ResNet", "type": "exercise"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "DL01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "DL-02",
                "title": "Natural Language Processing using PyTorch",
                "description": "From tokenisation to transformers — NLP fundamentals with hands-on PyTorch implementation.",
                "prerequisites": "DL-01",
                "audience": "Deep learning engineers moving into NLP",
                "sections": [
                    {
                        "title": "Text as Data",
                        "lessons": [
                            {"id": "DL02-L01", "title": "Course overview and NLP landscape in 2026", "type": "intro"},
                            {"id": "DL02-L02", "title": "Tokenisation strategies: word, subword (BPE), character", "type": "concept"},
                            {"id": "DL02-L03", "title": "Embeddings: word2vec, GloVe, contextual embeddings", "type": "concept"},
                            {"id": "DL02-L04", "title": "Exercise: train a word embedding and visualise it", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Sequence Modelling",
                        "lessons": [
                            {"id": "DL02-L05", "title": "RNNs and the vanishing gradient problem", "type": "concept"},
                            {"id": "DL02-L06", "title": "LSTMs and GRUs: architecture and intuition", "type": "concept"},
                            {"id": "DL02-L07", "title": "Sequence-to-sequence models", "type": "concept"},
                            {"id": "DL02-L08", "title": "Exercise: build a text classifier with an LSTM", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "The Transformer Architecture",
                        "lessons": [
                            {"id": "DL02-L09", "title": "Self-attention mechanism from first principles", "type": "concept"},
                            {"id": "DL02-L10", "title": "Multi-head attention and positional encoding", "type": "concept"},
                            {"id": "DL02-L11", "title": "The encoder-decoder structure", "type": "concept"},
                            {"id": "DL02-L12", "title": "BERT and GPT-style architectures compared", "type": "concept"},
                            {"id": "DL02-L13", "title": "Exercise: fine-tune a BERT model for sentiment analysis", "type": "exercise"},
                            {"id": "DL02-L14", "title": "Quiz: NLP with PyTorch", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "DL02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "DL-03",
                "title": "Computer Vision using PyTorch",
                "description": "CNNs, object detection, segmentation, and vision-language models — end to end.",
                "prerequisites": "DL-01",
                "audience": "Engineers building vision-based AI systems",
                "sections": [
                    {
                        "title": "CV Foundations",
                        "lessons": [
                            {"id": "DL03-L01", "title": "Course overview and the CV problem space", "type": "intro"},
                            {"id": "DL03-L02", "title": "Image data: formats, channels, normalisation, augmentation", "type": "concept"},
                            {"id": "DL03-L03", "title": "Convolutional networks deep dive", "type": "concept"},
                            {"id": "DL03-L04", "title": "Exercise: build a CNN from scratch on CIFAR-10", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Advanced Architectures",
                        "lessons": [
                            {"id": "DL03-L05", "title": "ResNets, EfficientNet, and modern backbones", "type": "concept"},
                            {"id": "DL03-L06", "title": "Object detection: YOLO family overview", "type": "concept"},
                            {"id": "DL03-L07", "title": "Semantic segmentation fundamentals", "type": "concept"},
                            {"id": "DL03-L08", "title": "Exercise: object detection with a pretrained YOLO model", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Vision Transformers and Multimodal CV",
                        "lessons": [
                            {"id": "DL03-L09", "title": "Vision Transformers (ViT): how attention applies to images", "type": "concept"},
                            {"id": "DL03-L10", "title": "CLIP and vision-language models in practice", "type": "concept"},
                            {"id": "DL03-L11", "title": "Deploying a CV model: ONNX export and inference optimisation", "type": "concept"},
                            {"id": "DL03-L12", "title": "Exercise: build a zero-shot image classifier with CLIP", "type": "exercise"},
                            {"id": "DL03-L13", "title": "Quiz: computer vision with PyTorch", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "DL03-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "DM-01",
                "title": "Human Decision-Making and Its Biases",
                "description": "How cognitive science explains human decisions — and how those biases infect AI systems.",
                "prerequisites": "None",
                "audience": "AI practitioners, product leads, analysts",
                "sections": [
                    {
                        "title": "How Humans Decide",
                        "lessons": [
                            {"id": "DM01-L01", "title": "Course overview: why this matters for AI practitioners", "type": "intro"},
                            {"id": "DM01-L02", "title": "System 1 vs System 2 thinking (Kahneman framework)", "type": "concept"},
                            {"id": "DM01-L03", "title": "Cognitive biases: anchoring, availability, confirmation bias", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Biases in AI and Data Work",
                        "lessons": [
                            {"id": "DM01-L04", "title": "How cognitive bias enters datasets and model design", "type": "concept"},
                            {"id": "DM01-L05", "title": "Groupthink and authority bias in AI teams", "type": "concept"},
                            {"id": "DM01-L06", "title": "Debiasing techniques and structured critique", "type": "concept"},
                            {"id": "DM01-L07", "title": "Quiz: recognising and countering biases", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "DM01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "DM-02",
                "title": "Structured Approach to Problem Solving",
                "description": "MECE thinking, issue trees, and decision frameworks for AI engineers and analysts.",
                "prerequisites": "None",
                "audience": "Anyone building or shipping AI products",
                "sections": [
                    {
                        "title": "Problem Framing",
                        "lessons": [
                            {"id": "DM02-L01", "title": "Course overview", "type": "intro"},
                            {"id": "DM02-L02", "title": "Decomposing complex problems: issue trees and MECE thinking", "type": "concept"},
                            {"id": "DM02-L03", "title": "Root cause analysis: 5 Whys and fishbone diagrams", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Decision Frameworks",
                        "lessons": [
                            {"id": "DM02-L04", "title": "Hypothesis-driven analysis", "type": "concept"},
                            {"id": "DM02-L05", "title": "Trade-off evaluation: criteria matrices and weighted scoring", "type": "concept"},
                            {"id": "DM02-L06", "title": "Communicating decisions to technical and non-technical audiences", "type": "concept"},
                            {"id": "DM02-L07", "title": "Quiz: structured problem solving", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "DM02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "FT-01",
                "title": "Finetuning LLMs",
                "description": "LoRA, QLoRA, SFT, and evaluation — everything needed to adapt an LLM to a custom task.",
                "prerequisites": "DL-01, basic LLM familiarity",
                "audience": "ML engineers building domain-specific models",
                "sections": [
                    {
                        "title": "Why Finetune?",
                        "lessons": [
                            {"id": "FT01-L01", "title": "Course overview and environment setup", "type": "intro"},
                            {"id": "FT01-L02", "title": "When to finetune vs prompt engineer vs RAG", "type": "concept"},
                            {"id": "FT01-L03", "title": "Types of finetuning: full, PEFT, LoRA, QLoRA", "type": "concept"},
                            {"id": "FT01-L04", "title": "Dataset preparation: formats, quality, and size considerations", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Running a Finetune",
                        "lessons": [
                            {"id": "FT01-L05", "title": "Supervised finetuning (SFT) with Hugging Face Transformers", "type": "concept"},
                            {"id": "FT01-L06", "title": "LoRA finetuning in practice: config, training loop, monitoring", "type": "concept"},
                            {"id": "FT01-L07", "title": "Exercise: finetune a small model on a custom instruction dataset", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Evaluation and Deployment",
                        "lessons": [
                            {"id": "FT01-L08", "title": "Evaluating finetuned models: benchmarks vs task-specific evals", "type": "concept"},
                            {"id": "FT01-L09", "title": "Merging LoRA adapters and quantisation", "type": "concept"},
                            {"id": "FT01-L10", "title": "Serving a finetuned model with vLLM or Ollama", "type": "concept"},
                            {"id": "FT01-L11", "title": "Exercise: evaluate and serve your finetuned model", "type": "exercise"},
                            {"id": "FT01-L12", "title": "Quiz: LLM finetuning", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "FT01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "FT-02",
                "title": "Training LLMs from Scratch",
                "description": "Pretraining data pipelines, GPT architecture, distributed training, and post-training alignment.",
                "prerequisites": "DL-01, DL-02, FT-01",
                "audience": "Senior ML engineers and researchers",
                "sections": [
                    {
                        "title": "Architecture and Data",
                        "lessons": [
                            {"id": "FT02-L01", "title": "Course overview: scope, scale, and prerequisites", "type": "intro"},
                            {"id": "FT02-L02", "title": "GPT-style decoder architecture in detail", "type": "concept"},
                            {"id": "FT02-L03", "title": "Pretraining data: sources, cleaning, deduplication, tokenisation", "type": "concept"},
                            {"id": "FT02-L04", "title": "Exercise: build a minimal GPT in PyTorch", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "The Pretraining Process",
                        "lessons": [
                            {"id": "FT02-L05", "title": "Distributed training fundamentals: data and model parallelism", "type": "concept"},
                            {"id": "FT02-L06", "title": "Mixed precision training and gradient checkpointing", "type": "concept"},
                            {"id": "FT02-L07", "title": "Training monitoring: loss curves, gradient norms, LR warmup", "type": "concept"},
                            {"id": "FT02-L08", "title": "Exercise: pretrain a small language model on a domain corpus", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Post-Pretraining",
                        "lessons": [
                            {"id": "FT02-L09", "title": "Instruction tuning and RLHF overview", "type": "concept"},
                            {"id": "FT02-L10", "title": "DPO and RLAIF as RLHF alternatives", "type": "concept"},
                            {"id": "FT02-L11", "title": "Scaling laws and practical trade-offs for small teams", "type": "concept"},
                            {"id": "FT02-L12", "title": "Quiz: training LLMs from scratch", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "FT02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "FT-03",
                "title": "Mastering Reinforcement Learning: Foundations to Human Feedback",
                "description": "RL fundamentals, deep RL, PPO, and the RLHF pipeline used to align modern LLMs.",
                "prerequisites": "DL-01, Python proficiency",
                "audience": "ML engineers working on model alignment and advanced training",
                "sections": [
                    {
                        "title": "RL Fundamentals",
                        "lessons": [
                            {"id": "FT03-L01", "title": "Course overview", "type": "intro"},
                            {"id": "FT03-L02", "title": "Agents, environments, rewards, and the Markov decision process", "type": "concept"},
                            {"id": "FT03-L03", "title": "Policy gradient methods: REINFORCE", "type": "concept"},
                            {"id": "FT03-L04", "title": "Exercise: train an agent on a simple Gym environment", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Deep RL",
                        "lessons": [
                            {"id": "FT03-L05", "title": "Deep Q-Networks (DQN) and experience replay", "type": "concept"},
                            {"id": "FT03-L06", "title": "Actor-Critic methods: A2C and PPO", "type": "concept"},
                            {"id": "FT03-L07", "title": "Exercise: train a PPO agent on a control task", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "RL from Human Feedback",
                        "lessons": [
                            {"id": "FT03-L08", "title": "RLHF pipeline: reward modelling and PPO finetuning", "type": "concept"},
                            {"id": "FT03-L09", "title": "Constitutional AI and RLAIF", "type": "concept"},
                            {"id": "FT03-L10", "title": "DPO: direct preference optimisation as a simpler alternative", "type": "concept"},
                            {"id": "FT03-L11", "title": "Practical RLHF at small scale with TRL", "type": "concept"},
                            {"id": "FT03-L12", "title": "Quiz: RL and RLHF", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "FT03-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "SD-01",
                "title": "Getting Started with Stable Diffusion",
                "description": "Diffusion model intuition, text-to-image generation, and core prompting techniques.",
                "prerequisites": "Basic Python, F-01",
                "audience": "Developers and creators entering generative image AI",
                "sections": [
                    {
                        "title": "Diffusion Model Intuition",
                        "lessons": [
                            {"id": "SD01-L01", "title": "Course overview and setup (ComfyUI / diffusers)", "type": "intro"},
                            {"id": "SD01-L02", "title": "How diffusion models work: forward and reverse process", "type": "concept"},
                            {"id": "SD01-L03", "title": "CLIP, VAE, and the UNet: the three-component architecture", "type": "concept"},
                            {"id": "SD01-L04", "title": "Text-to-image: your first generation", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Core Techniques",
                        "lessons": [
                            {"id": "SD01-L05", "title": "Prompt engineering for images: positive and negative prompts", "type": "concept"},
                            {"id": "SD01-L06", "title": "Sampler choices and their effects (Euler, DPM++, DDIM)", "type": "concept"},
                            {"id": "SD01-L07", "title": "CFG scale, steps, and resolution trade-offs", "type": "concept"},
                            {"id": "SD01-L08", "title": "Exercise: produce consistent character outputs with prompt iteration", "type": "exercise"},
                            {"id": "SD01-L09", "title": "Quiz: stable diffusion foundations", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "SD01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "SD-02",
                "title": "Mastering Methods and Tools of Stable Diffusion",
                "description": "ControlNet, LoRA fine-tunes, ComfyUI workflows, and the 2026 model landscape.",
                "prerequisites": "SD-01",
                "audience": "Developers and creators building production image pipelines",
                "sections": [
                    {
                        "title": "Advanced Control",
                        "lessons": [
                            {"id": "SD02-L01", "title": "Course overview", "type": "intro"},
                            {"id": "SD02-L02", "title": "ControlNet: depth, canny, pose, and scribble maps", "type": "concept"},
                            {"id": "SD02-L03", "title": "Image-to-image and inpainting workflows", "type": "concept"},
                            {"id": "SD02-L04", "title": "LoRA and embedding fine-tunes for style and character", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Production Workflows",
                        "lessons": [
                            {"id": "SD02-L05", "title": "ComfyUI node graphs for repeatable pipelines", "type": "concept"},
                            {"id": "SD02-L06", "title": "Batch generation and automation with the diffusers API", "type": "concept"},
                            {"id": "SD02-L07", "title": "SDXL, SD3, and Flux: the 2026 model landscape", "type": "concept"},
                            {"id": "SD02-L08", "title": "Exercise: build an end-to-end image generation pipeline", "type": "exercise"},
                            {"id": "SD02-L09", "title": "Quiz: advanced stable diffusion", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "SD02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "GL-01",
                "title": "Generative AI for Business: A Leaders' Handbook",
                "description": "Non-technical executive guide to evaluating, adopting, and governing generative AI.",
                "prerequisites": "None",
                "audience": "Business leaders, product owners, C-suite",
                "sections": [
                    {
                        "title": "Understanding the Technology",
                        "lessons": [
                            {"id": "GL01-L01", "title": "Course overview: written for leaders, not engineers", "type": "intro"},
                            {"id": "GL01-L02", "title": "What generative AI can and cannot do reliably", "type": "concept"},
                            {"id": "GL01-L03", "title": "The build vs buy vs partner decision", "type": "concept"},
                            {"id": "GL01-L04", "title": "Estimating ROI and avoiding hype-driven investments", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Leading AI Transformation",
                        "lessons": [
                            {"id": "GL01-L05", "title": "Identifying high-value use cases in your organisation", "type": "concept"},
                            {"id": "GL01-L06", "title": "Data readiness and infrastructure basics for leaders", "type": "concept"},
                            {"id": "GL01-L07", "title": "Change management, workforce upskilling, and ethical governance", "type": "concept"},
                            {"id": "GL01-L08", "title": "Quiz: GenAI for business leaders", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "GL01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "GL-02",
                "title": "Successful AI Strategies: A CEO's Perspective",
                "description": "Strategic frameworks for embedding AI into core operations and building durable competitive advantage.",
                "prerequisites": "GL-01 recommended",
                "audience": "CEOs, founders, and senior strategy leaders",
                "sections": [
                    {
                        "title": "Strategic Framing",
                        "lessons": [
                            {"id": "GL02-L01", "title": "Course overview", "type": "intro"},
                            {"id": "GL02-L02", "title": "How top companies are embedding AI into core operations", "type": "concept"},
                            {"id": "GL02-L03", "title": "Competitive moats in the AI era: data, distribution, and speed", "type": "concept"},
                            {"id": "GL02-L04", "title": "Common strategic mistakes and how to avoid them", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Execution and Culture",
                        "lessons": [
                            {"id": "GL02-L05", "title": "Building AI-native teams vs retrofitting existing ones", "type": "concept"},
                            {"id": "GL02-L06", "title": "Vendor and partnership evaluation frameworks", "type": "concept"},
                            {"id": "GL02-L07", "title": "Measuring AI impact: metrics that actually matter", "type": "concept"},
                            {"id": "GL02-L08", "title": "Quiz: AI strategy for CEOs", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "GL02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

        ]
    },

    "track2_agentic_ai": {
        "label": "Agentic AI & Automation Tools",
        "description": (
            "LLM application development, RAG systems, agent frameworks (LangChain, LangGraph, AutoGen, CrewAI), "
            "and production deployment. Assumes Python fluency and basic ML literacy."
        ),
        "courses": [

            {
                "id": "LLM-01",
                "title": "Getting Started with Large Language Models",
                "description": "How LLMs work, the 2026 model landscape, and making your first production-quality API calls.",
                "prerequisites": "Python proficiency, ML-01",
                "audience": "Developers entering LLM application development",
                "sections": [
                    {
                        "title": "LLM Foundations",
                        "lessons": [
                            {"id": "LLM01-L01", "title": "Course overview and prerequisites check", "type": "intro"},
                            {"id": "LLM01-L02", "title": "How LLMs work: tokens, context windows, next-token prediction", "type": "concept"},
                            {"id": "LLM01-L03", "title": "Key model families in 2026: GPT-4o, Claude, Gemini, Llama, Mistral", "type": "concept"},
                            {"id": "LLM01-L04", "title": "Accessing models: APIs vs local inference (Ollama, llama.cpp)", "type": "concept"},
                        ]
                    },
                    {
                        "title": "Working with LLMs",
                        "lessons": [
                            {"id": "LLM01-L05", "title": "Making your first API call (OpenAI-compatible interface)", "type": "concept"},
                            {"id": "LLM01-L06", "title": "Understanding model parameters: temperature, top-p, max tokens", "type": "concept"},
                            {"id": "LLM01-L07", "title": "System prompts and roles", "type": "concept"},
                            {"id": "LLM01-L08", "title": "Structured output: JSON mode and response schemas", "type": "concept"},
                            {"id": "LLM01-L09", "title": "Exercise: build a Q&A interface with streaming responses", "type": "exercise"},
                            {"id": "LLM01-L10", "title": "Quiz: LLM fundamentals", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "LLM01-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "LLM-02",
                "title": "Introduction to LangChain for Agentic AI",
                "description": "LangChain 0.3 architecture, LCEL pipelines, retrieval chains, and your first LangChain agent.",
                "prerequisites": "LLM-01",
                "audience": "Developers building LLM-powered applications",
                "sections": [
                    {
                        "title": "LangChain Architecture",
                        "lessons": [
                            {"id": "LLM02-L01", "title": "Course overview and LangChain 0.3 setup", "type": "intro"},
                            {"id": "LLM02-L02", "title": "Core abstractions: models, prompts, chains, memory", "type": "concept"},
                            {"id": "LLM02-L03", "title": "LCEL (LangChain Expression Language) for composing pipelines", "type": "concept"},
                            {"id": "LLM02-L04", "title": "Exercise: build a multi-turn conversational chain", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Tools and Retrieval",
                        "lessons": [
                            {"id": "LLM02-L05", "title": "Integrating tools: search, calculators, custom APIs", "type": "concept"},
                            {"id": "LLM02-L06", "title": "Document loaders, text splitters, and vector stores", "type": "concept"},
                            {"id": "LLM02-L07", "title": "Building a retrieval chain", "type": "concept"},
                            {"id": "LLM02-L08", "title": "Exercise: build a document QA system with LangChain and Chroma", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Agents in LangChain",
                        "lessons": [
                            {"id": "LLM02-L09", "title": "Agent types: ReAct and structured output agents", "type": "concept"},
                            {"id": "LLM02-L10", "title": "Tool calling with modern LangChain agents", "type": "concept"},
                            {"id": "LLM02-L11", "title": "Debugging and tracing with LangSmith", "type": "concept"},
                            {"id": "LLM02-L12", "title": "Exercise: build a research agent with web search and memory", "type": "exercise"},
                            {"id": "LLM02-L13", "title": "Quiz: LangChain fundamentals", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "LLM02-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "LLM-03",
                "title": "Prompt Engineering Essentials",
                "description": "Zero-shot, few-shot, chain-of-thought, ReAct, and a systematic approach to building and evaluating prompts.",
                "prerequisites": "LLM-01",
                "audience": "Developers and product builders working with LLMs daily",
                "sections": [
                    {
                        "title": "Writing Effective Prompts",
                        "lessons": [
                            {"id": "LLM03-L01", "title": "Course overview: the prompt engineering mindset", "type": "intro"},
                            {"id": "LLM03-L02", "title": "Zero-shot and few-shot prompting", "type": "concept"},
                            {"id": "LLM03-L03", "title": "Chain-of-thought and step-by-step reasoning", "type": "concept"},
                            {"id": "LLM03-L04", "title": "Role prompting and persona design", "type": "concept"},
                            {"id": "LLM03-L05", "title": "Exercise: improve a failing prompt systematically", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Advanced Techniques",
                        "lessons": [
                            {"id": "LLM03-L06", "title": "XML tagging and structured prompt formats", "type": "concept"},
                            {"id": "LLM03-L07", "title": "Self-consistency and majority voting", "type": "concept"},
                            {"id": "LLM03-L08", "title": "Tree of Thought and ReAct prompting patterns", "type": "concept"},
                            {"id": "LLM03-L09", "title": "Prompt injection risks and defences", "type": "concept"},
                            {"id": "LLM03-L10", "title": "Exercise: design a robust prompt for a production task", "type": "exercise"},
                        ]
                    },
                    {
                        "title": "Evaluating Prompts",
                        "lessons": [
                            {"id": "LLM03-L11", "title": "Building a prompt eval harness", "type": "concept"},
                            {"id": "LLM03-L12", "title": "LLM-as-judge evaluation", "type": "concept"},
                            {"id": "LLM03-L13", "title": "Iterating on prompts with data, not intuition", "type": "concept"},
                            {"id": "LLM03-L14", "title": "Quiz: prompt engineering", "type": "quiz"},
                        ]
                    },
                    {"title": "Final Assessment", "lessons": [
                        {"id": "LLM03-FA", "title": "Final Assessment", "type": "final_assessment"}
                    ]},
                ]
            },

            {
                "id": "RAG-01",
                "title": "RAG Sy
<truncated 40240 bytes>

NOTE: The output was truncated because it was too long. Use a more targeted query or a smaller range to get the information you need.