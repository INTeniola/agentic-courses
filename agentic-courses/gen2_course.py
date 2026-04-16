import json, os, numpy as np

OUT = os.path.join(os.path.dirname(__file__), "course2_first_ml_model")
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
# LESSON 2.1 — What Is Machine Learning?
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_2_1_What_Is_Machine_Learning.ipynb", [
md("""# Lesson 2.1 — What Is Machine Learning?
### Building Your First ML Model | AgenticLabs.ng

---

## Learning Objectives
- Define machine learning and explain how it differs from traditional programming
- Distinguish between supervised, unsupervised, and reinforcement learning
- Identify real-world ML applications and the data behind them
- Understand the end-to-end ML workflow
- Connect ML concepts to concrete business and technical problems

---

## The Core Idea

In traditional programming, you write explicit rules:
```
if credit_score > 700 AND income > 50000:
    approve_loan()
```

In machine learning, you show the algorithm examples of inputs and outputs, and it **learns the rules itself**:
```
model.fit(X_train, y_train)  # learn from historical data
model.predict(new_application)  # apply learned rules to new data
```

The power of this approach is that it can discover patterns far too complex for a human to write as rules.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.datasets import make_classification, make_blobs, make_regression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
print("Libraries loaded")
"""),

md("## 1. The Three Types of Machine Learning"),
code("""# ── Visualise all three paradigms ────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. SUPERVISED LEARNING — labelled data, predict a target
X_reg = np.linspace(0, 10, 50).reshape(-1, 1)
y_reg = 2.5 * X_reg.ravel() + np.random.randn(50) * 2
model_reg = LinearRegression().fit(X_reg, y_reg)
y_pred = model_reg.predict(X_reg)

axes[0].scatter(X_reg, y_reg, alpha=0.6, color="#4C72B0", s=50, label="Data points")
axes[0].plot(X_reg, y_pred, "r-", lw=2.5, label="Learned line")
axes[0].set_title("Supervised Learning\n(Regression: predict house price)", fontsize=11)
axes[0].set_xlabel("Size (sq m)"); axes[0].set_ylabel("Price ($1000s)")
axes[0].legend(fontsize=9); axes[0].grid(alpha=0.3)

# 2. UNSUPERVISED LEARNING — no labels, find structure
X_clust, _ = make_blobs(n_samples=150, centers=3, cluster_std=1.2, random_state=42)
colors_clust = ["#4C72B0", "#DD8452", "#55A868"]
# Show BEFORE clustering (no labels)
axes[1].scatter(X_clust[:, 0], X_clust[:, 1], c="gray", alpha=0.5, s=40)
axes[1].set_title("Unsupervised Learning\n(Clustering: group customers)", fontsize=11)
axes[1].set_xlabel("Feature 1"); axes[1].set_ylabel("Feature 2")
axes[1].grid(alpha=0.3)

# Add annotation arrows
for i, (x, y) in enumerate([(-3, -4), (2, 6), (8, -1)]):
    axes[1].annotate(f"Cluster {i+1}?", xy=(x, y),
                     xytext=(x+1.5, y+1.5),
                     arrowprops=dict(arrowstyle="->", color="red"),
                     fontsize=9, color="red")

# 3. REINFORCEMENT LEARNING — agent learns from rewards
# Show a simple grid world
grid = np.zeros((5, 5))
grid[0, 4] = 2   # goal
grid[2, 1] = -1  # obstacle
grid[3, 3] = -1  # obstacle

axes[2].imshow(grid, cmap="RdYlGn", vmin=-1, vmax=2)
axes[2].text(4, 0, "GOAL", ha="center", va="center", fontsize=9, fontweight="bold")
axes[2].text(1, 2, "X", ha="center", va="center", fontsize=12, color="red", fontweight="bold")
axes[2].text(3, 3, "X", ha="center", va="center", fontsize=12, color="red", fontweight="bold")
axes[2].text(0, 4, "START", ha="center", va="center", fontsize=8)
axes[2].set_title("Reinforcement Learning\n(Agent learns to navigate a maze)", fontsize=11)
axes[2].set_xticks([]); axes[2].set_yticks([])

plt.suptitle("The Three Types of Machine Learning", fontsize=13)
plt.tight_layout()
plt.show()
"""),

md("## 2. Supervised Learning in Depth\n\nThe focus of this course is supervised learning — the most widely used type in business applications."),
code("""# ── Supervised learning: two subtypes ────────────────────────────────────────

supervised_examples = {
    "Regression (predict a number)": [
        ("House prices",          "Location, size, age",           "£ price"),
        ("Sales forecasting",     "Season, ad spend, history",     "Units sold"),
        ("Loan default amount",   "Credit score, income, debt",    "$ risk"),
        ("Energy consumption",    "Temperature, time, building",   "kWh"),
    ],
    "Classification (predict a category)": [
        ("Spam detection",        "Email text, sender, links",     "spam / not spam"),
        ("Fraud detection",       "Transaction amount, location",  "fraud / legit"),
        ("Medical diagnosis",     "Patient symptoms, test results","disease / healthy"),
        ("Image recognition",     "Pixel values",                  "cat / dog / car"),
    ]
}

for task_type, examples in supervised_examples.items():
    print(f"\\n{task_type}")
    print(f"  {'Application':<25} {'Input (features)':<35} {'Output (label)'}")
    print("  " + "-" * 75)
    for app, inputs, output in examples:
        print(f"  {app:<25} {inputs:<35} {output}")
"""),

code("""# ── The supervised learning workflow visualised ───────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Left: Regression dataset
np.random.seed(42)
house_size  = np.random.uniform(50, 300, 80)
house_price = 1.8 * house_size + np.random.randn(80) * 30 + 20

axes[0].scatter(house_size, house_price, alpha=0.6, c="#4C72B0", s=60, edgecolors="white")
# Fit and draw the regression line
coef = np.polyfit(house_size, house_price, 1)
x_line = np.linspace(50, 300, 100)
axes[0].plot(x_line, np.polyval(coef, x_line), "r-", lw=2.5, label="Learned relationship")
axes[0].set_xlabel("House size (m²)"); axes[0].set_ylabel("Price (£1000s)")
axes[0].set_title("Regression: House Price Prediction"); axes[0].legend(); axes[0].grid(alpha=0.3)

# New prediction point
new_size = 175
new_price = np.polyval(coef, new_size)
axes[0].scatter([new_size], [new_price], c="green", s=150, zorder=5, marker="*",
                label=f"New house (175m²) → £{new_price:.0f}k")
axes[0].legend(fontsize=8)

# Right: Classification dataset
X_clf, y_clf = make_classification(n_samples=150, n_features=2, n_redundant=0,
                                    n_clusters_per_class=1, random_state=42)
colors = ["#DD8452" if y == 0 else "#4C72B0" for y in y_clf]
axes[1].scatter(X_clf[:, 0], X_clf[:, 1], c=colors, alpha=0.7, s=60, edgecolors="white")
axes[1].set_xlabel("Feature 1 (e.g. income)"); axes[1].set_ylabel("Feature 2 (e.g. credit score)")
axes[1].set_title("Classification: Loan Approval")
orange_patch = mpatches.Patch(color="#DD8452", label="Rejected")
blue_patch   = mpatches.Patch(color="#4C72B0", label="Approved")
axes[1].legend(handles=[orange_patch, blue_patch]); axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
"""),

