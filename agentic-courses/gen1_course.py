import json, os

OUT = os.path.join(os.path.dirname(__file__), "course1_coding_essentials")
if not os.path.exists(OUT):
    os.makedirs(OUT)

def nb(cells):
    return {
        "nbformat": 4, "nbformat_minor": 0,
        "metadata": {
            "colab": {"provenance": [], "toc_visible": True},
            "kernelspec": {"name": "python3", "display_name": "Python 3"},
            "language_info": {"name": "python"}
        },
        "cells": cells
    }

def md(src):   return {"cell_type": "markdown", "metadata": {}, "source": src}
def code(src): return {"cell_type": "code", "metadata": {}, "source": src, "execution_count": None, "outputs": []}

def save(filename, cells):
    with open(os.path.join(OUT, filename), "w") as f:
        json.dump(nb(cells), f, indent=2)
    print(f"  Created: {filename}")

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1.1 — Python Fundamentals Refresher
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_1_1_Python_Fundamentals_Refresher.ipynb", [
md("""# Lesson 1.1 — Python Fundamentals Refresher
### Coding Essentials for Agents | AgenticLabs.ng

---

## Learning Objectives
- Confidently use variables, data types, and operators
- Write clean, readable loops and conditionals
- Define reusable functions with parameters and return values
- Apply Python coding conventions used in real ML pipelines
- Understand why code style matters in collaborative AI projects

---

## Why This Matters for AI Development

Every ML pipeline — from data loading to model deployment — is Python code. The quality of that code determines whether your pipeline is maintainable, debuggable, and reproducible. This lesson builds the habits professionals rely on daily.

---

## 1. Variables and Data Types
"""),
code("""# ── Variables and core data types ────────────────────────────────────────────

# Python infers the type — you don't need to declare it
name        = "AgenticLabs"     # str
year        = 2024              # int
accuracy    = 0.947             # float
is_trained  = True              # bool
no_value    = None              # NoneType

# Check the type of any variable
print(type(name))
print(type(accuracy))
print(type(is_trained))

# Type conversion — common in data pipelines
age_str  = "25"
age_int  = int(age_str)
age_flt  = float(age_str)
print(f"String '{age_str}' → int {age_int} → float {age_flt}")

# f-strings are the standard for readable output in ML code
model_name = "ResNet-50"
val_acc    = 0.9231
print(f"Model: {model_name} | Validation accuracy: {val_acc:.2%}")
"""),

md("## 2. Operators and Expressions\n\nML pipelines use arithmetic, comparison, and logical operators constantly — in loss calculations, data filtering, and condition checks."),
code("""# ── Arithmetic operators ──────────────────────────────────────────────────────
n_samples   = 10000
train_ratio = 0.8

n_train = int(n_samples * train_ratio)
n_test  = n_samples - n_train
n_val   = n_test // 2           # integer division

print(f"Train: {n_train} | Val: {n_val} | Test: {n_test - n_val}")

# ── Comparison and logical operators ──────────────────────────────────────────
loss       = 0.043
threshold  = 0.05
patience   = 3
counter    = 2

# These are the kinds of conditions you write inside training loops
should_stop  = (loss < threshold) and (counter >= patience)
is_improving = (loss < threshold) or (counter == 0)

print(f"Should stop early: {should_stop}")
print(f"Is improving     : {is_improving}")

# ── Augmented assignment (shorthand used everywhere in loops) ─────────────────
total_loss = 0.0
batch_losses = [0.32, 0.28, 0.21, 0.18, 0.15]

for batch_loss in batch_losses:
    total_loss += batch_loss       # equivalent to: total_loss = total_loss + batch_loss

avg_loss = total_loss / len(batch_losses)
print(f"Average loss: {avg_loss:.4f}")
"""),

md("## 3. Conditionals\n\nConditionals control the flow of ML pipelines — choosing which preprocessing to apply, when to stop training, or how to handle edge cases."),
code("""# ── if / elif / else ─────────────────────────────────────────────────────────

def classify_model_performance(accuracy):
    \"\"\"Categorise model performance based on accuracy threshold.\"\"\"
    if accuracy >= 0.95:
        category = "Production-ready"
        action   = "Deploy to production."
    elif accuracy >= 0.85:
        category = "Good"
        action   = "Fine-tune further before deploying."
    elif accuracy >= 0.70:
        category = "Acceptable"
        action   = "Collect more data or try a better architecture."
    else:
        category = "Poor"
        action   = "Re-examine data quality and model design."
    return category, action

# Test across a range of scores
test_scores = [0.97, 0.88, 0.73, 0.51]
print(f"{'Accuracy':>10} | {'Category':<20} | Action")
print("-" * 65)
for score in test_scores:
    cat, act = classify_model_performance(score)
    print(f"{score:>10.0%} | {cat:<20} | {act}")
"""),

code("""# ── Ternary expression (one-line conditional) ─────────────────────────────────
# Common in data preprocessing and quick label assignment

labels = [0, 1, 1, 0, 1, 0, 0, 1]
sentiment = ["negative" if l == 0 else "positive" for l in labels]
print("Labels    :", labels)
print("Sentiment :", sentiment)

# ── Truthy and falsy values ────────────────────────────────────────────────────
# In Python, None, 0, empty string "", and empty list [] are all falsy
def load_model(path=None):
    if not path:
        print("No path provided — using default model.")
        return "default_model"
    print(f"Loading model from: {path}")
    return f"model_from_{path}"

load_model()
load_model("models/resnet50.pth")
"""),

md("## 4. Loops\n\nLoops are the foundation of ML training, data processing, and batch operations."),
code("""# ── for loops ─────────────────────────────────────────────────────────────────

# Iterating over a list
frameworks = ["PyTorch", "TensorFlow", "JAX", "scikit-learn"]
for fw in frameworks:
    print(f"  - {fw}")

# enumerate() gives you both index and value — use this instead of range(len(...))
print()
for i, fw in enumerate(frameworks, start=1):
    print(f"  {i}. {fw}")

# zip() pairs two sequences — critical for pairing predictions with labels
predictions = [0.92, 0.87, 0.43, 0.99, 0.61]
actuals     = [1,    1,    0,    1,    1   ]

correct = 0
for pred, actual in zip(predictions, actuals):
    predicted_class = 1 if pred >= 0.5 else 0
    if predicted_class == actual:
        correct += 1

print(f"\\nAccuracy: {correct / len(actuals):.0%}")
"""),

code("""# ── while loops ───────────────────────────────────────────────────────────────
# Used in training loops where you continue until a condition is met

import random
random.seed(42)

epoch      = 0
loss       = 1.0
best_loss  = float('inf')
no_improve = 0
history    = []

print("Simulating a training loop with early stopping:")
print(f"{'Epoch':>6} | {'Loss':>8} | {'Status'}")
print("-" * 35)

while epoch < 50 and no_improve < 5:
    loss = loss * random.uniform(0.85, 1.05)   # simulate loss changing
    epoch += 1
    history.append(loss)

    if loss < best_loss - 0.001:
        best_loss  = loss
        no_improve = 0
        status = "improved"
    else:
        no_improve += 1
        status = f"no improvement ({no_improve}/5)"

    if epoch % 5 == 0 or no_improve >= 5:
        print(f"{epoch:>6} | {loss:>8.4f} | {status}")

print(f"\\nStopped at epoch {epoch}. Best loss: {best_loss:.4f}")
"""),

