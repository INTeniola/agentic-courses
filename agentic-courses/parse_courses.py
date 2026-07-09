import json
import re

# Raw text from the user request
RAW_TEXT = """
Track 1: AI / ML Foundations

F-01 — Explore the GenAI Universe
Section 1: What is Generative AI?
Welcome and course overview
From discriminative to generative models
Key modalities: text, image, audio, code, multimodal
Quiz: What is Generative AI?
Section 2: The GenAI Landscape
Foundational model families (LLMs, diffusion, multimodal)
Key players and open-source ecosystem (2026 landscape)
The AI development stack: data, compute, frameworks, APIs
Real-world applications and industry use cases
Final Assessment

F-02 — Responsible AI in the Generative AI Era
Section 1: Core Principles
Why responsible AI matters now more than ever
Bias, fairness, and representation in generative models
Hallucination, factuality, and reliability challenges
Section 2: Risk and Governance
Safety, alignment, and RLHF: the basic picture
AI regulations and compliance landscape (EU AI Act, Nigeria NDPC)
Evaluating your own AI products responsibly
Quiz: Responsible AI principles
Final Assessment

ML-01 — Coding Essentials for Agents
Section 1: Python Foundations for AI
Course overview and environment setup (Colab/VS Code)
Python data structures agents rely on: lists, dicts, sets
Functions, classes, and modular code design
Exercise: build a simple data pipeline in Python
Section 2: Working with Data
NumPy essentials: arrays, broadcasting, vectorisation
Pandas for structured data manipulation
Reading and writing JSON, CSV, and API responses
Exercise: explore and clean a real dataset
Section 3: Practical Python for AI Workflows
Async programming basics: why agents need it
HTTP requests, REST APIs, and error handling
Intro to environment variables and secrets management
Exercise: call a public API and parse the response
Quiz: coding essentials
Final Assessment

ML-02 — Building Your First ML Model
Section 1: The ML Workflow
Course overview and the end-to-end ML pipeline
Supervised vs unsupervised learning
Train, validation, and test splits
Feature engineering fundamentals
Section 2: Your First Model
Linear regression: intuition and implementation (scikit-learn)
Logistic regression for classification
Model evaluation metrics: accuracy, precision, recall, F1, AUC
Exercise: build and evaluate a classification model
Section 3: Improving Your Model
Overfitting and underfitting
Cross-validation and hyperparameter tuning
Baseline models and iteration mindset
Exercise: tune a model with GridSearchCV
Quiz: ML workflow
Final Assessment

ML-03 — Foundational ML Algorithms
Section 1: Tree-Based Methods
Decision trees: splitting, depth, pruning
Random forests and ensemble learning
Gradient boosting: XGBoost and LightGBM in practice
Exercise: compare tree models on a tabular dataset
Section 2: Distance and Probability-Based Methods
K-Nearest Neighbours: intuition and use cases
Naive Bayes for text classification
Support Vector Machines: margins and kernels
Section 3: Unsupervised Methods
K-Means clustering: algorithm and evaluation
Dimensionality reduction: PCA and UMAP
Exercise: segment a customer dataset with clustering
Quiz: foundational ML algorithms
Final Assessment

DL-01 — Introduction to Deep Learning using PyTorch
Section 1: Neural Network Foundations
Course overview and PyTorch setup
Tensors, autograd, and computation graphs
Perceptrons to multilayer networks
Activation functions: ReLU, sigmoid, softmax
Section 2: Training Neural Networks
Loss functions and the backpropagation algorithm
Optimisers: SGD, Adam, learning rate scheduling
Batch training, epochs, and the training loop
Exercise: build and train a feedforward network on MNIST
Section 3: Deep Learning Best Practices
Overfitting in deep learning: dropout and batch normalisation
Weight initialisation strategies
Early stopping and model checkpointing
Exercise: improve a model with regularisation techniques
Quiz: deep learning fundamentals
Section 4: Introduction to CNNs
Convolutional layers, pooling, and receptive fields
Classic architectures: LeNet, AlexNet overview
Transfer learning: using pretrained weights
Exercise: classify images with a pretrained ResNet
Final Assessment

DL-02 — Natural Language Processing using PyTorch
Section 1: Text as Data
Course overview and NLP landscape in 2026
Tokenisation strategies: word, subword (BPE), character
Embeddings: word2vec, GloVe, contextual embeddings
Exercise: train a word embedding and visualise it
Section 2: Sequence Modelling
RNNs and the vanishing gradient problem
LSTMs and GRUs: architecture and intuition
Sequence-to-sequence models
Exercise: build a text classifier with an LSTM
Section 3: The Transformer Architecture
Self-attention mechanism from first principles
Multi-head attention and positional encoding
The encoder-decoder structure
BERT and GPT-style architectures compared
Exercise: fine-tune a BERT model for sentiment analysis
Quiz: NLP with PyTorch
Final Assessment

DL-03 — Computer Vision using PyTorch
Section 1: CV Foundations
Course overview and the computer vision problem space
Image data: formats, channels, normalisation, augmentation
Convolutional networks deep dive
Exercise: build a CNN from scratch on CIFAR-10
Section 2: Advanced Architectures
ResNets, EfficientNet, and modern backbones
Object detection: YOLO family overview
Semantic segmentation fundamentals
Exercise: object detection with a pretrained YOLO model
Section 3: Vision Transformers and Multimodal CV
Vision Transformers (ViT): how attention applies to images
CLIP and vision-language models in practice
Deploying a CV model: ONNX export and inference optimisation
Exercise: build a zero-shot image classifier with CLIP
Quiz: computer vision with PyTorch
Final Assessment

DM-01 — Human Decision-Making and Its Biases
Section 1: How Humans Decide
Course overview: why this matters for AI practitioners
System 1 vs System 2 thinking (Kahneman framework)
Cognitive biases: anchoring, availability, confirmation bias
Section 2: Biases in AI and Data Work
How cognitive bias enters datasets and model design
Groupthink and authority bias in AI teams
Debiasing techniques and structured critique
Quiz: recognising and countering biases
Final Assessment

DM-02 — Structured Approach to Problem Solving
Section 1: Problem Framing
Course overview
Decomposing complex problems: issue trees and MECE thinking
Root cause analysis: 5 Whys and fishbone diagrams
Section 2: Decision Frameworks
Hypothesis-driven analysis
Trade-off evaluation: criteria matrices and weighted scoring
Communicating decisions clearly to technical and non-technical audiences
Quiz: structured problem solving
Final Assessment

FT-01 — Finetuning LLMs
Section 1: Why Finetune?
Course overview and environment setup
When to finetune vs prompt engineer vs RAG
Types of finetuning: full, PEFT, LoRA, QLoRA
Dataset preparation: formats, quality, and size considerations
Section 2: Running a Finetune
Supervised finetuning (SFT) with Hugging Face Transformers
LoRA finetuning in practice: config, training loop, monitoring
Exercise: finetune a small model on a custom instruction dataset
Section 3: Evaluation and Deployment
Evaluating finetuned models: benchmarks vs task-specific evals
Merging LoRA adapters and quantisation
Serving a finetuned model with vLLM or Ollama
Exercise: evaluate and serve your finetuned model
Quiz: LLM finetuning
Final Assessment

FT-02 — Training LLMs from Scratch
Section 1: Architecture and Data
Course overview: scope, scale, and prerequisites
GPT-style decoder architecture in detail
Pretraining data: sources, cleaning, deduplication, tokenisation
Exercise: build a minimal GPT in PyTorch
Section 2: The Pretraining Process
Distributed training fundamentals: data parallelism, model parallelism
Mixed precision training and gradient checkpointing
Training monitoring: loss curves, gradient norms, learning rate warmup
Exercise: pretrain a small language model on a domain corpus
Section 3: Post-Pretraining
Instruction tuning and RLHF overview
DPO and RLAIF as RLHF alternatives
Scaling laws and practical trade-offs for small teams
Quiz: training LLMs from scratch
Final Assessment

FT-03 — Mastering Reinforcement Learning: Foundations to Human Feedback
Section 1: RL Fundamentals
Course overview
Agents, environments, rewards, and the Markov decision process
Policy gradient methods: REINFORCE
Exercise: train an agent on a simple Gym environment
Section 2: Deep RL
Deep Q-Networks (DQN) and experience replay
Actor-Critic methods: A2C and PPO
Exercise: train a PPO agent on a control task
Section 3: RL from Human Feedback
RLHF pipeline: reward modelling and PPO finetuning
Constitutional AI and RLAIF
DPO: direct preference optimisation as a simpler alternative
Practical RLHF at small scale with TRL
Quiz: RL and RLHF
Final Assessment

SD-01 — Getting Started with Stable Diffusion
Section 1: Diffusion Model Intuition
Course overview and setup (ComfyUI / diffusers)
How diffusion models work: forward and reverse process
CLIP, VAE, and the UNet: the three-component architecture
Text-to-image: your first generation
Section 2: Core Techniques
Prompt engineering for images: positive and negative prompts
Sampler choices and their effects (Euler, DPM++, DDIM)
CFG scale, steps, and resolution trade-offs
Exercise: produce consistent character outputs with prompt iteration
Quiz: stable diffusion foundations
Final Assessment

SD-02 — Mastering Methods and Tools of Stable Diffusion
Section 1: Advanced Control
Course overview
ControlNet: depth, canny, pose, and scribble maps
Image-to-image and inpainting workflows
LoRA and embedding fine-tunes for style and character
Section 2: Production Workflows
ComfyUI node graphs for repeatable pipelines
Batch generation and automation with the diffusers API
SDXL, SD3, and Flux: the 2026 model landscape
Exercise: build an end-to-end image generation pipeline
Quiz: advanced stable diffusion
Final Assessment

GL-01 — Generative AI for Business: A Leaders' Handbook
Section 1: Understanding the Technology
Course overview: written for leaders, not engineers
What generative AI can and cannot do reliably
The build vs buy vs partner decision
Estimating ROI and avoiding hype-driven investments
Section 2: Leading AI Transformation
Identifying high-value use cases in your organisation
Data readiness and infrastructure basics for leaders
Change management, workforce upskilling, and ethical governance
Quiz: GenAI for business leaders
Final Assessment

GL-02 — Successful AI Strategies: A CEO's Perspective
Section 1: Strategic Framing
Course overview
How top companies are embedding AI into core operations
Competitive moats in the AI era: data, distribution, and speed
Common strategic mistakes and how to avoid them
Section 2: Execution and Culture
Building AI-native teams vs retrofitting existing ones
Vendor and partnership evaluation frameworks
Measuring AI impact: metrics that actually matter
Quiz: AI strategy for CEOs
Final Assessment

Track 2: Agentic AI & Automation Tools

LLM-01 — Getting Started with Large Language Models
Section 1: LLM Foundations
Course overview and prerequisites check
How LLMs work: tokens, context windows, next-token prediction
Key model families in 2026: GPT-4o, Claude, Gemini, Llama, Mistral
Accessing models: APIs vs local inference (Ollama, llama.cpp)
Section 2: Working with LLMs
Making your first API call (OpenAI-compatible interface)
Understanding model parameters: temperature, top-p, max tokens
System prompts and roles
Structured output: JSON mode and response schemas
Exercise: build a simple Q&A interface with streaming responses
Quiz: LLM fundamentals
Final Assessment

LLM-02 — Introduction to LangChain for Agentic AI
Section 1: LangChain Architecture
Course overview and LangChain 0.3 setup
Core abstractions: models, prompts, chains, memory
LCEL (LangChain Expression Language) for composing pipelines
Exercise: build a multi-turn conversational chain
Section 2: Tools and Retrieval
Integrating tools: search, calculators, APIs
Document loaders, text splitters, and vector stores
Building a simple retrieval chain
Exercise: build a document QA system with LangChain and Chroma
Section 3: Agents in LangChain
Agent types: ReAct, structured output agents
Tool calling with modern LangChain agents
Debugging and tracing with LangSmith
Exercise: build a research agent with web search and memory
Quiz: LangChain fundamentals
Final Assessment

LLM-03 — Prompt Engineering Essentials
Section 1: Writing Effective Prompts
Course overview: the prompt engineering mindset
Zero-shot and few-shot prompting
Chain-of-thought and step-by-step reasoning
Role prompting and persona design
Exercise: improve a failing prompt systematically
Section 2: Advanced Techniques
XML tagging and structured prompt formats
Self-consistency and majority voting
Tree of Thought and ReAct prompting patterns
Prompt injection risks and defences
Exercise: design a robust prompt for a production task
Section 3: Evaluating Prompts
Building a prompt eval harness
LLM-as-judge evaluation
Iterating on prompts with data, not intuition
Quiz: prompt engineering
Final Assessment

RAG-01 — RAG Systems Essentials
Section 1: Why RAG?
Course overview
The knowledge gap problem in LLMs
RAG vs finetuning vs context stuffing: when to use each
The core RAG pipeline: index, retrieve, generate
Section 2: Building a RAG Pipeline
Document loading and preprocessing strategies
Chunking: fixed-size, semantic, and hierarchical approaches
Embedding models: choosing and comparing (2026 landscape)
Vector databases: Chroma, Pinecone, Weaviate, pgvector
Exercise: build a local RAG system from scratch
Section 3: Retrieval Quality
Lexical search: BM25 and keyword retrieval
Hybrid search: combining dense and sparse retrieval
Reranking with cross-encoders
Evaluating retrieval: recall, MRR, NDCG
Exercise: implement and benchmark hybrid retrieval
Quiz: RAG essentials
Final Assessment

RAG-02 — Building Production-Ready RAG Systems using LlamaIndex
Section 1: LlamaIndex Architecture
Course overview and LlamaIndex 0.12 setup
Core abstractions: nodes, indices, query engines, pipelines
Ingestion pipeline: connectors, transformations, embeddings
Exercise: build a multi-document query engine
Section 2: Advanced RAG Patterns
Contextual retrieval and late chunking
Recursive and small-to-big retrieval
Query routing and multi-index strategies
Sub-question decomposition
Exercise: implement advanced retrieval on a real corpus
Section 3: Productionising RAG
Metadata filtering and access control
Caching strategies for latency and cost
RAG observability with Arize Phoenix or LlamaTrace
Evaluation frameworks: RAGAs and TruLens
Exercise: end-to-end evaluation of a production RAG pipeline
Quiz: production RAG with LlamaIndex
Final Assessment

RAG-03 — Building End-to-End Generative AI Applications
Section 1: Application Architecture
Course overview
Full-stack AI app architecture: backend, frontend, vector store, LLM
Selecting your stack: FastAPI, Next.js, Streamlit trade-offs
Auth, rate limiting, and cost controls for LLM APIs
Section 2: Building the Application
Building a REST API backend with FastAPI and LangChain
Streaming responses to the frontend
Conversation memory and session management
Exercise: build a full-stack document assistant
Section 3: Deployment and Monitoring
Containerising with Docker and deploying to cloud (AWS/GCP/Azure)
LLM observability: logging, tracing, and alerting
Cost optimisation: caching, model routing, and batching
Exercise: deploy your application with CI/CD
Quiz: end-to-end GenAI applications
Final Assessment

AG-01 — Anyone Can Build AI Agents
Section 1: Agent Intuition
Course overview: no prior agent experience needed
What is an AI agent? Perception, reasoning, action loop
Tools, memory, and planning: the three pillars
Five real-world agent use cases dissected
Section 2: Your First Agent
Building a minimal agent loop in plain Python
Adding tools: web search, calculator, file reader
Giving your agent memory
Exercise: build a personal research assistant agent
Quiz: agent fundamentals
Final Assessment

AG-02 — Architecting Agentic AI: Design Patterns and Practices
Section 1: Agent Architecture Patterns
Course overview
Single-agent vs multi-agent systems
Workflow patterns: chaining, routing, parallelisation, orchestrator-subagent
When agents fail: error handling and fallback design
Section 2: Design for Production
State management in long-running agents
Human-in-the-loop design: approval gates and interrupts
Security considerations: prompt injection, tool misuse
Observability and debugging agent behaviour
Exercise: architect a multi-agent workflow for a business process
Quiz: agentic system design
Final Assessment

AG-03 — Building AI Agents from Scratch
Section 1: Core Agent Components
Course overview and repository setup
Building the ReAct loop: thought, action, observation
Tool definition and JSON schema for function calling
Memory systems: in-context, episodic, semantic
Section 2: Agent Capabilities
Multi-step planning and task decomposition
Handling tool errors and retrying gracefully
Streaming agent output to users
Exercise: build a fully functional research-and-report agent
Section 3: Testing and Hardening
Unit testing agent tools
Adversarial testing: prompt injection and edge cases
Agent evaluation frameworks
Exercise: write an evaluation harness for your agent
Quiz: building agents from scratch
Final Assessment

AG-04 — Building AI Agents with LangChain
Section 1: LangChain Agents Deep Dive
Course overview
Modern LangChain agent architecture (LCEL-based)
Defining and binding custom tools
Structured output agents and forced tool use
Exercise: build a tool-using customer support agent
Section 2: Advanced Agent Features
Multi-agent orchestration with LangChain
Stateful agents with checkpointing
Human-in-the-loop with interrupt and resume
LangSmith for production tracing and evals
Exercise: build a multi-agent pipeline with LangSmith observability
Quiz: agents with LangChain
Final Assessment

GS-01 — Building Your First AI Agent with LangGraph
Section 1: LangGraph Foundations
Course overview and LangGraph 0.3 setup
Graphs, nodes, edges, and state: the core abstractions
StateGraph vs MessageGraph
Your first LangGraph workflow
Exercise: build a simple document summarisation graph
Section 2: Building a Real Agent
Adding conditional edges and routing logic
Tool nodes and the ToolNode helper
Checkpointing state for persistence
Streaming graph execution output
Exercise: build a ReAct agent in LangGraph with memory
Quiz: LangGraph fundamentals
Final Assessment

GS-02 — Building Your First AI Agent with CrewAI
Section 1: CrewAI Foundations
Course overview and CrewAI 0.8 setup
Crews, agents, tasks, and tools: the four building blocks
Role-based agent design: how to define effective agents
Exercise: create a two-agent research crew
Section 2: Building a Real Crew
Sequential vs hierarchical process execution
Defining tasks with expected output schemas
Using built-in and custom tools
Inter-agent delegation and collaboration
Exercise: build a content pipeline crew (researcher + writer + editor)
Quiz: CrewAI fundamentals
Final Assessment

ADV-01 — Building Advanced AI Agents with LangGraph
Section 1: Advanced Graph Patterns
Course overview and prerequisites
Subgraphs and nested graph composition
Parallelism with fan-out and fan-in nodes
Dynamic graph construction at runtime
Section 2: Production-Grade Agents
Long-running agent persistence with LangGraph Platform
Streaming, interrupts, and time-travel debugging
Multi-agent networks: supervisor and swarm topologies
Custom reducers and complex state management
Exercise: build a multi-agent research system with supervisor routing
Section 3: Evaluation and Deployment
Agent evaluation with LangSmith datasets and CI evals
Deploying to LangGraph Cloud
Cost and latency profiling
Exercise: deploy and monitor an advanced agent pipeline
Quiz: advanced LangGraph
Final Assessment

ADV-02 — Building Advanced AI Agents with AutoGen
Section 1: AutoGen Architecture
Course overview and AutoGen 0.4 setup (AgentChat and Core APIs)
Conversable agents, assistant agents, and user proxy agents
Group chat and round-robin vs selector orchestration
Exercise: build a code-writing and execution team
Section 2: Advanced Patterns
Custom agents and message routing
Termination conditions and safety patterns
Tool use in AutoGen: function calling and code execution sandbox
Nested chats and composable conversation patterns
Exercise: build a multi-agent debugging and code review system
Section 3: Observability and Deployment
Tracing with OpenTelemetry in AutoGen
Distributed agents with AutoGen's actor model
Evaluation and regression testing
Quiz: advanced AutoGen
Final Assessment

ADV-03 — Building Advanced AI Agents with CrewAI
Section 1: Advanced CrewAI Features
Course overview
Hierarchical process with manager agents
Asynchronous task execution and parallelism
Custom tool development and tool caching
Exercise: build an async multi-crew research pipeline
Section 2: Production CrewAI
Memory types in CrewAI: short-term, long-term, entity, contextual
Training your crew with human feedback
CrewAI flows for structured event-driven pipelines
Crew evaluation and output quality scoring
Exercise: production-ready crew with memory, evals, and flows
Quiz: advanced CrewAI
Final Assessment

ADV-04 — Building Agentic RAG Systems with LangGraph
Section 1: Agentic RAG Concepts
Course overview
Limitations of naive RAG and why agents solve them
Corrective RAG (CRAG): self-grading and re-retrieval
Self-RAG: retrieve, critique, generate, regenerate
Section 2: Implementing Agentic RAG
Routing queries between retrieval and generation
Adaptive retrieval with query transformation
Multi-step retrieval graphs in LangGraph
Exercise: implement Corrective RAG with LangGraph
Section 3: Advanced Patterns
Agentic RAG with web search fallback
Multi-vector retrieval and hypothetical document embeddings (HyDE)
Evaluating agentic RAG: faithfulness, relevance, completeness
Exercise: build a full agentic RAG system with evals
Quiz: agentic RAG with LangGraph
Final Assessment

OPS-01 — Mastering LLMOps: From Build to Deployment
Section 1: LLMOps Foundations
Course overview: what separates a prototype from a product
The LLM application lifecycle: develop, evaluate, deploy, monitor
Prompt versioning and management
Environment separation and config management
Section 2: Evaluation Pipelines
Automated eval frameworks: DeepEval, RAGAs, PromptFoo
CI-integrated evals: running tests on every PR
Regression testing and A/B evaluation
Exercise: set up a full eval pipeline for an LLM application
Section 3: Deployment and Monitoring
Model serving: vLLM, Ollama, cloud-managed endpoints
Observability stack: LangSmith, Langfuse, Arize Phoenix
Cost dashboards, token budgets, and rate limit handling
Incident response for LLM production issues
Exercise: deploy, instrument, and set up alerts for an LLM app
Quiz: LLMOps
Final Assessment

PRJ-01 — Project: Multi-Agent AI System for Hotel Reservations
Section 1: Project Scoping
System overview: requirements and architecture walkthrough
Tool inventory: booking APIs, calendar, confirmation emails
Section 2: Building the System
Implementing the intent-routing agent
Building the reservation, availability, and modification sub-agents
Human-in-the-loop approval for bookings
Section 3: Hardening and Demo
Edge case handling and fallback flows
End-to-end testing
Project walkthrough and code review
Final Assessment

PRJ-02 — Project: Agentic RAG with AutoGen for eCommerce
Section 1: Project Scoping
System overview: product Q&A, recommendations, order queries
Data preparation: product catalogue ingestion and indexing
Section 2: Building the System
Building the retrieval layer with hybrid search
AutoGen agent crew: retriever, responder, escalation agent
Handling out-of-scope queries gracefully
Section 3: Evaluation and Demo
Evaluating answer quality against a golden dataset
Latency and cost profiling
Project walkthrough and deployment notes
Final Assessment
"""