md("## 3. Real-World Case Studies"),
code("""# ── How ML is used across industries ─────────────────────────────────────────

case_studies = [
    {
        "industry"    : "Finance",
        "application" : "Fraud detection",
        "input_data"  : "Transaction amount, location, time, merchant, user history",
        "output"      : "Fraud probability score",
        "algorithm"   : "Gradient Boosting (XGBoost)",
        "business_impact": "Saves millions monthly in prevented fraud"
    },
    {
        "industry"    : "Healthcare",
        "application" : "Disease diagnosis from scans",
        "input_data"  : "Medical images (X-ray, MRI), patient metadata",
        "output"      : "Diagnosis + confidence score",
        "algorithm"   : "Convolutional Neural Network (CNN)",
        "business_impact": "97% accuracy matching specialist radiologists"
    },
    {
        "industry"    : "Transport",
        "application" : "Ride-hailing route pricing",
        "input_data"  : "Route distance, time, demand, driver availability, weather",
        "output"      : "Dynamic price estimate",
        "algorithm"   : "Random Forest Regression",
        "business_impact": "Reduces idle driver time by 23%"
    },
    {
        "industry"    : "E-commerce",
        "application" : "Product recommendations",
        "input_data"  : "User purchase history, browsing, ratings, demographics",
        "output"      : "Ranked list of products to show",
        "algorithm"   : "Collaborative filtering + Neural Embedding",
        "business_impact": "35% of Amazon revenue attributed to recommendations"
    },
]

for cs in case_studies:
    print(f"Industry   : {cs['industry']}")
    print(f"Application: {cs['application']}")
    print(f"Input data : {cs['input_data']}")
    print(f"Output     : {cs['output']}")
    print(f"Algorithm  : {cs['algorithm']}")
    print(f"Impact     : {cs['business_impact']}")
    print()
"""),

md("## 4. The End-to-End ML Workflow\n\nEvery ML project — regardless of industry or algorithm — follows the same high-level workflow."),
code("""# ── The ML workflow ───────────────────────────────────────────────────────────

workflow = [
    ("1. Define the problem",
     "What are we predicting? What is the target variable? What counts as success?",
     "Loan approval: predict approved (1) or rejected (0)"),
    ("2. Collect data",
     "Gather historical examples with known outcomes",
     "10,000 past loan applications with approval decisions"),
    ("3. Explore the data",
     "Understand distributions, correlations, outliers, and missing values",
     "Credit score range, income vs approval rate, missing value patterns"),
    ("4. Preprocess",
     "Clean, encode categorical variables, scale numerical features, split data",
     "Encode employment_type, scale income, 80/20 train/test split"),
    ("5. Choose and train a model",
     "Select an appropriate algorithm and fit it to the training data",
     "Fit a LogisticRegression on X_train"),
    ("6. Evaluate",
     "Measure performance on the held-out test set using relevant metrics",
     "Accuracy 88%, F1 0.86, AUC-ROC 0.93"),
    ("7. Improve",
     "Tune hyperparameters, engineer new features, try different algorithms",
     "Add employment_years feature, tune regularisation"),
    ("8. Deploy",
     "Integrate the trained model into a product or decision system",
     "REST API that returns approval decision + probability"),
]

print("The End-to-End Machine Learning Workflow")
print("=" * 65)
for step, description, example in workflow:
    print(f"\\n{step}")
    print(f"   What   : {description}")
    print(f"   Example: {example}")
"""),

md("""## Exercises

1. **Identify the task type**: For each scenario below, state whether it is regression, binary classification, or multi-class classification:
   - Predicting the number of deliveries a driver will complete tomorrow
   - Identifying whether a bank transaction is fraudulent
   - Classifying a customer's support ticket into one of 8 categories
   - Estimating the age of a person from their photo

2. **Workflow mapping**: Pick any real-world application (not one from this lesson). Write out all 8 workflow steps as they would apply to that specific problem.

3. **Data type thinking**: For the loan approval case study, list at least 3 additional features (not already mentioned) that would likely improve prediction accuracy. For each, explain why it should matter.

---

## Summary

| Concept | Key idea |
|---|---|
| Machine learning | Learning rules from data rather than writing them manually |
| Supervised learning | Labelled data — the model learns from input-output pairs |
| Regression | Predict a continuous number |
| Classification | Predict a category |
| The ML workflow | Problem → Data → Explore → Preprocess → Train → Evaluate → Improve → Deploy |

**Next — Lesson 2.2: Preparing Your Dataset**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 2.2 — Preparing Your Dataset
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_2_2_Preparing_Your_Dataset.ipynb", [
md("""# Lesson 2.2 — Preparing Your Dataset
### Building Your First ML Model | AgenticLabs.ng

---

## Learning Objectives
- Perform feature selection and understand which variables to include
- Handle missing values, outliers, and incorrect data types
- Encode categorical variables for use in ML algorithms
- Scale numerical features appropriately
- Perform a proper train/test split with stratification
- Understand data leakage and why it invalidates models

---

## The Golden Rule of Data Preparation

Every transformation you apply must be **fit on the training set only** and then **applied to both train and test**. Fitting on the test set — even accidentally — leads to overly optimistic performance estimates that will not hold in production. This mistake, called **data leakage**, is one of the most common errors in applied ML.
"""),
code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)

# ── Create the dataset we will use throughout this lesson ─────────────────────
n = 800
data = {
    "age"             : np.random.randint(18, 70, n),
    "employment_years": np.random.uniform(0, 40, n).round(1),
    "annual_income"   : np.random.lognormal(11.0, 0.6, n).astype(int),
    "credit_score"    : np.random.randint(500, 850, n),
    "loan_amount"     : np.random.randint(5000, 100000, n),
    "employment_type" : np.random.choice(["employed", "self-employed", "unemployed", "student"], n,
                                          p=[0.55, 0.25, 0.12, 0.08]),
    "loan_purpose"    : np.random.choice(["home", "vehicle", "education", "business", "personal"], n),
    "has_mortgage"    : np.random.choice([0, 1], n, p=[0.6, 0.4]),
}

# Create a realistic target variable
score = (
    (data["credit_score"] - 500) / 350 * 0.4 +
    np.log1p(np.array(data["annual_income"])) / 14 * 0.3 +
    np.array(data["employment_years"]) / 40 * 0.2 +
    np.array(data["has_mortgage"]) * 0.1
)
data["approved"] = (score + np.random.randn(n) * 0.15 > 0.5).astype(int)

# Introduce missing values and an outlier
for i in np.random.choice(n, 60, replace=False):
    data["annual_income"][i] = None
for i in np.random.choice(n, 30, replace=False):
    data["employment_years"][i] = None
data["annual_income"][5] = 99999999   # outlier

df = pd.DataFrame(data)
print(f"Dataset shape: {df.shape}")
print(f"Class balance: {df['approved'].value_counts(normalize=True).round(2).to_dict()}")
"""),

md("## 1. Exploratory Analysis Before Preparation"),
code("""# ── Understand your data before touching it ───────────────────────────────────

fig, axes = plt.subplots(2, 3, figsize=(14, 8))

# 1. Target distribution
df["approved"].value_counts().plot(kind="bar", ax=axes[0,0], color=["#DD8452","#4C72B0"],
                                     edgecolor="white")
axes[0,0].set_title("Class Distribution"); axes[0,0].set_xlabel("")
axes[0,0].set_xticklabels(["Rejected", "Approved"], rotation=0)
axes[0,0].grid(axis="y", alpha=0.3)

# 2. Credit score by outcome
df.groupby("approved")["credit_score"].plot(kind="hist", bins=25, alpha=0.6, ax=axes[0,1])
axes[0,1].set_title("Credit Score by Approval"); axes[0,1].set_xlabel("Credit score")
axes[0,1].legend(["Rejected", "Approved"]); axes[0,1].grid(alpha=0.3)

# 3. Income distribution (with outlier visible)
axes[0,2].boxplot(df["annual_income"].dropna(), vert=False)
axes[0,2].set_title("Income Distribution (note outlier)"); axes[0,2].set_xlabel("Income")
axes[0,2].grid(alpha=0.3)

# 4. Employment type breakdown
emp_counts = df["employment_type"].value_counts()
emp_counts.plot(kind="bar", ax=axes[1,0], color="#55A868", edgecolor="white")
axes[1,0].set_title("Employment Type"); axes[1,0].set_xticklabels(emp_counts.index, rotation=30, ha="right")
axes[1,0].grid(axis="y", alpha=0.3)

# 5. Approval rate by employment type
approval_by_emp = df.groupby("employment_type")["approved"].mean().sort_values()
approval_by_emp.plot(kind="bar", ax=axes[1,1], color="#4C72B0", edgecolor="white")
axes[1,1].set_title("Approval Rate by Employment Type")
axes[1,1].set_xticklabels(approval_by_emp.index, rotation=30, ha="right")
axes[1,1].set_ylabel("Approval rate"); axes[1,1].grid(axis="y", alpha=0.3)

# 6. Correlation heatmap
numeric_cols = ["age", "employment_years", "annual_income", "credit_score", "loan_amount", "approved"]
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=axes[1,2],
            linewidths=0.5, cbar=False)
axes[1,2].set_title("Feature Correlations")

plt.suptitle("Exploratory Data Analysis — Loan Dataset", fontsize=13)
plt.tight_layout()
plt.show()
"""),