md("## 5. Functions\n\nWell-written functions are the difference between code that can be maintained and code that becomes a liability. Every operation in your ML pipeline should live in a named function."),
code("""# ── Defining and calling functions ────────────────────────────────────────────

def normalise(values, min_val=None, max_val=None):
    \"\"\"
    Apply min-max normalisation to a list of values.

    Args:
        values  : list of numeric values
        min_val : optional minimum (uses data min if not provided)
        max_val : optional maximum (uses data max if not provided)

    Returns:
        list of normalised values in range [0, 1]
    \"\"\"
    if min_val is None:
        min_val = min(values)
    if max_val is None:
        max_val = max(values)

    if max_val == min_val:
        return [0.0] * len(values)          # avoid division by zero

    return [(v - min_val) / (max_val - min_val) for v in values]


# Test it
raw_ages = [22, 45, 31, 67, 18, 55]
norm_ages = normalise(raw_ages)

print("Original :", raw_ages)
print("Normalised:", [f"{v:.3f}" for v in norm_ages])
print("Min → 0, Max → 1:", norm_ages[0], "→", norm_ages[3])

# Fix the range explicitly (e.g. you know age range is 0-100)
norm_fixed = normalise(raw_ages, min_val=0, max_val=100)
print("Fixed range:", [f"{v:.3f}" for v in norm_fixed])
"""),

code("""# ── *args and **kwargs — flexible function signatures ─────────────────────────
# You will see these frequently in PyTorch, scikit-learn, and API wrappers

def log_experiment(*metrics, **hyperparams):
    \"\"\"
    Log experiment results with arbitrary metrics and hyperparameters.
    This pattern is used by tools like MLflow and Weights & Biases.
    \"\"\"
    print("Experiment Log")
    print("  Metrics:")
    for value in metrics:
        print(f"    - {value}")
    print("  Hyperparameters:")
    for key, val in hyperparams.items():
        print(f"    {key}: {val}")

log_experiment(
    "accuracy=0.924", "f1=0.918", "auc=0.971",
    learning_rate=0.001,
    batch_size=64,
    epochs=20,
    optimizer="Adam"
)
"""),

code("""# ── Lambda functions ──────────────────────────────────────────────────────────
# Short anonymous functions — used in data transformation pipelines

# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
sq = lambda x: x ** 2
print(square(5), sq(5))       # both give 25

# Practical use: sorting complex objects
models = [
    {"name": "LogisticRegression", "accuracy": 0.87, "train_time": 1.2},
    {"name": "RandomForest",       "accuracy": 0.93, "train_time": 8.4},
    {"name": "SVM",                "accuracy": 0.91, "train_time": 3.1},
]

# Sort by accuracy descending
ranked = sorted(models, key=lambda m: m["accuracy"], reverse=True)
print("\\nModels ranked by accuracy:")
for i, m in enumerate(ranked, 1):
    print(f"  {i}. {m['name']:25s} | acc={m['accuracy']:.2f} | time={m['train_time']:.1f}s")
"""),

md("## 6. Writing Clean, ML-Grade Python\n\nProfessional ML code follows conventions that make it readable and maintainable."),
code("""# ── Style and readability conventions ────────────────────────────────────────

# BAD: hard to read, no context
def p(x, t=0.5):
    return [1 if i > t else 0 for i in x]

# GOOD: clear names, docstring, type hints
def threshold_predictions(probabilities: list, threshold: float = 0.5) -> list:
    \"\"\"
    Convert prediction probabilities to binary class labels.

    Args:
        probabilities : list of floats between 0 and 1
        threshold     : decision cutoff (default 0.5)

    Returns:
        list of integer class labels (0 or 1)
    \"\"\"
    return [1 if prob > threshold else 0 for prob in probabilities]


# BAD: magic numbers, unclear flow
def calc(n):
    return n * 0.8, n * 0.1, n * 0.1

# GOOD: named constants, descriptive names
TRAIN_RATIO = 0.80
VAL_RATIO   = 0.10
TEST_RATIO  = 0.10

def compute_split_sizes(total_samples: int) -> tuple:
    \"\"\"Return (train, val, test) split sizes for a dataset.\"\"\"
    train = int(total_samples * TRAIN_RATIO)
    val   = int(total_samples * VAL_RATIO)
    test  = total_samples - train - val
    return train, val, test

train, val, test = compute_split_sizes(10000)
print(f"Split: {train} train | {val} val | {test} test")

# ── List comprehensions (Pythonic, preferred over explicit loops) ─────────────
temperatures_c = [0, 20, 37, 100]
temperatures_f = [(c * 9/5) + 32 for c in temperatures_c]
print("\\nCelsius    :", temperatures_c)
print("Fahrenheit :", temperatures_f)
"""),

md("""## Exercises

1. **Function writing**: Write a function `evaluate_predictions(y_true, y_pred)` that takes two lists and returns a dictionary with keys `accuracy`, `correct_count`, and `total_count`.

2. **Loop practice**: Write a `while` loop that simulates a learning rate warm-up schedule — start at `lr=0.0001` and multiply by 1.5 each step until it reaches `0.01`. Print the lr value at each step.

3. **Clean code refactor**: The following function works but is poorly written. Rewrite it with proper naming, a docstring, and type hints:
   ```python
   def f(d, k, v=0):
       if k in d:
           return d[k]
       return v
   ```

4. **Comprehension challenge**: Using a single list comprehension, generate a list of all even numbers between 1 and 100 that are divisible by 6.

---

## Summary

| Concept | When you use it in ML |
|---|---|
| Variables and types | Storing hyperparameters, labels, model outputs |
| Conditionals | Early stopping, decision logic, error handling |
| for loops | Iterating over batches, features, epochs |
| while loops | Training loops with convergence conditions |
| Functions | Encapsulating preprocessing, evaluation, training steps |
| Clean style | Making your pipeline readable to teammates and your future self |

**Next — Lesson 1.2: Working with Data Structures**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1.2 — Working with Data Structures
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_1_2_Working_with_Data_Structures.ipynb", [
md("""# Lesson 1.2 — Working with Data Structures
### Coding Essentials for Agents | AgenticLabs.ng

---

## Learning Objectives
- Use lists, tuples, sets, and dictionaries confidently
- Manipulate and transform data using built-in Python methods
- Work with pandas DataFrames as the primary structure for tabular ML data
- Apply indexing, filtering, and aggregation operations on real data
- Understand which data structure to reach for in different ML scenarios

---

## Why Data Structures Matter in ML

Every dataset you work with is stored in a data structure before it reaches a model. Knowing how to efficiently access, filter, and transform data in Python is a non-negotiable skill — it determines the speed and correctness of your preprocessing pipeline.

---

## 1. Lists — Ordered, Mutable Sequences
"""),
code("""# ── Lists: the workhorse of Python data handling ─────────────────────────────

# Creating lists
feature_names  = ["age", "income", "credit_score", "loan_amount", "employment_years"]
class_labels   = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
loss_history   = []   # empty — will be populated during training

# Accessing elements
print(f"First feature  : {feature_names[0]}")
print(f"Last feature   : {feature_names[-1]}")
print(f"Features 1-3   : {feature_names[1:4]}")    # slicing [start:stop]
print(f"Every 2nd      : {feature_names[::2]}")    # [::step]
print(f"Reversed       : {feature_names[::-1]}")

print(f"\\nTotal features : {len(feature_names)}")
print(f"Class balance  : {class_labels.count(1)} positives, {class_labels.count(0)} negatives")
"""),

code("""# ── List methods used daily in ML ─────────────────────────────────────────────

# append, extend — building up results during training
epochs_run    = []
val_accuracies = []

for epoch in range(1, 6):
    simulated_acc = 0.6 + (epoch * 0.07)
    epochs_run.append(epoch)
    val_accuracies.append(round(simulated_acc, 3))

print("Epochs   :", epochs_run)
print("Val accs :", val_accuracies)
print("Best acc :", max(val_accuracies))
print("Best epoch:", val_accuracies.index(max(val_accuracies)) + 1)

# sort, sorted — ranking models
model_scores = [0.87, 0.93, 0.91, 0.78, 0.95]
print(f"\\nOriginal    : {model_scores}")
print(f"Sorted asc  : {sorted(model_scores)}")
print(f"Sorted desc : {sorted(model_scores, reverse=True)}")

# List comprehensions with conditions — filtering data
high_performing = [score for score in model_scores if score >= 0.90]
print(f"\\nScores ≥ 0.90: {high_performing}")

# Flattening a nested list — common after batch processing
batch_predictions = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]
flat_predictions  = [pred for batch in batch_predictions for pred in batch]
print(f"\\nFlattened predictions: {flat_predictions}")
"""),

md("## 2. Dictionaries — Key-Value Stores\n\nDictionaries are everywhere in ML: storing hyperparameters, model configs, label mappings, and API responses."),
code("""# ── Dictionaries: structured storage for ML configs ──────────────────────────