# Parse raw text into structured JSON matching tracks_catalogue format
tracks = {
    "track1_aiml_foundations": {
        "label": "AI / ML Foundations",
        "description": "Core concepts in ML, deep learning, computer vision, NLP, and model training. Prerequisite knowledge for the Agentic AI track.",
        "courses": []
    },
    "track2_agentic_ai": {
        "label": "Agentic AI & Automation Tools",
        "description": "LLM application development, RAG systems, agent frameworks, and production deployment. Assumes Python fluency and basic ML literacy.",
        "courses": []
    }
}

current_track = None
current_course = None
current_section = None

COURSE_METADATA_MAP = {
    "F-01": {
        "description": "A broad, accessible introduction to generative AI — what it is, how it works at a high level, and where the field stands in 2026.",
        "prerequisites": "None",
        "audience": "Anyone curious about AI"
    },
    "F-02": {
        "description": "Ethics, safety, and governance for generative AI — built for practitioners who need to ship responsibly.",
        "prerequisites": "F-01 or basic AI familiarity",
        "audience": "Developers, product teams, AI practitioners"
    },
    "ML-01": {
        "description": "Python and tooling skills specifically needed to build AI agents and ML pipelines.",
        "prerequisites": "Basic programming literacy",
        "audience": "Beginners transitioning into AI engineering"
    },
    "ML-02": {
        "description": "End-to-end introduction to supervised machine learning with scikit-learn.",
        "prerequisites": "ML-01 or Python proficiency",
        "audience": "Developers new to machine learning"
    },
    "ML-03": {
        "description": "A practical tour of classical ML algorithms every AI engineer should know.",
        "prerequisites": "ML-02",
        "audience": "ML beginners building algorithmic literacy"
    },
    "DL-01": {
        "description": "Build and train neural networks from scratch using PyTorch, from perceptrons to CNNs.",
        "prerequisites": "ML-02, Python proficiency",
        "audience": "ML engineers moving into deep learning"
    },
    "DL-02": {
        "description": "From tokenisation to transformers — NLP fundamentals with hands-on PyTorch implementation.",
        "prerequisites": "DL-01",
        "audience": "Deep learning engineers moving into NLP"
    },
    "DL-03": {
        "description": "CNNs, object detection, segmentation, and vision-language models — end to end.",
        "prerequisites": "DL-01",
        "audience": "Engineers building vision-based AI systems"
    },
    "DM-01": {
        "description": "How cognitive science explains human decisions — and how those biases infect AI systems.",
        "prerequisites": "None",
        "audience": "AI practitioners, product leads, analysts"
    },
    "DM-02": {
        "description": "MECE thinking, issue trees, and decision frameworks for AI engineers and analysts.",
        "prerequisites": "None",
        "audience": "Anyone building or shipping AI products"
    },
    "FT-01": {
        "description": "LoRA, QLoRA, SFT, and evaluation — everything needed to adapt an LLM to a custom task.",
        "prerequisites": "DL-01, basic LLM familiarity",
        "audience": "ML engineers building domain-specific models"
    },
    "FT-02": {
        "description": "Pretraining data pipelines, GPT architecture, distributed training, and post-training alignment.",
        "prerequisites": "DL-01, DL-02, FT-01",
        "audience": "Senior ML engineers and researchers"
    },
    "FT-03": {
        "description": "RL fundamentals, deep RL, PPO, and the RLHF pipeline used to align modern LLMs.",
        "prerequisites": "DL-01, Python proficiency",
        "audience": "ML engineers working on model alignment and advanced training"
    },
    "SD-01": {
        "description": "Diffusion model intuition, text-to-image generation, and core prompting techniques.",
        "prerequisites": "Basic Python, F-01",
        "audience": "Developers and creators entering generative image AI"
    },
    "SD-02": {
        "description": "ControlNet, LoRA fine-tunes, ComfyUI workflows, and the 2026 model landscape.",
        "prerequisites": "SD-01",
        "audience": "Developers and creators building production image pipelines"
    },
    "GL-01": {
        "description": "Non-technical executive guide to evaluating, adopting, and governing generative AI.",
        "prerequisites": "None",
        "audience": "Business leaders, product owners, C-suite"
    },
    "GL-02": {
        "description": "Strategic frameworks for embedding AI into core operations and building durable competitive advantage.",
        "prerequisites": "GL-01 recommended",
        "audience": "CEOs, founders, and senior strategy leaders"
    },
    "LLM-01": {
        "description": "How LLMs work, the 2026 model landscape, and making your first production-quality API calls.",
        "prerequisites": "Python proficiency, ML-01",
        "audience": "Developers entering LLM application development"
    },
    "LLM-02": {
        "description": "LangChain 0.3 architecture, LCEL pipelines, retrieval chains, and your first LangChain agent.",
        "prerequisites": "LLM-01",
        "audience": "Developers building LLM-powered applications"
    },
    "LLM-03": {
        "description": "Zero-shot, few-shot, chain-of-thought, ReAct, and a systematic approach to building and evaluating prompts.",
        "prerequisites": "LLM-01",
        "audience": "Developers and product builders working with LLMs daily"
    },
    "RAG-01": {
        "description": "Core concepts, document processing, embedding strategies, vector databases, and evaluation of RAG systems.",
        "prerequisites": "LLM-01",
        "audience": "Developers building simple query/QA systems"
    },
    "RAG-02": {
        "description": "Advanced retrieval patterns, indexing strategies, routing, and enterprise RAG engineering with LlamaIndex.",
        "prerequisites": "RAG-01",
        "audience": "Data and software engineers building production QA applications"
    },
    "RAG-03": {
        "description": "FastAPI, Next.js, Streamlit, and dockerized cloud deployments for full-stack Generative AI applications.",
        "prerequisites": "RAG-01, RAG-02",
        "audience": "Full-stack developers and DevOps engineers"
    },
    "AG-01": {
        "description": "An intuitive, code-optional introduction to perception-reasoning-action loops, tools, and memory.",
        "prerequisites": "None",
        "audience": "Anyone interested in learning how AI agents automate workflows"
    },
    "AG-02": {
        "description": "Architectural design patterns, state management, human-in-the-loop loops, and security designs for AI agents.",
        "prerequisites": "AG-01, LLM-01",
        "audience": "Software architects and AI system designers"
    },
    "AG-03": {
        "description": "Build agentic ReAct loops, planning mechanisms, tool call builders, and evaluation harnesses from scratch.",
        "prerequisites": "AG-02, Python proficiency",
        "audience": "AI application engineers looking to understand core mechanics"
    },
    "AG-04": {
        "description": "Building tool-using support pipelines, stateful agents, and multi-agent coordination frameworks with LangChain.",
        "prerequisites": "AG-03, LLM-02",
        "audience": "Developers building production agent systems"
    },
    "GS-01": {
        "description": "Build stateful workflows, MessageGraphs, conditional edges, routing, and ReAct loops using LangGraph.",
        "prerequisites": "AG-04",
        "audience": "AI developers wanting robust control over agent state and pathways"
    },
    "GS-02": {
        "description": "Role-based agent design, inter-agent delegation, and automated crew management with CrewAI.",
        "prerequisites": "AG-01",
        "audience": "Developers and automated pipeline builders"
    },
    "ADV-01": {
        "description": "Subgraphs, nested composition, supervisor nodes, time-travel debugging, and swarm topologies with LangGraph.",
        "prerequisites": "GS-01",
        "audience": "Senior AI engineers building complex multi-agent architectures"
    },
    "ADV-02": {
        "description": "Conversable assistant agents, round-robin/selector groups, and distributed systems with AutoGen.",
        "prerequisites": "AG-03",
        "audience": "Research and software engineers creating collaborative agent systems"
    },
    "ADV-03": {
        "description": "Hierarchical managers, asynchronous tasks, tool caching, memory systems, and Flows with CrewAI.",
        "prerequisites": "GS-02",
        "audience": "Senior developers building robust business task automation"
    },
    "ADV-04": {
        "description": "Corrective RAG, self-RAG, adaptive query routing, and self-correcting search tools with LangGraph.",
        "prerequisites": "ADV-01, RAG-02",
        "audience": "AI search engineers building state-of-the-art retrieval QA"
    },
    "OPS-01": {
        "description": "Automated evaluation pipelines, CI evals, model serving optimizations, and production observability stack.",
        "prerequisites": "LLM-01",
        "audience": "AI engineers and DevOps specialists"
    },
    "PRJ-01": {
        "description": "Build an intent router and a multi-agent sub-crew with human approval gates to handle hotel bookings.",
        "prerequisites": "GS-01 or GS-02",
        "audience": "AI builders completing their practical capstone"
    },
    "PRJ-02": {
        "description": "Build a multi-agent e-commerce catalog search and query routing assistant with AutoGen.",
        "prerequisites": "ADV-02, RAG-01",
        "audience": "AI search capstone developers"
    }
}