md("## 2. Feature Selection\n\nNot every column in a dataset should be a feature. Include variables that are causally or statistically related to the target — and nothing else."),
code("""# ── Selecting relevant features ───────────────────────────────────────────────

# Features we will use — and why
feature_rationale = {
    "age"             : "Life stage affects financial stability and loan risk",
    "employment_years": "Job stability correlates with repayment reliability",
    "annual_income"   : "Primary predictor of ability to repay",
    "credit_score"    : "Summarises credit history — strongest predictor",
    "loan_amount"     : "Larger loans have higher default risk",
    "employment_type" : "Employment stability varies by type",
    "loan_purpose"    : "Some purposes (e.g. education) have better repayment rates",
    "has_mortgage"    : "Existing financial commitment indicator",
}

print("Selected features and rationale:")
for feature, reason in feature_rationale.items():
    print(f"  {feature:<20} {reason}")

# Columns we deliberately exclude
excluded = {
    "applicant_id": "Unique identifier — has no predictive signal",
}
# (In a real dataset, also exclude: postcode alone, name, date of birth exact)

# Define X and y
feature_cols = list(feature_rationale.keys())
X = df[feature_cols].copy()
y = df["approved"].copy()

print(f"\\nFeature matrix shape : {X.shape}")
print(f"Target vector shape  : {y.shape}")
print(f"Feature names        : {feature_cols}")
"""),

md("## 3. Train / Test Split\n\nAlways split BEFORE any preprocessing. This ensures your test set is truly unseen."),
code("""# ── Stratified train/test split ───────────────────────────────────────────────

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size   = 0.20,       # 20% held out for testing
    random_state= 42,
    stratify    = y           # ensures class balance is maintained in both splits
)

print(f"Training set : {X_train.shape[0]:>4} rows | Approval rate: {y_train.mean():.2%}")
print(f"Test set     : {X_test.shape[0]:>4} rows | Approval rate: {y_test.mean():.2%}")
print("\\nNote: Approval rate is similar in both sets thanks to stratification.")
print("This is critical — without stratification, one split could be mostly positive")
print("or mostly negative, making your evaluation meaningless.")
"""),

md("## 4. Handling Missing Values"),
code("""# ── Imputation — fit on train, transform both ─────────────────────────────────

# Identify columns with missing values
print("Missing values in training set:")
print(X_train.isnull().sum()[X_train.isnull().sum() > 0])

# Numerical columns: impute with median (robust to outliers)
num_cols  = ["age", "employment_years", "annual_income", "credit_score", "loan_amount"]
cat_cols  = ["employment_type", "loan_purpose", "has_mortgage"]

imputer_num = SimpleImputer(strategy="median")
X_train[num_cols] = imputer_num.fit_transform(X_train[num_cols])   # fit + transform
X_test[num_cols]  = imputer_num.transform(X_test[num_cols])         # transform only!

print(f"\\nMedian values learned from training data:")
for col, med in zip(num_cols, imputer_num.statistics_):
    print(f"  {col:<20}: {med:,.0f}")

print(f"\\nMissing values remaining: {X_train.isnull().sum().sum()}")
"""),

md("## 5. Handling Outliers"),
code("""# ── Detect and cap outliers using IQR ─────────────────────────────────────────

def cap_outliers(df_train, df_test, columns, multiplier=3.0):
    \"\"\"
    Cap outliers at [Q1 - multiplier*IQR, Q3 + multiplier*IQR].
    Bounds are computed from training data only.
    \"\"\"
    bounds = {}
    for col in columns:
        Q1 = df_train[col].quantile(0.25)
        Q3 = df_train[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - multiplier * IQR
        upper = Q3 + multiplier * IQR
        bounds[col] = (lower, upper)

        before_train = df_train[col].max()
        df_train[col] = df_train[col].clip(lower, upper)
        df_test[col]  = df_test[col].clip(lower, upper)
        if before_train > upper:
            print(f"  {col}: capped {before_train:,.0f} → {upper:,.0f}")
    return df_train, df_test, bounds

print("Outlier capping:")
X_train, X_test, bounds = cap_outliers(X_train, X_test, ["annual_income", "loan_amount"])
print(f"\\nIncome bounds: {bounds['annual_income'][0]:,.0f} to {bounds['annual_income'][1]:,.0f}")
"""),

md("## 6. Encoding Categorical Variables"),
code("""# ── One-Hot Encoding for nominal categories (no order) ────────────────────────

# employment_type and loan_purpose have no natural ordering
# One-hot encoding creates a binary column for each category

ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore", drop="first")
# drop="first" avoids multicollinearity (the dummy variable trap)

# Fit on train, transform both
cols_to_encode = ["employment_type", "loan_purpose"]
train_encoded  = ohe.fit_transform(X_train[cols_to_encode])
test_encoded   = ohe.transform(X_test[cols_to_encode])

# Get the generated column names
encoded_cols = ohe.get_feature_names_out(cols_to_encode)
print("Generated OHE columns:", encoded_cols.tolist())

# Add encoded columns to the DataFrames
train_ohe = pd.DataFrame(train_encoded, columns=encoded_cols, index=X_train.index)
test_ohe  = pd.DataFrame(test_encoded,  columns=encoded_cols, index=X_test.index)

X_train = pd.concat([X_train.drop(cols_to_encode, axis=1), train_ohe], axis=1)
X_test  = pd.concat([X_test.drop(cols_to_encode,  axis=1), test_ohe],  axis=1)

print(f"\\nShape after encoding: train={X_train.shape}, test={X_test.shape}")
"""),

md("## 7. Feature Scaling"),
code("""# ── StandardScaler — zero mean, unit variance ─────────────────────────────────
# Most algorithms (logistic regression, SVM, neural networks) are sensitive to scale.
# Tree-based models (decision trees, random forests) are NOT — no scaling needed.

# Scale numerical columns only — don't scale binary/one-hot encoded columns
scale_cols = ["age", "employment_years", "annual_income", "credit_score", "loan_amount"]

scaler = StandardScaler()
X_train[scale_cols] = scaler.fit_transform(X_train[scale_cols])   # fit + transform
X_test[scale_cols]  = scaler.transform(X_test[scale_cols])         # transform only!

print("After StandardScaling (numerical features):")
print(f"  Training mean (should be ≈0): {X_train[scale_cols].mean().round(3).tolist()}")
print(f"  Training std  (should be ≈1): {X_train[scale_cols].std().round(3).tolist()}")

print(f"\\nFinal prepared shapes:")
print(f"  X_train: {X_train.shape} | y_train: {y_train.shape}")
print(f"  X_test : {X_test.shape}  | y_test : {y_test.shape}")
print(f"\\nAll column names: {X_train.columns.tolist()}")
"""),