# Model configuration — a real-world use case
model_config = {
    "architecture"  : "ResNet-50",
    "num_classes"   : 10,
    "learning_rate" : 0.001,
    "batch_size"    : 64,
    "optimizer"     : "Adam",
    "dropout_rate"  : 0.3,
    "pretrained"    : True,
}

# Accessing values
print(f"Architecture : {model_config['architecture']}")
print(f"Learning rate: {model_config['learning_rate']}")

# .get() is safer than [] — returns None (or a default) if key doesn't exist
weight_decay = model_config.get("weight_decay", 1e-4)
print(f"Weight decay : {weight_decay}  (default used — key not in config)")

# Updating and adding entries
model_config["epochs"]       = 30
model_config["learning_rate"] = 0.0005   # update existing key
print(f"\\nUpdated config: {model_config}")
"""),

code("""# ── Dictionary operations for ML workflows ────────────────────────────────────

# Label encoding — mapping class names to integers
label_map = {
    "cat"        : 0,
    "dog"        : 1,
    "bird"       : 2,
    "fish"       : 3,
    "rabbit"     : 4,
}

# Reverse mapping — going from int back to class name
reverse_map = {v: k for k, v in label_map.items()}

text_labels = ["dog", "cat", "bird", "cat", "rabbit"]
encoded     = [label_map[l] for l in text_labels]
decoded     = [reverse_map[e] for e in encoded]

print("Original  :", text_labels)
print("Encoded   :", encoded)
print("Decoded   :", decoded)

# Iterating over a config — common for logging
print("\\nModel hyperparameters:")
config = {"lr": 0.001, "batch_size": 64, "epochs": 20, "dropout": 0.3}
for param, value in config.items():
    print(f"  {param:<15}: {value}")

# Nested dictionaries — experiment tracking
experiments = {
    "exp_001": {"model": "LR",  "accuracy": 0.84, "f1": 0.82},
    "exp_002": {"model": "RF",  "accuracy": 0.91, "f1": 0.90},
    "exp_003": {"model": "SVM", "accuracy": 0.89, "f1": 0.88},
}
best_exp = max(experiments, key=lambda k: experiments[k]["accuracy"])
print(f"\\nBest experiment: {best_exp} → {experiments[best_exp]}")
"""),

md("## 3. Tuples and Sets"),
code("""# ── Tuples — immutable sequences ──────────────────────────────────────────────
# Use tuples when data should not change: image dimensions, model output shapes

image_shape    = (224, 224, 3)          # height, width, channels
output_shape   = (batch_size := 32, 10) # batch, classes

print(f"Image shape : {image_shape}")
print(f"Channels    : {image_shape[2]}")

# Tuple unpacking — very common in Python ML code
height, width, channels = image_shape
print(f"H={height}, W={width}, C={channels}")

# Functions that return multiple values return tuples
def train_test_split_sizes(total, train_ratio=0.8):
    train = int(total * train_ratio)
    test  = total - train
    return train, test       # returns a tuple

n_train, n_test = train_test_split_sizes(5000)
print(f"\\nTrain: {n_train} | Test: {n_test}")

# ── Sets — unordered, unique elements ─────────────────────────────────────────
# Used for deduplication, vocabulary building, and membership checks

all_tokens  = ["the", "cat", "sat", "on", "the", "mat", "the", "cat"]
unique_vocab = set(all_tokens)
print(f"\\nAll tokens   : {all_tokens}")
print(f"Unique vocab : {unique_vocab}")
print(f"Vocab size   : {len(unique_vocab)}")

# Set operations — useful for data validation
required_columns = {"age", "income", "label"}
available_columns = {"age", "income", "name", "label", "city"}

missing  = required_columns - available_columns
extra    = available_columns - required_columns
overlap  = required_columns & available_columns

print(f"\\nMissing columns : {missing}")
print(f"Extra columns   : {extra}")
print(f"Present and needed: {overlap}")
"""),

md("## 4. Pandas DataFrames — The Core ML Data Structure\n\nIn practice, almost all tabular data in ML pipelines lives in a pandas DataFrame. Mastering it is essential."),
code("""import pandas as pd
import numpy as np

# ── Creating a DataFrame ──────────────────────────────────────────────────────
np.random.seed(42)