lesson_counter = {}

for line in RAW_TEXT.strip().split("\n"):
    line = line.strip()
    if not line:
        continue
        
    if line.startswith("Track 1:"):
        current_track = "track1_aiml_foundations"
        continue
    elif line.startswith("Track 2:"):
        current_track = "track2_agentic_ai"
        continue
        
    # Check if it is a course title (ID — Name)
    match = re.match(r"^([A-Z0-9\-]+)\s+—\s+(.+)$", line)
    if match:
        c_id = match.group(1).strip()
        c_title = match.group(2).strip()
        meta = COURSE_METADATA_MAP.get(c_id, {
            "description": f"Comprehensive learning course for {c_title}.",
            "prerequisites": "Basic understanding of Python and AI foundations",
            "audience": "Developers and AI practitioners"
        })
        current_course = {
            "id": c_id,
            "title": c_title,
            "description": meta["description"],
            "prerequisites": meta["prerequisites"],
            "audience": meta["audience"],
            "sections": []
        }
        tracks[current_track]["courses"].append(current_course)
        current_section = None
        lesson_counter[c_id] = 1
        continue
        
    # Check if section
    if line.startswith("Section "):
        sec_title = line.split(":", 1)[1].strip() if ":" in line else line
        current_section = {
            "title": sec_title,
            "lessons": []
        }
        current_course["sections"].append(current_section)
        continue
        
    # Check if Final Assessment
    if line == "Final Assessment":
        fa_sec = {
            "title": "Final Assessment",
            "lessons": [
                {
                    "id": f"{current_course['id'].replace('-', '')}-FA",
                    "title": "Final Assessment",
                    "type": "final_assessment"
                }
            ]
        }
        current_course["sections"].append(fa_sec)
        continue
        
    # Otherwise it must be a lesson
    if current_course and current_section:
        c_id_clean = current_course["id"].replace("-", "")
        lesson_num = lesson_counter[current_course["id"]]
        lesson_counter[current_course["id"]] += 1
        
        # Deduce lesson type from title keywords
        title_lower = line.lower()
        l_type = "concept"
        if "welcome" in title_lower or "overview" in title_lower:
            l_type = "intro"
        elif "exercise" in title_lower or "project" in title_lower or "build" in title_lower:
            l_type = "exercise"
        elif "quiz" in title_lower:
            l_type = "quiz"
            
        lesson_id = f"{c_id_clean}-L{lesson_num:02d}"
        current_section["lessons"].append({
            "id": lesson_id,
            "title": line,
            "type": l_type
        })

# Write the output to a JSON file
with open("courses_catalogue.json", "w") as f:
    json.dump(tracks, f, indent=2)

print(f"Catalog parsed successfully. Total tracks: {len(tracks)}")
for t_id, track in tracks.items():
    print(f"  Track: {track['label']}, Courses: {len(track['courses'])}")