md("## 8. Data Leakage — What to Avoid"),
code("""# ── The most common leakage mistakes ──────────────────────────────────────────

print("DATA LEAKAGE — Common Mistakes and How to Avoid Them")
print("=" * 60)

leakage_examples = [
    {
        "mistake" : "Fitting scaler on full dataset before splitting",
        "bad_code": "scaler.fit_transform(X)  # then split",
        "fix"     : "Split first, then: scaler.fit_transform(X_train); scaler.transform(X_test)"
    },
    {
        "mistake" : "Including future information as a feature",
        "bad_code": "features include 'total_loans_in_next_year'",
        "fix"     : "Only use information available at the time of prediction"
    },
    {
        "mistake" : "Imputing with stats computed on full dataset",
        "bad_code": "df['income'].fillna(df['income'].mean())",
        "fix"     : "Compute mean on X_train only: imputer.fit(X_train).transform(X_test)"
    },
    {
        "mistake" : "Using target-correlated IDs as features",
        "bad_code": "using 'customer_id' when IDs happen to correlate with outcome",
        "fix"     : "Drop all identifier columns"
    },
]

for ex in leakage_examples:
    print(f"\\nMistake : {ex['mistake']}")
    print(f"Bad code: {ex['bad_code']}")
    print(f"Fix     : {ex['fix']}")
"""),

md("""## Exercises

1. **End-to-end prep**: Load the loan dataset from Lesson 1.4 and run the full preparation pipeline from this lesson — missing values, outlier capping, encoding, and scaling. Report the final feature matrix shape.

2. **Leakage investigation**: Take a dataset of your choice, intentionally introduce data leakage by fitting the scaler on the full dataset, and compare train vs test accuracy to a correctly prepared version. How much does leakage inflate test accuracy?

3. **Feature engineering**: Create two new features from the loan dataset: `debt_to_income = loan_amount / annual_income` and `credit_age = age * credit_score`. Add them to the pipeline. Do they improve a logistic regression model's accuracy?

4. **Encoding comparison**: For the `loan_purpose` column (5 categories), compare one-hot encoding vs label encoding. Train a logistic regression on each. Which gives better performance and why?

---

## Summary

| Step | Tool | Key rule |
|---|---|---|
| Split | `train_test_split` | Split FIRST, before any preprocessing |
| Missing values | `SimpleImputer` | Fit on train only |
| Outliers | Manual IQR clip | Compute bounds on train only |
| Categorical encoding | `OneHotEncoder` | Fit on train only |
| Feature scaling | `StandardScaler` | Fit on train only |

**Next — Lesson 2.3: Training a Model**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 2.3 — Training a Model
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_2_3_Training_a_Model.ipynb", [
md("""# Lesson 2.3 — Training a Model
### Building Your First ML Model | AgenticLabs.ng

---

## Learning Objectives
- Understand the scikit-learn estimator API (fit, predict, score)
- Train a logistic regression and decision tree on the prepared loan dataset
- Understand what happens mathematically during model training
- Make and interpret predictions with confidence scores
- Save and reload a trained model for later use

---

## What "Training" Actually Means

When you call `model.fit(X_train, y_train)`, the algorithm searches for the parameter values that minimise its error on the training data. For logistic regression, these parameters are the weights (coefficients) for each feature. For a decision tree, the parameters are the split thresholds and feature choices at each node.

After fitting, the model has learned a function that maps inputs to predicted outputs.
"""),
code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import joblib
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)

# ── Recreate the prepared dataset from Lesson 2.2 ─────────────────────────────
n = 800
data = {
    "age"             : np.random.randint(18, 70, n).astype(float),
    "employment_years": np.random.uniform(0, 40, n).round(1),
    "annual_income"   : np.random.lognormal(11.0, 0.6, n).astype(float),
    "credit_score"    : np.random.randint(500, 850, n).astype(float),
    "loan_amount"     : np.random.randint(5000, 100000, n).astype(float),
    "has_mortgage"    : np.random.choice([0, 1], n, p=[0.6, 0.4]).astype(float),
}
score = (
    (data["credit_score"] - 500) / 350 * 0.4 +
    np.log1p(data["annual_income"]) / 14 * 0.3 +
    data["employment_years"] / 40 * 0.2 +
    data["has_mortgage"] * 0.1
)
y = (score + np.random.randn(n) * 0.15 > 0.5).astype(int)
X = pd.DataFrame(data)

# Quick prep
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

print(f"Ready: X_train={X_train_s.shape}, X_test={X_test_s.shape}")
print(f"Feature names: {list(X.columns)}")
"""),

md("## 1. Logistic Regression — A Linear Classifier"),
code("""# ── Training logistic regression ──────────────────────────────────────────────

# C is the inverse of regularisation strength — smaller C = more regularisation
lr_model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)

# This one line does all the learning
lr_model.fit(X_train_s, y_train)

print("Logistic Regression trained successfully.")
print(f"\\nModel type     : {type(lr_model).__name__}")
print(f"Num features   : {lr_model.n_features_in_}")
print(f"Classes        : {lr_model.classes_}")
print(f"Iterations used: {lr_model.n_iter_[0]} (of max 1000)")
"""),

code("""# ── What the model learned — the coefficients ─────────────────────────────────
feature_names = list(X.columns)
coefficients  = lr_model.coef_[0]

coef_df = pd.DataFrame({
    "Feature"    : feature_names,
    "Coefficient": coefficients,
}).sort_values("Coefficient", ascending=True)

plt.figure(figsize=(9, 5))
colors = ["#DD8452" if c < 0 else "#4C72B0" for c in coef_df["Coefficient"]]
plt.barh(coef_df["Feature"], coef_df["Coefficient"], color=colors, edgecolor="white")
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("Coefficient value")
plt.title("Logistic Regression Coefficients\n(larger positive = stronger push toward approval)")
plt.grid(alpha=0.3, axis="x")
plt.tight_layout()
plt.show()

print("\\nTop features driving approval:")
for _, row in coef_df.tail(3).iterrows():
    direction = "increases" if row["Coefficient"] > 0 else "decreases"
    print(f"  {row['Feature']:<20}: {direction} approval likelihood (coef={row['Coefficient']:.3f})")
"""),

md("## 2. Making Predictions"),
code("""# ── predict() vs predict_proba() ──────────────────────────────────────────────

# Hard predictions — the final class label
y_pred = lr_model.predict(X_test_s)

# Probability predictions — confidence scores for each class
y_proba = lr_model.predict_proba(X_test_s)
# y_proba[:, 0] = probability of class 0 (rejected)
# y_proba[:, 1] = probability of class 1 (approved)

print("First 10 predictions:")
print(f"{'Actual':>8} | {'Predicted':>9} | {'P(Approved)':>12} | {'Confidence'}")
print("-" * 50)
for i in range(10):
    actual    = y_test.iloc[i]
    predicted = y_pred[i]
    prob      = y_proba[i, 1]
    correct   = "✓" if actual == predicted else "✗"
    print(f"{actual:>8} | {predicted:>9} | {prob:>11.3f} | {correct}")
"""),

code("""# ── Decision threshold tuning ─────────────────────────────────────────────────
# Default threshold is 0.5 — you can change it based on business requirements
# In fraud detection: lower threshold = catch more fraud but more false positives
# In loan approval: higher threshold = fewer defaults but reject more good applicants

thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
print(f"{'Threshold':>10} | {'Accuracy':>9} | {'Approved %':>10} | {'Recall (approved)':>18}")
print("-" * 58)

for t in thresholds:
    y_t = (y_proba[:, 1] >= t).astype(int)
    acc = accuracy_score(y_test, y_t)
    pct = y_t.mean()
    recall = ((y_t == 1) & (y_test == 1)).sum() / (y_test == 1).sum()
    print(f"{t:>10.1f} | {acc:>9.3f} | {pct:>10.1%} | {recall:>18.3f}")
"""),