data = {
    "customer_id"     : range(1, 11),
    "age"             : [23, 45, 31, 56, 28, 41, 37, 52, 26, 44],
    "income"          : [32000, 85000, 54000, 120000, 41000, 76000, 62000, 95000, 38000, 88000],
    "credit_score"    : [620, 780, 690, 820, 640, 750, 710, 800, 600, 760],
    "loan_requested"  : [5000, 20000, 12000, 35000, 8000, 18000, 15000, 25000, 6000, 22000],
    "approved"        : [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
}

df = pd.DataFrame(data)
print("DataFrame shape:", df.shape)
print("\\nFirst 5 rows:")
print(df.head())
"""),

code("""# ── Inspection methods — first thing you do with any dataset ─────────────────
print("Data types:")
print(df.dtypes)
print("\\nBasic statistics:")
print(df.describe().round(1))
print("\\nMissing values:")
print(df.isnull().sum())
"""),

code("""# ── Selecting data ────────────────────────────────────────────────────────────

# Select a single column (returns a Series)
ages = df["age"]
print("Ages:", ages.tolist())

# Select multiple columns (returns a DataFrame)
features_only = df[["age", "income", "credit_score", "loan_requested"]]
print("\\nFeature columns:")
print(features_only.head(3))

# Select by row index with .iloc (integer location)
print("\\nFirst row (iloc):")
print(df.iloc[0])

# Select by label with .loc
print("\\nRow where customer_id == 3:")
print(df.loc[df["customer_id"] == 3])
"""),

code("""# ── Filtering — the most used operation in data prep ─────────────────────────

# Single condition
high_income = df[df["income"] > 70000]
print(f"High income customers (>70k): {len(high_income)}")

# Multiple conditions (use & and |, not 'and'/'or')
qualified = df[(df["credit_score"] >= 700) & (df["income"] >= 50000)]
print(f"\\nQualified (credit≥700 AND income≥50k): {len(qualified)}")
print(qualified[["customer_id", "income", "credit_score", "approved"]])

# Filtering out nulls
df_sample = df.copy()
df_sample.loc[2, "income"] = None     # introduce a missing value
df_clean = df_sample.dropna(subset=["income"])
print(f"\\nBefore dropna: {len(df_sample)} | After dropna: {len(df_clean)}")
"""),

code("""# ── Adding columns and transformations ────────────────────────────────────────

df_work = df.copy()

# Derived features — engineer new columns from existing ones
df_work["debt_to_income"]  = (df_work["loan_requested"] / df_work["income"]).round(3)
df_work["income_per_year"] = (df_work["income"] / 12).round(0).astype(int)

# Binning (discretisation) — turning continuous into categorical
df_work["age_group"] = pd.cut(
    df_work["age"],
    bins=[0, 30, 45, 100],
    labels=["young", "mid-career", "senior"]
)

print("Engineered features:")
print(df_work[["customer_id", "age", "age_group", "debt_to_income"]].head(8))

# GroupBy aggregation — understanding your data by category
print("\\nApproval stats by age group:")
print(df_work.groupby("age_group")["approved"].agg(["count", "sum", "mean"]).round(2))
"""),

md("""## Exercises

1. **List manipulation**: Given `scores = [78, 92, 65, 88, 72, 95, 61, 84]`, write a one-liner to create a new list containing only scores above 80, sorted in descending order.

2. **Dictionary challenge**: Write a function `merge_configs(base_config, override_config)` that returns a new dictionary combining both configs, with `override_config` values taking precedence where keys overlap.

3. **DataFrame operations**: Using the loan dataset from this lesson, calculate the approval rate (mean of `approved`) for customers with a `debt_to_income` ratio above 0.3 versus below.

4. **Vocabulary builder**: Write a function that takes a list of sentences (strings) and returns a sorted list of unique words (lowercase, punctuation removed).

---

## Summary

| Structure | Best for |
|---|---|
| List | Ordered sequences — training history, batch results, feature lists |
| Dictionary | Key-value mappings — configs, label maps, API responses |
| Tuple | Immutable groupings — shapes, coordinates, function return values |
| Set | Unique collections — vocabulary, column validation |
| DataFrame | Tabular data — any structured dataset before modelling |

**Next — Lesson 1.3: Libraries and Environment Setup**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1.3 — Libraries and Environment Setup
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_1_3_Libraries_and_Environment_Setup.ipynb", [
md("""# Lesson 1.3 — Libraries and Environment Setup
### Coding Essentials for Agents | AgenticLabs.ng

---

## Learning Objectives
- Understand how Python environments and package managers work
- Install and import NumPy, pandas, and scikit-learn correctly
- Perform core numerical computing operations with NumPy
- Know the purpose and relationship between the main ML libraries
- Navigate Jupyter notebooks and VS Code effectively

---

## The Python ML Library Ecosystem

```
NumPy          → numerical computing, arrays, linear algebra
pandas         → tabular data, DataFrames, data wrangling
matplotlib     → plotting and visualisation
scikit-learn   → classical ML algorithms, preprocessing, evaluation
PyTorch        → deep learning (covered in the DL Foundations course)
transformers   → pretrained LLMs (covered in the Agentic AI course)
```

Each library is built on top of the one before it. NumPy is the foundation everything else depends on.
"""),
code("""# ── In Google Colab, most libraries are pre-installed ─────────────────────────
# Run this cell first to ensure you have everything needed for this lesson

!pip install numpy pandas scikit-learn matplotlib seaborn --quiet
print("All libraries installed")
"""),

code("""# ── Imports — standard conventions used by the entire community ───────────────
# These aliases (np, pd, plt) are universal — always use them

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sklearn

print(f"NumPy      : {np.__version__}")
print(f"pandas     : {pd.__version__}")
print(f"matplotlib : {matplotlib.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
"""),

md("## 2. NumPy — Numerical Computing\n\nNumPy's N-dimensional array (`ndarray`) is the data type that PyTorch tensors, pandas DataFrames, and scikit-learn models all use internally. Understanding NumPy means understanding the foundation of all ML computing."),
code("""# ── Creating NumPy arrays ─────────────────────────────────────────────────────

# From a Python list
heights = np.array([170, 165, 182, 158, 175, 190, 168])
print("Heights array :", heights)
print("Shape         :", heights.shape)
print("Data type     :", heights.dtype)

# 2D array — a small dataset matrix
# Each row = one sample, each column = one feature
X = np.array([
    [25, 50000, 680],   # age, income, credit_score
    [42, 92000, 780],
    [31, 61000, 720],
    [55, 130000, 810],
    [28, 43000, 640],
])
print("\nFeature matrix shape:", X.shape, "  (5 samples, 3 features)")
print("Row 0 (first sample):", X[0])
print("Column 1 (income)   :", X[:, 1])    # all rows, column index 1
"""),

code("""# ── Array creation shortcuts — used constantly ────────────────────────────────

zeros     = np.zeros(5)                   # initialise with zeros
ones      = np.ones((3, 3))              # 3x3 matrix of ones
identity  = np.eye(4)                    # 4x4 identity matrix
linspace  = np.linspace(0, 1, 11)        # 11 evenly spaced points from 0 to 1
arange    = np.arange(0, 100, 10)        # like range() but returns an array
random_m  = np.random.randn(3, 3)        # standard normal distribution

print("zeros    :", zeros)
print("ones:\n",   ones)
print("linspace :", linspace)
print("arange   :", arange)
"""),

code("""# ── Vectorised operations — the power of NumPy ────────────────────────────────
# These run in optimised C code — vastly faster than Python loops

prices = np.array([200.0, 450.0, 125.0, 780.0, 340.0])

# Apply operations to every element simultaneously (no loop needed)
print("Original prices  :", prices)
print("10% discount     :", prices * 0.90)
print("Log transform    :", np.log(prices).round(3))
print("Standardised     :", ((prices - prices.mean()) / prices.std()).round(3))

# Comparison operations — produce boolean arrays
print("\nPrices > 300     :", prices > 300)
print("Filtered         :", prices[prices > 300])   # boolean indexing

# Universal functions (ufuncs) — applied element-wise
angles = np.array([0, 30, 45, 60, 90])
radians = np.radians(angles)
print("\nSine values      :", np.sin(radians).round(3))
"""),

code("""# ── Statistical operations ────────────────────────────────────────────────────
np.random.seed(42)
data = np.random.randint(0, 100, size=(6, 4))   # 6 samples, 4 features

print("Data matrix:\n", data)
print("\nPer-feature statistics:")
print(f"  Mean  : {data.mean(axis=0)}")      # axis=0 means across rows
print(f"  Std   : {data.std(axis=0).round(1)}")
print(f"  Min   : {data.min(axis=0)}")
print(f"  Max   : {data.max(axis=0)}")

# Matrix operations — linear algebra at the core of ML
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix multiply (A @ B):\n", A @ B)
print("Transpose of A:\n", A.T)
print("Determinant of A:", np.linalg.det(A).round(2))
"""),

md("## 3. Visualisation with Matplotlib\n\nEvery ML practitioner needs to visualise data and model results. Matplotlib is the foundation; knowing it well means you can produce any chart you need."),
code("""# ── Essential plots for ML work ───────────────────────────────────────────────
np.random.seed(42)

fig, axes = plt.subplots(2, 3, figsize=(14, 8))

# 1. Line plot — training curves
epochs = range(1, 21)
train_loss = [1.0 * 0.85**e + np.random.randn()*0.02 for e in epochs]
val_loss   = [1.0 * 0.88**e + np.random.randn()*0.03 for e in epochs]
axes[0, 0].plot(epochs, train_loss, 'b-o', ms=4, label='Train')
axes[0, 0].plot(epochs, val_loss,   'r-o', ms=4, label='Val')
axes[0, 0].set_title("Training Curves"); axes[0, 0].set_xlabel("Epoch")
axes[0, 0].set_ylabel("Loss"); axes[0, 0].legend(); axes[0, 0].grid(alpha=0.3)

# 2. Scatter plot — feature relationships
x = np.random.randn(100); y = 2*x + np.random.randn(100)*0.5
axes[0, 1].scatter(x, y, alpha=0.6, c='#4C72B0', edgecolors='white', s=50)
axes[0, 1].set_title("Feature Correlation"); axes[0, 1].set_xlabel("Feature A")
axes[0, 1].set_ylabel("Feature B"); axes[0, 1].grid(alpha=0.3)

# 3. Histogram — data distribution
income = np.random.lognormal(mean=11, sigma=0.5, size=500)
axes[0, 2].hist(income, bins=30, color='#55A868', edgecolor='white', alpha=0.8)
axes[0, 2].set_title("Income Distribution"); axes[0, 2].set_xlabel("Income")
axes[0, 2].set_ylabel("Count"); axes[0, 2].grid(alpha=0.3, axis='y')

# 4. Bar chart — class distribution
class_names = ['Cat', 'Dog', 'Bird', 'Fish', 'Rabbit']
counts      = [320, 285, 145, 90, 160]
colors      = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2']
axes[1, 0].bar(class_names, counts, color=colors, edgecolor='white')
axes[1, 0].set_title("Class Distribution"); axes[1, 0].set_ylabel("Count")
axes[1, 0].grid(alpha=0.3, axis='y')

# 5. Box plot — outlier detection
data_multi = [np.random.randn(100) * s + m
              for s, m in [(1, 0), (1.5, 2), (0.8, -1), (2, 1)]]
axes[1, 1].boxplot(data_multi, labels=['Feat 1', 'Feat 2', 'Feat 3', 'Feat 4'])
axes[1, 1].set_title("Feature Distributions (Boxplot)")
axes[1, 1].set_ylabel("Value"); axes[1, 1].grid(alpha=0.3, axis='y')

# 6. Heatmap — correlation matrix
corr_data = pd.DataFrame(np.random.randn(50, 4),
                          columns=['Age', 'Income', 'Score', 'Loan'])
corr = corr_data.corr()
import seaborn as sns
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            ax=axes[1, 2], linewidths=0.5)
axes[1, 2].set_title("Correlation Heatmap")

plt.suptitle("Essential ML Visualisations", fontsize=14, y=1.01)
plt.tight_layout()
plt.show()
"""),

md("## 4. scikit-learn — The ML Toolkit\n\nScikit-learn provides a consistent interface for preprocessing, model training, and evaluation. Understanding its API structure makes every other ML library easier to learn."),
code("""from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

np.random.seed(42)

# ── The scikit-learn API: fit → transform → predict ───────────────────────────

# 1. Create synthetic data
n = 200
X = np.random.randn(n, 3)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Preprocess — ALWAYS fit on train, transform both
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)    # fit + transform
X_test_scaled  = scaler.transform(X_test)         # transform only — never fit on test!

# 4. Train
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 5. Evaluate
train_acc = accuracy_score(y_train, model.predict(X_train_scaled))
test_acc  = accuracy_score(y_test,  model.predict(X_test_scaled))

print("scikit-learn Pipeline:")
print(f"  Training accuracy : {train_acc:.2%}")
print(f"  Test accuracy     : {test_acc:.2%}")
print(f"\nScaler mean (per feature): {scaler.mean_.round(3)}")
print(f"Scaler std  (per feature): {scaler.scale_.round(3)}")

# This fit→transform pattern is the SAME for every sklearn preprocessor
# StandardScaler, MinMaxScaler, LabelEncoder, PCA — they all work this way
"""),

md("""## 5. Jupyter Notebook Best Practices

Working in Jupyter efficiently makes you a better ML practitioner.

```
Run a cell                   : Shift + Enter
Run and insert new cell below: Alt + Enter  
Convert cell to markdown     : Esc, then M
Convert cell to code         : Esc, then Y
Delete a cell                : Esc, then D D
Move cell up/down            : Esc, then K / J
Show function documentation  : Shift + Tab inside the function call
```

**Structuring a good notebook:**
1. Start with a markdown cell explaining the purpose of the notebook
2. Group related code into logical sections with markdown headers
3. Keep each cell focused on one task
4. Run cells in order — avoid hidden state bugs
5. Restart and run all before sharing (`Kernel → Restart & Run All`)
"""),

md("""## Exercises

1. **NumPy**: Create a 5x5 matrix of random integers between 1 and 100. Compute the mean of each column, find the column with the highest mean, and normalise the entire matrix to have values between 0 and 1.

2. **Matplotlib**: Using the `loss_history` concept from Lesson 1.1, generate a realistic-looking training curve (train loss decreasing faster than val loss, with slight noise) and plot it with proper labels, legend, and gridlines.

3. **scikit-learn API**: Create a `StandardScaler`, fit it on a training set of 100 random samples with 4 features, and confirm that after transformation the mean of each column is approximately 0 and the standard deviation is approximately 1.

4. **Research**: Look up the difference between `fit_transform()` and `fit()` + `transform()` in scikit-learn. Why is using `fit_transform()` on test data a data leakage problem?

---

## Summary

| Library | Core purpose | Key objects |
|---|---|---|
| NumPy | Fast array operations and linear algebra | `ndarray` |
| pandas | Tabular data manipulation | `DataFrame`, `Series` |
| matplotlib | Plotting and visualisation | `Figure`, `Axes` |
| scikit-learn | ML algorithms and preprocessing | `fit`, `transform`, `predict` |

**Next — Lesson 1.4: Reading and Writing Data**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1.4 — Reading and Writing Data
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_1_4_Reading_and_Writing_Data.ipynb", [
md("""# Lesson 1.4 — Reading and Writing Data
### Coding Essentials for Agents | AgenticLabs.ng

---

## Learning Objectives
- Load data from CSV and JSON files into pandas DataFrames
- Perform systematic data inspection and quality checks
- Handle missing values, duplicates, and incorrect data types
- Write clean, processed data back to disk
- Build a reusable data loading function for ML pipelines

---

## Data is the Starting Point for Everything

Before any model can be trained, data must be loaded, inspected, and cleaned. Studies consistently show that data preparation accounts for 60–80% of the work in real ML projects. A practitioner who can move quickly and accurately through this step has a significant advantage.
"""),
code("""import pandas as pd
import numpy as np
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
print("Libraries imported")
"""),

code("""# ── Create sample data files to work with ─────────────────────────────────────
# (In your real work, you will load files that already exist)

# Generate a realistic loan application dataset
n = 200
data = {
    "applicant_id"   : [f"APP_{i:04d}" for i in range(1, n+1)],
    "age"            : np.random.randint(18, 70, n).tolist(),
    "employment_type": np.random.choice(["employed", "self-employed", "unemployed", "student"], n).tolist(),
    "annual_income"  : np.where(
        np.random.rand(n) > 0.1,
        np.random.lognormal(11, 0.5, n).astype(int),
        None                              # 10% missing income values
    ).tolist(),
    "credit_score"   : np.random.randint(500, 850, n).tolist(),
    "loan_amount"    : np.random.randint(2000, 50000, n).tolist(),
    "loan_purpose"   : np.random.choice(["education", "home", "vehicle", "business", "personal"], n).tolist(),
    "approved"       : np.random.choice([0, 1], n, p=[0.35, 0.65]).tolist(),
}

# Introduce some data quality issues deliberately
data["age"][15]          = -5        # invalid age
data["credit_score"][30] = 9999      # invalid credit score
data["credit_score"][55] = None      # missing credit score
data["applicant_id"][80] = "APP_0001"   # duplicate ID

# Save as CSV and JSON
df_raw = pd.DataFrame(data)
df_raw.to_csv("loan_applications.csv", index=False)

# Save first 20 records as JSON
records = df_raw.head(20).to_dict(orient="records")
with open("loan_sample.json", "w") as f:
    json.dump(records, f, indent=2)

print(f"Created: loan_applications.csv ({n} rows)")
print(f"Created: loan_sample.json (20 records)")
"""),

md("## 1. Loading Data"),
code("""# ── Reading CSV files ─────────────────────────────────────────────────────────

# Basic load
df = pd.read_csv("loan_applications.csv")

# pd.read_csv has many useful parameters:
# sep         : delimiter (default comma — use '\t' for TSV)
# header      : row number for column names (default 0)
# index_col   : column to use as row index
# dtype       : specify data types upfront
# na_values   : additional strings to treat as NaN (e.g. "N/A", "unknown")
# usecols     : only load specific columns (saves memory on large files)
# nrows       : load only the first N rows (useful for quick inspection)

# Load only specific columns
df_small = pd.read_csv("loan_applications.csv", usecols=["applicant_id", "age", "credit_score", "approved"])
print("Selective load shape:", df_small.shape)

print("\nFull dataset:")
print(df.head())
print(f"\nShape: {df.shape}")
"""),

code("""# ── Reading JSON files ────────────────────────────────────────────────────────

# JSON as list of records (most common API response format)
with open("loan_sample.json", "r") as f:
    raw_json = json.load(f)

# Convert to DataFrame
df_json = pd.DataFrame(raw_json)
print("From JSON:")
print(df_json.head(3))
print(f"\nShape: {df_json.shape}")

# pandas can also read JSON directly
df_json2 = pd.read_json("loan_sample.json")
print("\nDirect read_json — same result:", df_json2.shape)
"""),

md("## 2. Systematic Data Inspection\n\nEvery time you load a new dataset, run this inspection checklist before doing anything else."),
code("""# ── The data inspection checklist ─────────────────────────────────────────────

print("=" * 55)
print("  DATA INSPECTION REPORT")
print("=" * 55)

# 1. Shape
print(f"\n1. Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

# 2. Column names and types
print("\n2. Columns and types:")
print(df.dtypes.to_string())

# 3. Missing values
print("\n3. Missing values:")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
missing_report = pd.DataFrame({"count": missing, "pct": missing_pct})
print(missing_report[missing_report["count"] > 0])

# 4. Duplicates
n_dups = df.duplicated(subset=["applicant_id"]).sum()
print(f"\n4. Duplicate applicant IDs: {n_dups}")

# 5. Value counts for categorical columns
print("\n5. Categorical distributions:")
for col in ["employment_type", "loan_purpose", "approved"]:
    print(f"\n  {col}:")
    print(df[col].value_counts().to_string())

# 6. Numerical summary
print("\n6. Numerical summary:")
print(df[["age", "annual_income", "credit_score", "loan_amount"]].describe().round(1).to_string())
"""),

md("## 3. Handling Data Quality Issues"),
code("""# ── Fixing the data quality problems we introduced ───────────────────────────

df_clean = df.copy()

print("Before cleaning:")
print(f"  Shape            : {df_clean.shape}")
print(f"  Invalid ages (<0): {(df_clean['age'] < 0).sum()}")
print(f"  Invalid credit   : {(df_clean['credit_score'] > 850).sum()}")
print(f"  Missing income   : {df_clean['annual_income'].isnull().sum()}")
print(f"  Missing credit   : {df_clean['credit_score'].isnull().sum()}")
print(f"  Duplicate IDs    : {df_clean.duplicated(subset=['applicant_id']).sum()}")

# 1. Remove rows with impossible values
df_clean = df_clean[df_clean["age"].between(18, 100)]
df_clean = df_clean[df_clean["credit_score"].between(300, 850) | df_clean["credit_score"].isnull()]

# 2. Handle missing values — strategy depends on the column
# Income: fill with median (robust to outliers)
median_income = df_clean["annual_income"].median()
df_clean["annual_income"] = df_clean["annual_income"].fillna(median_income)

# Credit score: fill with median by employment type (group-aware imputation)
df_clean["credit_score"] = df_clean.groupby("employment_type")["credit_score"].transform(
    lambda x: x.fillna(x.median())
)

# 3. Remove duplicate IDs (keep first occurrence)
df_clean = df_clean.drop_duplicates(subset=["applicant_id"], keep="first")

print("\nAfter cleaning:")
print(f"  Shape            : {df_clean.shape}")
print(f"  Invalid ages (<0): {(df_clean['age'] < 0).sum()}")
print(f"  Missing income   : {df_clean['annual_income'].isnull().sum()}")
print(f"  Missing credit   : {df_clean['credit_score'].isnull().sum()}")
print(f"  Duplicate IDs    : {df_clean.duplicated(subset=['applicant_id']).sum()}")
"""),

code("""# ── Type conversion ───────────────────────────────────────────────────────────

# Ensure numeric columns are the right type
df_clean["annual_income"] = df_clean["annual_income"].astype(float)
df_clean["credit_score"]  = df_clean["credit_score"].astype(int)
df_clean["approved"]      = df_clean["approved"].astype(int)

# Categorical columns — converting to 'category' saves memory and enables cat operations
df_clean["employment_type"] = df_clean["employment_type"].astype("category")
df_clean["loan_purpose"]    = df_clean["loan_purpose"].astype("category")

print("Final data types:")
print(df_clean.dtypes)
print(f"\nMemory usage: {df_clean.memory_usage(deep=True).sum() / 1024:.1f} KB")
"""),

md("## 4. Saving Clean Data"),
code("""# ── Writing data back to disk ─────────────────────────────────────────────────

# Save as CSV (most universal format)
df_clean.to_csv("loan_applications_clean.csv", index=False)
print("Saved: loan_applications_clean.csv")

# Save as JSON
df_clean.head(20).to_json("loan_clean_sample.json", orient="records", indent=2)
print("Saved: loan_clean_sample.json")

# Save as Parquet (best for large datasets — compressed and fast to reload)
try:
    df_clean.to_parquet("loan_applications_clean.parquet", index=False)
    print("Saved: loan_applications_clean.parquet")
except Exception:
    print("(Parquet requires pyarrow — install with: pip install pyarrow)")

# Verify the save by reloading
df_verify = pd.read_csv("loan_applications_clean.csv")
print(f"\nVerified reload: {df_verify.shape} — matches expected")
"""),

md("## 5. A Reusable Data Loading Function\n\nIn real projects, your data loading logic should live in a function so it can be reused across notebooks and scripts."),
code("""# ── Production-ready data loader ──────────────────────────────────────────────

def load_and_validate(filepath: str,
                       required_columns: list,
                       target_column: str) -> pd.DataFrame:
    \"\"\"
    Load a CSV or JSON file, validate structure, and perform
    basic quality checks. Returns a clean DataFrame.

    Args:
        filepath         : path to the data file
        required_columns : list of column names that must be present
        target_column    : the label column (checked for class balance)

    Returns:
        Validated pandas DataFrame

    Raises:
        FileNotFoundError : if the file does not exist
        ValueError        : if required columns are missing
    \"\"\"
    # 1. File existence check
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # 2. Load based on extension
    ext = filepath.rsplit(".", 1)[-1].lower()
    if ext == "csv":
        df = pd.read_csv(filepath)
    elif ext == "json":
        df = pd.read_json(filepath)
    elif ext == "parquet":
        df = pd.read_parquet(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    # 3. Required column check
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # 4. Report
    n_missing = df.isnull().sum().sum()
    n_dups    = df.duplicated().sum()
    balance   = df[target_column].value_counts(normalize=True).round(3).to_dict()

    print(f"Loaded: {filepath}")
    print(f"  Shape          : {df.shape}")
    print(f"  Missing values : {n_missing}")
    print(f"  Duplicates     : {n_dups}")
    print(f"  Class balance  : {balance}")

    return df


# Use it
required = ["applicant_id", "age", "annual_income", "credit_score", "approved"]
df_loaded = load_and_validate("loan_applications_clean.csv", required, "approved")
"""),

md("""## Exercises

1. **Inspection practice**: Download any CSV dataset from Kaggle (or use the loan dataset from this lesson) and run the full inspection checklist. Report: shape, missing values, data types, and the top 3 most common values in any categorical column.

2. **Missing value strategy**: For the loan dataset, compare three imputation strategies for `annual_income`: (a) fill with mean, (b) fill with median, (c) fill with the median within each `employment_type` group. Plot a histogram of the filled values for each strategy. Which preserves the distribution best?

3. **Data loader extension**: Extend the `load_and_validate` function to also (a) drop duplicate rows automatically and (b) return a summary dictionary alongside the DataFrame.

4. **JSON parsing**: Write a function that reads the `loan_sample.json` file and returns a list of `applicant_id` values for all applicants who were approved (i.e. `approved == 1`).

---

## Summary

| Task | Tool | Key method |
|---|---|---|
| Load CSV | pandas | `pd.read_csv()` |
| Load JSON | pandas / json | `pd.read_json()` / `json.load()` |
| Inspect | pandas | `.info()`, `.describe()`, `.isnull().sum()` |
| Fix missing values | pandas | `.fillna()`, `.dropna()` |
| Fix types | pandas | `.astype()` |
| Save | pandas | `.to_csv()`, `.to_json()`, `.to_parquet()` |

**Next — Lesson 1.5: Calling External APIs**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1.5 — Calling External APIs
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_1_5_Calling_External_APIs.ipynb", [
md("""# Lesson 1.5 — Calling External APIs
### Coding Essentials for Agents | AgenticLabs.ng

---

## Learning Objectives
- Understand what REST APIs are and how they work
- Use the `requests` library to make GET and POST requests
- Parse and handle JSON API responses
- Handle errors, timeouts, and rate limits gracefully
- Call a real LLM API endpoint and process the response
- Build a reusable API client function

---

## Why APIs Matter for AI Development

Modern AI applications are built by composing services through APIs. Your Python script calls a weather API, a database API, a translation API, and an LLM API — and orchestrates their responses into something useful. This is exactly what agents do at scale.

Understanding how to call, handle, and debug APIs is therefore a foundational skill for every AI developer.
"""),
code("""# ── Install and import ────────────────────────────────────────────────────────
!pip install requests --quiet

import requests
import json
import time
import os
from typing import Optional

print("requests version:", requests.__version__)
"""),

md("## 1. HTTP Basics\n\nAPIs communicate using HTTP — the same protocol your browser uses. The main methods are:\n\n| Method | Purpose | Example |\n|---|---|---|\n| `GET` | Retrieve data | Get a list of models |\n| `POST` | Send data / create something | Submit a prompt to an LLM |\n| `PUT` | Update an existing resource | Update a user profile |\n| `DELETE` | Remove a resource | Delete a model run |"),
code("""# ── Your first API call — a public free API ────────────────────────────────────

# This public API returns exchange rates — no authentication needed
url = "https://api.exchangerate-api.com/v4/latest/USD"

response = requests.get(url, timeout=10)

# The response object contains everything
print(f"Status code  : {response.status_code}")   # 200 = success
print(f"Content type : {response.headers.get('Content-Type', 'unknown')}")
print(f"Response size: {len(response.content)} bytes")

# Parse the JSON body
data = response.json()
print(f"\nBase currency : {data['base']}")
print(f"Date          : {data['date']}")
print(f"\nSample rates  :")
for currency in ["EUR", "GBP", "NGN", "JPY", "CAD"]:
    rate = data["rates"].get(currency, "N/A")
    print(f"  USD → {currency}: {rate}")
"""),

md("## 2. Understanding the Response"),
code("""# ── Inspecting responses thoroughly ───────────────────────────────────────────

# Status codes — what they mean
status_meanings = {
    200: "OK — request succeeded",
    201: "Created — resource was created",
    400: "Bad Request — your request has an error",
    401: "Unauthorised — missing or invalid API key",
    403: "Forbidden — you don't have permission",
    404: "Not Found — endpoint doesn't exist",
    429: "Too Many Requests — rate limit exceeded",
    500: "Internal Server Error — problem on the server side",
}

print("Common HTTP Status Codes:")
for code, meaning in status_meanings.items():
    print(f"  {code}  {meaning}")

print(f"\nOur response: {response.status_code} — {status_meanings.get(response.status_code, 'Unknown')}")

# Always check before using
if response.status_code == 200:
    print("\nResponse is valid — safe to use.")
else:
    print("\nError — check before processing further.")
"""),

code("""# ── Working with the JSON response ────────────────────────────────────────────

data = response.json()

# JSON is just a Python dictionary (or list)
print("Type of response.json():", type(data))
print("Top-level keys:", list(data.keys()))

# Safe navigation — use .get() to avoid KeyError
rates = data.get("rates", {})
ngn_rate = rates.get("NGN")
print(f"\n1 USD = {ngn_rate} NGN" if ngn_rate else "NGN rate not found")

# Convert to DataFrame for analysis
import pandas as pd
rates_df = pd.DataFrame(list(rates.items()), columns=["Currency", "Rate"])
rates_df = rates_df.sort_values("Rate").reset_index(drop=True)
print(f"\nWeakest currencies vs USD (top 5):")
print(rates_df.tail(5).to_string(index=False))
print(f"\nStrongest currencies vs USD (top 5):")
print(rates_df.head(5).to_string(index=False))
"""),

md("## 3. POST Requests — Sending Data to APIs\n\nLLM APIs (like the Anthropic API, OpenAI API, and others) use POST requests where you send a JSON body and receive a generated response."),
code("""# ── POST request structure ────────────────────────────────────────────────────

# A typical LLM API call looks like this:
# (We will use httpbin.org — a request inspection service — for safe testing)

url     = "https://httpbin.org/post"
headers = {
    "Content-Type" : "application/json",
    "Authorization": "Bearer YOUR_API_KEY_WOULD_GO_HERE",
}
payload = {
    "model"      : "claude-sonnet-4-6",
    "max_tokens" : 1024,
    "messages"   : [
        {"role": "user", "content": "Explain gradient descent in two sentences."}
    ]
}

response = requests.post(url, headers=headers, json=payload, timeout=15)
echo     = response.json()

print("POST request sent successfully")
print(f"\nHeaders we sent:")
for k, v in echo["headers"].items():
    if k in ["Content-Type", "Authorization"]:
        val = v if "WOULD_GO_HERE" in v else "****"
        print(f"  {k}: {val}")

print(f"\nBody we sent (as received by server):")
body_json = json.loads(echo["data"])
print(json.dumps(body_json, indent=2))
"""),

md("## 4. Error Handling and Resilience\n\nProduction API code must handle failures gracefully. Networks fail, rate limits are hit, and APIs return errors."),
code("""# ── Robust API call with error handling and retry ─────────────────────────────

def call_api(url: str,
             method: str = "GET",
             headers: dict = None,
             payload: dict = None,
             max_retries: int = 3,
             timeout: int = 15,
             retry_delay: float = 1.0) -> Optional[dict]:
    \"\"\"
    Make an HTTP request with automatic retry on transient errors.

    Args:
        url         : API endpoint URL
        method      : 'GET' or 'POST'
        headers     : request headers (include auth token here)
        payload     : request body for POST requests
        max_retries : number of retry attempts on failure
        timeout     : seconds to wait before giving up
        retry_delay : seconds to wait between retries

    Returns:
        Parsed JSON response as a dict, or None on failure
    \"\"\"
    headers = headers or {}

    for attempt in range(1, max_retries + 1):
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, timeout=timeout)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=payload, timeout=timeout)
            else:
                raise ValueError(f"Unsupported method: {method}")

            # Raise an exception for 4xx and 5xx status codes
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            print(f"  Attempt {attempt}/{max_retries}: Request timed out.")
        except requests.exceptions.ConnectionError:
            print(f"  Attempt {attempt}/{max_retries}: Connection failed.")
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            if status == 429:
                print(f"  Attempt {attempt}/{max_retries}: Rate limit hit. Waiting {retry_delay*2:.0f}s.")
                time.sleep(retry_delay * 2)     # wait longer for rate limits
            elif status in (400, 401, 403, 404):
                print(f"  Client error {status} — not retrying.")
                return None                     # don't retry client errors
            else:
                print(f"  Attempt {attempt}/{max_retries}: Server error {status}.")
        except Exception as e:
            print(f"  Attempt {attempt}/{max_retries}: Unexpected error: {e}")

        if attempt < max_retries:
            time.sleep(retry_delay)

    print("All retry attempts failed.")
    return None


# Test it
result = call_api("https://api.exchangerate-api.com/v4/latest/USD")
if result:
    print(f"Success — got rates for {len(result['rates'])} currencies")
"""),

md("## 5. Calling an LLM API (Anthropic Claude Demo)\n\nThis is the most important section — calling an LLM API is the bridge from this course to the Agentic AI curriculum."),
code("""# ── LLM API client — ready to use with your own key ──────────────────────────

def call_llm(prompt: str,
             api_key: str,
             model: str = "claude-sonnet-4-6",
             max_tokens: int = 512,
             system_prompt: str = "You are a helpful AI assistant.") -> str:
    \"\"\"
    Send a prompt to the Anthropic Claude API and return the text response.

    Args:
        prompt        : the user message to send
        api_key       : your Anthropic API key
        model         : model identifier string
        max_tokens    : maximum tokens in the response
        system_prompt : system-level instruction for the model

    Returns:
        Generated text response as a string

    Usage:
        response = call_llm(
            prompt="Explain what a neural network is.",
            api_key="sk-ant-..."
        )
    \"\"\"
    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key"        : api_key,
        "anthropic-version": "2023-06-01",
        "content-type"     : "application/json",
    }

    payload = {
        "model"      : model,
        "max_tokens" : max_tokens,
        "system"     : system_prompt,
        "messages"   : [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["content"][0]["text"]

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        if status == 401:
            return "Error: Invalid or missing API key."
        elif status == 429:
            return "Error: Rate limit exceeded. Wait and try again."
        else:
            return f"Error: HTTP {status} — {e.response.text[:200]}"
    except Exception as e:
        return f"Error: {str(e)}"


# ── To use this with a real API key ───────────────────────────────────────────
# Option A: paste key directly (only in private notebooks, never in shared code)
# api_key = "sk-ant-YOUR-KEY-HERE"
# response = call_llm("What is gradient descent?", api_key=api_key)
# print(response)

# Option B: environment variable (the professional approach)
# In Colab: Runtime → Secrets → add ANTHROPIC_API_KEY
# Then use:
# api_key = os.environ.get("ANTHROPIC_API_KEY", "")
# response = call_llm("Explain overfitting briefly.", api_key=api_key)

print("LLM client function is ready.")
print("To test it, add your API key using the instructions above.")
print("The same pattern works for OpenAI, Cohere, Mistral, and other providers.")
"""),

code("""# ── Processing and structuring LLM responses ─────────────────────────────────
# Even without calling the API, you can practise handling the response format

# Simulate what an API response looks like
simulated_response = {
    "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "Gradient descent is an optimisation algorithm used to minimise a loss function by iteratively adjusting model parameters in the direction of the steepest decrease of the function."
        }
    ],
    "model": "claude-sonnet-4-6",
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 18,
        "output_tokens": 42
    }
}

# Extract what you need
response_text    = simulated_response["content"][0]["text"]
input_tokens     = simulated_response["usage"]["input_tokens"]
output_tokens    = simulated_response["usage"]["output_tokens"]
total_tokens     = input_tokens + output_tokens

print("Response text:")
print(f"  {response_text}")
print(f"\nToken usage:")
print(f"  Input : {input_tokens}")
print(f"  Output: {output_tokens}")
print(f"  Total : {total_tokens}")
print(f"\nEstimated cost (at $3/1M input, $15/1M output):")
cost = (input_tokens / 1_000_000 * 3) + (output_tokens / 1_000_000 * 15)
print(f"  ~${cost:.6f}")
"""),

md("""## Exercises

1. **Exchange rate tracker**: Using the exchange rate API from this lesson, write a function that accepts a list of currencies and prints a nicely formatted table showing how much 10,000 NGN is worth in each currency.

2. **Error code simulator**: Create a test that deliberately triggers each of the following error types with `requests` and verifies your `call_api` function handles each correctly: timeout (use `timeout=0.001`), 404 (use a bad URL), 200 with malformed JSON.

3. **API research**: Visit `docs.anthropic.com/en/api/messages` and read the Messages API reference. What additional parameters does the real endpoint support that our `call_llm` function doesn't currently use? Add support for one of them.

4. **Rate limit simulation**: Modify the `call_api` function to track the total number of calls made in the last 60 seconds (using `time.time()`), and raise a local warning if more than 10 calls are made in that window.

---

## Course 1 Capstone Project

Build a Python script that:
1. Loads a CSV dataset using the data loader from Lesson 1.4
2. Cleans the data using the techniques from Lesson 1.4
3. Computes basic statistics (mean, median, class balance) and prints a clean report
4. Calls a free public API (e.g. the exchange rate API) to enrich one of the features
5. Saves the enriched dataset to a new CSV file

All logic must be inside functions with docstrings and type hints.

---

## Summary

| Concept | Key method |
|---|---|
| GET request | `requests.get(url, timeout=n)` |
| POST request | `requests.post(url, headers=h, json=payload)` |
| Check success | `response.status_code == 200` or `response.raise_for_status()` |
| Parse response | `response.json()` |
| Handle errors | `try / except requests.exceptions.HTTPError` |
| Retry logic | Loop with delay, skip on client errors (4xx) |

**Course 1 complete. Next — Course 2: Building Your First ML Model**
""")
])

print("\nCourse 1 notebooks generated successfully.")