md("## 3. Decision Tree — A Non-Linear Classifier"),
code("""# ── Training a decision tree ──────────────────────────────────────────────────
# Decision trees don't need feature scaling

dt_model = DecisionTreeClassifier(
    max_depth   = 4,       # limits tree depth to prevent overfitting
    min_samples_split=20,  # node must have at least 20 samples to split
    random_state=42
)

dt_model.fit(X_train, y_train)   # note: using unscaled data

dt_train_acc = accuracy_score(y_train, dt_model.predict(X_train))
dt_test_acc  = accuracy_score(y_test,  dt_model.predict(X_test))

print(f"Decision Tree Results:")
print(f"  Train accuracy : {dt_train_acc:.3f}")
print(f"  Test accuracy  : {dt_test_acc:.3f}")
print(f"\\nTree depth : {dt_model.get_depth()}")
print(f"Num leaves : {dt_model.get_n_leaves()}")
"""),

code("""# ── Visualise the decision tree ───────────────────────────────────────────────
plt.figure(figsize=(20, 8))
plot_tree(
    dt_model,
    feature_names=feature_names,
    class_names=["Rejected", "Approved"],
    filled=True,
    rounded=True,
    fontsize=9,
    max_depth=3    # show first 3 levels for readability
)
plt.title("Decision Tree — Loan Approval (first 3 levels)", fontsize=13)
plt.tight_layout()
plt.show()
"""),

code("""# ── Feature importance (unique to tree-based models) ─────────────────────────
importances = pd.DataFrame({
    "Feature"   : feature_names,
    "Importance": dt_model.feature_importances_,
}).sort_values("Importance", ascending=True)

plt.figure(figsize=(8, 4))
plt.barh(importances["Feature"], importances["Importance"],
          color="#4C72B0", edgecolor="white")
plt.xlabel("Importance score")
plt.title("Decision Tree — Feature Importance")
plt.grid(alpha=0.3, axis="x")
plt.tight_layout()
plt.show()

print("Most important feature:", importances.iloc[-1]["Feature"])
print("This is what the tree uses first to split the data.")
"""),

md("## 4. Comparing Both Models"),
code("""# ── Side-by-side comparison ───────────────────────────────────────────────────

lr_train_acc = accuracy_score(y_train, lr_model.predict(X_train_s))
lr_test_acc  = accuracy_score(y_test,  lr_model.predict(X_test_s))

comparison = pd.DataFrame({
    "Model"           : ["Logistic Regression", "Decision Tree"],
    "Train Accuracy"  : [f"{lr_train_acc:.3f}", f"{dt_train_acc:.3f}"],
    "Test Accuracy"   : [f"{lr_test_acc:.3f}",  f"{dt_test_acc:.3f}"],
    "Interpretable"   : ["Yes (coefficients)", "Yes (tree rules)"],
    "Needs Scaling"   : ["Yes", "No"],
})
print(comparison.to_string(index=False))
print(f"\\nGap (train-test) for LR: {lr_train_acc - lr_test_acc:.3f}")
print(f"Gap (train-test) for DT: {dt_train_acc - dt_test_acc:.3f}")
print("\\nLarger gap = more overfitting. Decision trees often overfit more than LR.")
"""),

md("## 5. Saving and Loading a Trained Model"),
code("""# ── Persist your model for deployment ─────────────────────────────────────────

# Save the model and the scaler (you need both to serve predictions)
joblib.dump(lr_model, "loan_approval_model.pkl")
joblib.dump(scaler,   "feature_scaler.pkl")
print("Saved: loan_approval_model.pkl")
print("Saved: feature_scaler.pkl")

# ── Reload and serve ──────────────────────────────────────────────────────────
loaded_model  = joblib.load("loan_approval_model.pkl")
loaded_scaler = joblib.load("feature_scaler.pkl")

def predict_loan(age, employment_years, annual_income,
                  credit_score, loan_amount, has_mortgage):
    \"\"\"Predict loan approval for a new applicant.\"\"\"
    features = np.array([[age, employment_years, annual_income,
                           credit_score, loan_amount, has_mortgage]])
    scaled   = loaded_scaler.transform(features)
    proba    = loaded_model.predict_proba(scaled)[0, 1]
    decision = "APPROVED" if proba >= 0.5 else "REJECTED"
    return decision, proba

# Test with three fictional applicants
applicants = [
    (35, 8.0,  75000, 740, 20000, 0, "Young professional, good credit"),
    (22, 1.5,  28000, 580, 15000, 0, "Recent graduate, low credit score"),
    (50, 22.0, 130000, 810, 50000, 1, "Senior professional, excellent credit"),
]

print("\\nLoan Prediction Results:")
print("=" * 65)
for age, emp, inc, cs, loan, mtg, desc in applicants:
    decision, prob = predict_loan(age, emp, inc, cs, loan, mtg)
    print(f"\\n{desc}")
    print(f"  Decision    : {decision}")
    print(f"  Probability : {prob:.1%}")
"""),

md("""## Exercises

1. **Coefficient interpretation**: For the logistic regression model, identify the single feature with the strongest negative coefficient. Write a one-paragraph explanation of what this means in plain English for a loan officer.

2. **Underfitting vs overfitting**: Train decision trees with `max_depth` values of 1, 3, 5, 10, and None (unlimited). Plot train vs test accuracy for each. At what depth does overfitting clearly start?

3. **Custom threshold**: The bank's policy is to reject any application with less than 40% approval probability. Re-run predictions with this threshold and report the approval rate and accuracy compared to the default 50% threshold.

4. **Saving pipeline**: Instead of saving the model and scaler separately, create a scikit-learn `Pipeline` object that combines them, then save the single pipeline object. Reload and verify predictions match.

---

## Summary

| Concept | Key method |
|---|---|
| Train a model | `model.fit(X_train, y_train)` |
| Predict labels | `model.predict(X_test)` |
| Predict probabilities | `model.predict_proba(X_test)` |
| Inspect LR weights | `model.coef_` |
| Inspect tree importance | `model.feature_importances_` |
| Save / load | `joblib.dump()` / `joblib.load()` |

**Next — Lesson 2.4: Evaluating Model Performance**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 2.4 — Evaluating Model Performance
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_2_4_Evaluating_Model_Performance.ipynb", [
md("""# Lesson 2.4 — Evaluating Model Performance
### Building Your First ML Model | AgenticLabs.ng

---

## Learning Objectives
- Understand why accuracy alone is an insufficient metric
- Interpret confusion matrices, precision, recall, and F1-score
- Use ROC curves and AUC to evaluate probabilistic classifiers
- Know which metric to prioritise based on business context
- Apply cross-validation for robust performance estimation
- Evaluate a regression model with MSE, RMSE, and R²

---

## Why Evaluation Goes Beyond Accuracy

Consider a fraud detection model. If only 0.5% of transactions are fraudulent, a model that predicts "not fraud" for every transaction achieves **99.5% accuracy** — yet it is completely useless. The right metric depends on the cost of different types of errors in your specific context.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    roc_curve, auc, roc_auc_score,
    mean_squared_error, mean_absolute_error, r2_score
)
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)

# ── Recreate dataset ──────────────────────────────────────────────────────────
n = 800
data_d = {
    "age"             : np.random.randint(18, 70, n).astype(float),
    "employment_years": np.random.uniform(0, 40, n),
    "annual_income"   : np.random.lognormal(11.0, 0.6, n).astype(float),
    "credit_score"    : np.random.randint(500, 850, n).astype(float),
    "loan_amount"     : np.random.randint(5000, 100000, n).astype(float),
    "has_mortgage"    : np.random.choice([0, 1], n).astype(float),
}
score = (data_d["credit_score"]-500)/350*.4 + np.log1p(data_d["annual_income"])/14*.3
y = (score + np.random.randn(n)*0.15 > 0.5).astype(int)
X = pd.DataFrame(data_d)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
scaler = StandardScaler()
X_tr = scaler.fit_transform(X_train)
X_te = scaler.transform(X_test)

model = LogisticRegression(C=1.0, max_iter=1000, random_state=42).fit(X_tr, y_train)
y_pred = model.predict(X_te)
y_proba = model.predict_proba(X_te)[:, 1]

print("Models trained and predictions ready.")
"""),

md("## 1. The Confusion Matrix — The Foundation of Classification Metrics"),
code("""# ── Confusion matrix ─────────────────────────────────────────────────────────
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Visualise confusion matrix
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=axes[0],
            xticklabels=["Predicted Rejected", "Predicted Approved"],
            yticklabels=["Actual Rejected", "Actual Approved"],
            linewidths=1)
axes[0].set_title("Confusion Matrix — Loan Approval Model")

# Annotated explanation
labels_grid = np.array([
    [f"TN = {tn}\\n(Correctly rejected)", f"FP = {fp}\\n(Wrongly approved)"],
    [f"FN = {fn}\\n(Wrongly rejected)",   f"TP = {tp}\\n(Correctly approved)"]
])
color_grid = [["#55A868", "#DD8452"], ["#DD8452", "#55A868"]]

for i in range(2):
    for j in range(2):
        axes[1].add_patch(plt.Rectangle((j, 1-i), 1, 1, fill=True,
                                         color=color_grid[i][j], alpha=0.3))
        axes[1].text(j+0.5, 1.5-i, labels_grid[i][j],
                      ha="center", va="center", fontsize=10)
axes[1].set_xlim(0, 2); axes[1].set_ylim(0, 2)
axes[1].set_xticks([0.5, 1.5]); axes[1].set_yticks([0.5, 1.5])
axes[1].set_xticklabels(["Predicted Neg.", "Predicted Pos."])
axes[1].set_yticklabels(["Actual Pos.", "Actual Neg."])
axes[1].set_title("Confusion Matrix — What Each Cell Means")
axes[1].grid(False)

plt.tight_layout(); plt.show()

print(f"\\nTP={tp}  FP={fp}  FN={fn}  TN={tn}")
"""),

md("## 2. Precision, Recall, and F1"),
code("""# ── The metrics and their business meanings ───────────────────────────────────

accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall    = recall_score(y_test, y_pred)
f1        = f1_score(y_test, y_pred)

print("Classification Metrics:")
print(f"  Accuracy  : {accuracy:.3f}  — of all predictions, what fraction were correct?")
print(f"  Precision : {precision:.3f}  — of all approved loans, what fraction were correct approvals?")
print(f"  Recall    : {recall:.3f}  — of all genuinely good applicants, what fraction did we approve?")
print(f"  F1 Score  : {f1:.3f}  — harmonic mean of precision and recall")

print("\\nFull classification report:")
print(classification_report(y_test, y_pred, target_names=["Rejected", "Approved"]))
"""),

code("""# ── Precision vs Recall tradeoff ──────────────────────────────────────────────

# As we change the decision threshold, precision and recall move in opposite directions

thresholds = np.linspace(0.1, 0.9, 50)
precisions, recalls, f1s = [], [], []

for t in thresholds:
    y_t = (y_proba >= t).astype(int)
    if y_t.sum() == 0:
        precisions.append(1.0); recalls.append(0.0); f1s.append(0.0)
    else:
        precisions.append(precision_score(y_test, y_t, zero_division=0))
        recalls.append(recall_score(y_test, y_t, zero_division=0))
        f1s.append(f1_score(y_test, y_t, zero_division=0))

plt.figure(figsize=(10, 4))
plt.plot(thresholds, precisions, "b-", lw=2, label="Precision")
plt.plot(thresholds, recalls,    "r-", lw=2, label="Recall")
plt.plot(thresholds, f1s,        "g-", lw=2, label="F1")
plt.axvline(0.5, color="gray", ls="--", alpha=0.7, label="Default threshold (0.5)")
best_t = thresholds[np.argmax(f1s)]
plt.axvline(best_t, color="green", ls=":", alpha=0.7, label=f"Best F1 threshold ({best_t:.2f})")
plt.xlabel("Decision threshold")
plt.ylabel("Score")
plt.title("Precision-Recall-F1 vs Threshold")
plt.legend(); plt.grid(alpha=0.3)
plt.tight_layout(); plt.show()

print(f"\\nBusiness context matters:")
print(f"  High-risk lending: prefer high threshold (precision) → fewer bad loans approved")
print(f"  Inclusive lending: prefer low threshold (recall) → fewer good applicants rejected")
"""),

md("## 3. ROC Curve and AUC\n\nThe ROC curve shows model performance across all possible thresholds — independent of the threshold you choose to deploy."),
code("""# ── ROC curve ─────────────────────────────────────────────────────────────────

fpr, tpr, thresholds_roc = roc_curve(y_test, y_proba)
auc_score = roc_auc_score(y_test, y_proba)

# Compare with a decision tree
dt = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)
dt_proba = dt.predict_proba(X_test)[:, 1]
fpr_dt, tpr_dt, _ = roc_curve(y_test, dt_proba)
auc_dt = roc_auc_score(y_test, dt_proba)

plt.figure(figsize=(7, 6))
plt.plot(fpr, tpr, "b-", lw=2.5, label=f"Logistic Regression (AUC={auc_score:.3f})")
plt.plot(fpr_dt, tpr_dt, "g--", lw=2.5, label=f"Decision Tree (AUC={auc_dt:.3f})")
plt.plot([0,1], [0,1], "r:", lw=1.5, label="Random classifier (AUC=0.500)")
plt.fill_between(fpr, tpr, alpha=0.1, color="blue")
plt.xlabel("False Positive Rate (1 - Specificity)")
plt.ylabel("True Positive Rate (Recall)")
plt.title("ROC Curves — Loan Approval Models")
plt.legend(loc="lower right")
plt.grid(alpha=0.3)
plt.tight_layout(); plt.show()

print(f"\\nAUC Interpretation:")
print(f"  1.00 = Perfect model")
print(f"  0.90+ = Excellent")
print(f"  0.80-0.90 = Good")
print(f"  0.70-0.80 = Fair")
print(f"  0.50 = Random guessing (useless)")
print(f"\\nOur model AUC: {auc_score:.3f}")
"""),

md("## 4. Cross-Validation — More Reliable Estimates"),
code("""# ── K-Fold Cross Validation ───────────────────────────────────────────────────
# A single train/test split can be lucky or unlucky. CV averages over multiple splits.

X_scaled = scaler.fit_transform(X)   # scale full dataset for CV
cv        = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

models_cv = {
    "Logistic Regression": LogisticRegression(C=1.0, max_iter=1000, random_state=42),
    "Decision Tree"      : DecisionTreeClassifier(max_depth=4, random_state=42),
}

print("5-Fold Cross-Validation Results:")
print(f"{'Model':<25} | {'Mean Acc':>8} | {'Std':>6} | {'95% CI'}")
print("-" * 65)

for name, mod in models_cv.items():
    scores = cross_val_score(mod, X_scaled, y, cv=cv, scoring="accuracy")
    mean, std = scores.mean(), scores.std()
    ci_low, ci_high = mean - 1.96*std, mean + 1.96*std
    print(f"{name:<25} | {mean:>8.3f} | {std:>6.4f} | [{ci_low:.3f}, {ci_high:.3f}]")
    print(f"  Fold scores: {[f'{s:.3f}' for s in scores]}")
"""),

md("## 5. Regression Metrics"),
code("""# ── Evaluating regression models ─────────────────────────────────────────────

# Create a regression problem — predicting loan amount
X_reg = pd.DataFrame({
    "income"       : np.random.lognormal(11, 0.5, 400),
    "credit_score" : np.random.randint(500, 850, 400),
    "age"          : np.random.randint(22, 65, 400),
})
y_reg = 0.3 * X_reg["income"] / 1000 + \
        0.1 * X_reg["credit_score"] + \
        np.random.randn(400) * 5000 + 5000

X_tr_r, X_te_r, y_tr_r, y_te_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
sc_r = StandardScaler()
X_tr_rs = sc_r.fit_transform(X_tr_r)
X_te_rs  = sc_r.transform(X_te_r)

lr_reg = LinearRegression().fit(X_tr_rs, y_tr_r)
y_pred_r = lr_reg.predict(X_te_rs)

# ── Regression metrics ────────────────────────────────────────────────────────
mse  = mean_squared_error(y_te_r, y_pred_r)
rmse = np.sqrt(mse)
mae  = mean_absolute_error(y_te_r, y_pred_r)
r2   = r2_score(y_te_r, y_pred_r)

print("Regression Evaluation Metrics:")
print(f"  MSE  = {mse:>10,.1f}  (mean squared error — penalises large errors heavily)")
print(f"  RMSE = {rmse:>10,.1f}  (in original units — 'on average, off by £{rmse:,.0f}')")
print(f"  MAE  = {mae:>10,.1f}  (mean absolute error — more robust to outliers)")
print(f"  R²   = {r2:>10.4f}  (variance explained — 1.0 = perfect, 0 = baseline)")

# Predicted vs actual plot
plt.figure(figsize=(7, 5))
plt.scatter(y_te_r, y_pred_r, alpha=0.4, color="#4C72B0", s=30, edgecolors="white")
plt.plot([y_te_r.min(), y_te_r.max()], [y_te_r.min(), y_te_r.max()], "r--", lw=2, label="Perfect prediction")
plt.xlabel("Actual loan amount (£)"); plt.ylabel("Predicted (£)")
plt.title(f"Predicted vs Actual (R²={r2:.3f})")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout(); plt.show()
"""),

md("## 6. Choosing the Right Metric"),
code("""# ── Metric selection guide ────────────────────────────────────────────────────

metric_guide = [
    ("Fraud detection",    "Recall",    "Missing actual fraud is extremely costly"),
    ("Medical screening",  "Recall",    "False negatives (missed diagnosis) are dangerous"),
    ("Spam filter",        "Precision", "False positives (blocking real email) are very annoying"),
    ("Content moderation", "F1",        "Both types of error have real costs — balance them"),
    ("Search ranking",     "AUC-ROC",   "Ranking matters more than a specific threshold"),
    ("Loan approval",      "AUC-ROC",   "Evaluate the model's discrimination ability holistically"),
    ("Price prediction",   "RMSE",      "Errors in original units are intuitive for business"),
    ("Demand forecasting", "MAE",        "Treats all-sized errors equally — suitable for operations"),
]

print(f"{'Use Case':<25} | {'Primary Metric':<14} | Reason")
print("-" * 80)
for use_case, metric, reason in metric_guide:
    print(f"{use_case:<25} | {metric:<14} | {reason}")
"""),

md("""## Exercises

1. **Imbalanced data**: Create a highly imbalanced dataset (90% class 0, 10% class 1) and train a logistic regression. Show that 90% accuracy is misleading by computing precision, recall, and F1.

2. **Threshold optimisation**: For the fraud detection scenario, find the decision threshold that maximises recall while keeping precision above 0.60.

3. **Cross-validation comparison**: Compare logistic regression and decision tree using both accuracy and AUC-ROC with 10-fold CV. Which metric gives you more confidence in the comparison?

4. **Error analysis**: Identify the 10 test samples your model was most wrong about (highest confidence incorrect predictions). Do they share any common features? What does this suggest?

---

## Summary

| Metric | Best for | Formula |
|---|---|---|
| Accuracy | Balanced datasets | (TP+TN) / All |
| Precision | When FP is costly | TP / (TP+FP) |
| Recall | When FN is costly | TP / (TP+FN) |
| F1 | Balanced precision/recall | 2×P×R / (P+R) |
| AUC-ROC | Overall ranking ability | Area under ROC curve |
| RMSE | Regression, penalise large errors | √(mean(errors²)) |
| R² | Regression, proportion explained | 1 - SS_res/SS_tot |

**Next — Lesson 2.5: Improving Your Model**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 2.5 — Improving Your Model
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_2_5_Improving_Your_Model.ipynb", [
md("""# Lesson 2.5 — Improving Your Model
### Building Your First ML Model | AgenticLabs.ng

---

## Learning Objectives
- Apply a systematic model improvement methodology
- Perform hyperparameter tuning with GridSearchCV and RandomizedSearchCV
- Engineer new features that improve model performance
- Apply cross-validation properly in the improvement loop
- Diagnose overfitting vs underfitting and apply the right fix
- Build a final pipeline that is ready for evaluation

---

## The Improvement Loop

Model development is iterative, not linear. The professional process is:

```
Train baseline → Evaluate → Diagnose → Improve → Evaluate again → Repeat
```

Each iteration should test one change at a time so you can attribute any improvement or degradation to a specific decision.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import (train_test_split, cross_val_score,
                                      GridSearchCV, RandomizedSearchCV,
                                      StratifiedKFold, learning_curve)
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (accuracy_score, roc_auc_score,
                               classification_report)
from scipy.stats import uniform, randint
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)

# ── Setup dataset ─────────────────────────────────────────────────────────────
n = 800
data_d = {
    "age"             : np.random.randint(18, 70, n).astype(float),
    "employment_years": np.random.uniform(0, 40, n),
    "annual_income"   : np.random.lognormal(11.0, 0.6, n).astype(float),
    "credit_score"    : np.random.randint(500, 850, n).astype(float),
    "loan_amount"     : np.random.randint(5000, 100000, n).astype(float),
    "has_mortgage"    : np.random.choice([0, 1], n).astype(float),
}
score = (data_d["credit_score"]-500)/350*.4 + np.log1p(data_d["annual_income"])/14*.3
y = (score + np.random.randn(n)*0.15 > 0.5).astype(int)
X = pd.DataFrame(data_d)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
feature_names = list(X.columns)
print(f"Train: {X_train.shape} | Test: {X_test.shape}")
"""),

md("## 1. Establish a Baseline\n\nAlways start with the simplest possible model. Every improvement will be measured against this baseline."),
code("""# ── Baseline: logistic regression with default hyperparameters ───────────────
baseline_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  LogisticRegression(max_iter=1000, random_state=42))
])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

baseline_auc  = cross_val_score(baseline_pipe, X_train, y_train, cv=cv, scoring="roc_auc")
baseline_acc  = cross_val_score(baseline_pipe, X_train, y_train, cv=cv, scoring="accuracy")

print("BASELINE — Logistic Regression (default settings)")
print(f"  CV AUC      : {baseline_auc.mean():.4f} ± {baseline_auc.std():.4f}")
print(f"  CV Accuracy : {baseline_acc.mean():.4f} ± {baseline_acc.std():.4f}")
print("\nAll future improvements will be compared to this.")
"""),

md("## 2. Feature Engineering\n\nCreating informative new features is often the highest-leverage improvement you can make — more impactful than any hyperparameter tuning."),
code("""# ── Engineer new features ─────────────────────────────────────────────────────

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"
    Create derived features from the loan application data.
    All transformations are deterministic and use only same-row information.
    \"\"\"
    df = df.copy()

    # 1. Debt-to-income ratio — standard underwriting metric
    df["debt_to_income"]   = df["loan_amount"] / (df["annual_income"] + 1)

    # 2. Credit utilisation estimate
    df["income_per_credit"] = df["annual_income"] / (df["credit_score"] + 1)

    # 3. Financial maturity score
    df["financial_maturity"] = df["employment_years"] * df["credit_score"] / 1000

    # 4. Age-adjusted risk
    df["age_credit_product"] = df["age"] * df["credit_score"] / 10000

    # 5. Log income — income is log-normally distributed
    df["log_income"] = np.log1p(df["annual_income"])

    return df

X_eng_train = engineer_features(X_train)
X_eng_test  = engineer_features(X_test)

print("Original features :", len(X_train.columns))
print("After engineering :", len(X_eng_train.columns))
print("New features      :", [c for c in X_eng_train.columns if c not in X_train.columns])

# Evaluate with engineered features
eng_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  LogisticRegression(max_iter=1000, random_state=42))
])

eng_auc = cross_val_score(eng_pipe, X_eng_train, y_train, cv=cv, scoring="roc_auc")
print(f"\nWith engineered features — CV AUC: {eng_auc.mean():.4f} ± {eng_auc.std():.4f}")
print(f"Improvement vs baseline          : {eng_auc.mean() - baseline_auc.mean():+.4f}")
"""),

md("## 3. Hyperparameter Tuning"),
code("""# ── GridSearchCV — exhaustive search ─────────────────────────────────────────

param_grid = {
    "model__C"      : [0.01, 0.1, 1.0, 10.0, 100.0],
    "model__penalty": ["l1", "l2"],
    "model__solver" : ["liblinear"],
}

grid_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  LogisticRegression(max_iter=1000, random_state=42))
])

grid_search = GridSearchCV(
    grid_pipe,
    param_grid,
    cv         = cv,
    scoring    = "roc_auc",
    n_jobs     = -1,
    verbose    = 0,
    refit      = True
)
grid_search.fit(X_eng_train, y_train)

print("GridSearchCV Results:")
print(f"  Best AUC   : {grid_search.best_score_:.4f}")
print(f"  Best params: {grid_search.best_params_}")
print(f"\nImprovement vs baseline: {grid_search.best_score_ - baseline_auc.mean():+.4f}")
"""),

code("""# ── RandomizedSearchCV — faster for large search spaces ──────────────────────

rf_param_dist = {
    "model__n_estimators"     : randint(50, 300),
    "model__max_depth"        : [None, 3, 5, 8, 10],
    "model__min_samples_split": randint(2, 20),
    "model__min_samples_leaf" : randint(1, 10),
    "model__max_features"     : ["sqrt", "log2", None],
}

rf_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  RandomForestClassifier(random_state=42))
])

rand_search = RandomizedSearchCV(
    rf_pipe,
    rf_param_dist,
    n_iter     = 30,
    cv         = cv,
    scoring    = "roc_auc",
    n_jobs     = -1,
    random_state=42,
    verbose    = 0
)
rand_search.fit(X_eng_train, y_train)

print("RandomizedSearchCV (Random Forest) Results:")
print(f"  Best AUC   : {rand_search.best_score_:.4f}")
print(f"  Best params: {rand_search.best_params_}")
print(f"\nImprovement vs baseline: {rand_search.best_score_ - baseline_auc.mean():+.4f}")
"""),

md("## 4. Learning Curves — Diagnosing Overfitting vs Underfitting"),
code("""# ── Learning curves ───────────────────────────────────────────────────────────

def plot_learning_curve(estimator, X, y, title, cv, scoring="roc_auc"):
    train_sizes, train_scores, val_scores = learning_curve(
        estimator, X, y,
        cv=cv, scoring=scoring,
        train_sizes=np.linspace(0.1, 1.0, 10),
        n_jobs=-1
    )
    train_mean = train_scores.mean(axis=1)
    train_std  = train_scores.std(axis=1)
    val_mean   = val_scores.mean(axis=1)
    val_std    = val_scores.std(axis=1)

    plt.plot(train_sizes, train_mean, "b-o", ms=5, label="Train")
    plt.fill_between(train_sizes, train_mean-train_std, train_mean+train_std, alpha=0.15, color="blue")
    plt.plot(train_sizes, val_mean, "r-o", ms=5, label="Val")
    plt.fill_between(train_sizes, val_mean-val_std, val_mean+val_std, alpha=0.15, color="red")
    plt.xlabel("Training set size"); plt.ylabel(scoring.upper())
    plt.title(title); plt.legend(); plt.grid(alpha=0.3)

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

plt.sca(axes[0])
plot_learning_curve(
    Pipeline([("s", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]),
    X_eng_train, y_train,
    "Logistic Regression — Learning Curve", cv
)

plt.sca(axes[1])
plot_learning_curve(
    Pipeline([("s", StandardScaler()), ("m", RandomForestClassifier(**{
        k.replace("model__",""): v
        for k,v in rand_search.best_params_.items()
    }, random_state=42))]),
    X_eng_train, y_train,
    "Random Forest (Tuned) — Learning Curve", cv
)

plt.suptitle("Learning Curves — Diagnosing Model Behaviour", fontsize=13)
plt.tight_layout(); plt.show()

print("How to read learning curves:")
print("  Large gap (train >> val): overfitting → regularise or get more data")
print("  Both low: underfitting → more complex model or better features")
print("  Converging: well-fitted → collect more data to further improve")
"""),

md("## 5. Final Model Comparison and Selection"),
code("""# ── Compare all models on the test set ────────────────────────────────────────

models_final = {
    "Baseline LR"    : Pipeline([("s", StandardScaler()),
                                   ("m", LogisticRegression(max_iter=1000, random_state=42))]),
    "Tuned LR"       : grid_search.best_estimator_,
    "Tuned RF"       : rand_search.best_estimator_,
}

results = []
for name, pipe in models_final.items():
    pipe.fit(X_eng_train, y_train)
    y_pred  = pipe.predict(X_eng_test)
    y_proba = pipe.predict_proba(X_eng_test)[:, 1]
    results.append({
        "Model"    : name,
        "Accuracy" : accuracy_score(y_test, y_pred),
        "AUC-ROC"  : roc_auc_score(y_test, y_proba),
        "F1"       : f1_score(y_test, y_pred),
    })

results_df = pd.DataFrame(results)
print("Final Model Comparison (Test Set):")
print(results_df.to_string(index=False, float_format="%.4f"))

best_model_name = results_df.loc[results_df["AUC-ROC"].idxmax(), "Model"]
print(f"\nSelected model: {best_model_name} (highest AUC-ROC)")
"""),

code("""# ── Improvement summary ───────────────────────────────────────────────────────
improvement_log = [
    ("Baseline LR",           baseline_auc.mean(),        "Starting point"),
    ("+ Feature engineering", eng_auc.mean(),             "Added 5 derived features"),
    ("+ Hyperparameter tuning",grid_search.best_score_,   "GridSearchCV on LR"),
    ("+ Better algorithm",    rand_search.best_score_,    "Random Forest + RandomizedSearchCV"),
]

print("Model Improvement Journey:")
print(f"{'Step':<30} | {'CV AUC':>8} | {'Delta':>7} | Note")
print("-" * 75)
prev = improvement_log[0][1]
for step, score, note in improvement_log:
    delta = score - improvement_log[0][1]
    print(f"{step:<30} | {score:>8.4f} | {delta:>+7.4f} | {note}")

print(f"\nTotal improvement: {improvement_log[-1][1] - improvement_log[0][1]:+.4f} AUC")
"""),

md("""## Course 2 Capstone Project

Build a complete end-to-end ML pipeline on a dataset of your choice from Kaggle. Your deliverable should include:

1. Exploratory data analysis with at least 4 visualisations
2. A preprocessing pipeline with documented rationale for each decision
3. A baseline model and at least 2 improved versions
4. Comparison table of all models with accuracy, AUC, and F1
5. Learning curves for your best model
6. A saved, loadable model file
7. A function that accepts a new data row and returns a prediction

Suggested datasets: Titanic survival, Pima Indians diabetes, Heart disease, Customer churn.

---

## Summary

| Improvement step | Typical AUC gain | Effort |
|---|---|---|
| Establish baseline | — | Low |
| Feature engineering | +0.02 to +0.10 | Medium |
| Hyperparameter tuning | +0.01 to +0.05 | Low-medium |
| Better algorithm | +0.02 to +0.08 | Low |
| More/better data | Variable (often highest) | High |

**Course 2 complete. Next — Course 3: Foundational ML Algorithms**
""")
])

print("\nCourse 2 notebooks generated successfully.")