import json, os, numpy as np

OUT = os.path.join(os.path.dirname(__file__), "course3_ml_algorithms")
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
# LESSON 3.1 — Linear and Logistic Regression
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_3_1_Linear_and_Logistic_Regression.ipynb", [
md("""# Lesson 3.1 — Linear and Logistic Regression
### Foundational ML Algorithms | AgenticLabs.ng

---

## Learning Objectives
- Understand how linear regression models continuous outcomes
- Derive gradient descent intuitively and implement it from scratch
- Understand the logistic function and why it is used for classification
- Implement logistic regression from scratch and verify against scikit-learn
- Interpret coefficients and understand regularisation (L1, L2)
- Visualise decision boundaries for 2D classification problems

---

## Why Start Here?

Linear and logistic regression are the bedrock of supervised learning. They are interpretable, fast, and surprisingly powerful. Most importantly, understanding them deeply — especially gradient descent — gives you the intuition needed to understand neural networks, which are stacked layers of these exact same operations.

If you truly understand these two algorithms, everything that follows will make more sense.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.datasets import make_regression, make_classification
from sklearn.linear_model import LinearRegression, LogisticRegression, Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
print("Libraries ready")
"""),

md("## 1. Linear Regression — The Full Picture"),
code("""# ── Generate a realistic regression dataset ──────────────────────────────────
n = 300
experience = np.random.uniform(0, 20, n)    # years of experience
education  = np.random.randint(12, 22, n)   # years of education
salary = (
    25000 +
    3500 * experience +
    2000 * education +
    np.random.randn(n) * 8000            # irreducible noise
)

X_sal = np.column_stack([experience, education])
y_sal = salary

X_tr, X_te, y_tr, y_te = train_test_split(X_sal, y_sal, test_size=0.2, random_state=42)
sc = StandardScaler()
X_tr_s = sc.fit_transform(X_tr)
X_te_s  = sc.transform(X_te)

model = LinearRegression().fit(X_tr_s, y_tr)
y_pred = model.predict(X_te_s)

print("Linear Regression — Salary Prediction")
print(f"  Intercept      : £{model.intercept_:,.0f}")
print(f"  Coef (experience): £{model.coef_[0]:,.0f} per std unit")
print(f"  Coef (education) : £{model.coef_[1]:,.0f} per std unit")
print(f"  RMSE           : £{np.sqrt(mean_squared_error(y_te, y_pred)):,.0f}")
print(f"  R²             : {r2_score(y_te, y_pred):.3f}")

# Visualise
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for i, (col_name, col_data) in enumerate([("Experience (years)", experience), ("Education (years)", education)]):
    axes[i].scatter(col_data[:50], salary[:50], alpha=0.5, color="#4C72B0", s=50, edgecolors="white")
    axes[i].set_xlabel(col_name); axes[i].set_ylabel("Salary (£)")
    axes[i].set_title(f"Salary vs {col_name}"); axes[i].grid(alpha=0.3)
plt.suptitle("Feature Relationships — Salary Dataset", fontsize=12)
plt.tight_layout(); plt.show()
"""),

md("## 2. Gradient Descent — Built from Scratch\n\nThis is the most important section. Understanding gradient descent means understanding how all neural networks learn."),
code("""# ── Linear regression via gradient descent ────────────────────────────────────

class LinearRegressionGD:
    \"\"\"
    Linear regression trained with batch gradient descent.
    Shows exactly what sklearn's LinearRegression computes analytically.
    \"\"\"
    def __init__(self, lr=0.01, n_iterations=1000):
        self.lr = lr
        self.n_iterations = n_iterations
        self.w = None
        self.b = None
        self.loss_history = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0.0

        for i in range(self.n_iterations):
            # Forward pass
            y_hat = X @ self.w + self.b

            # Compute loss (MSE)
            loss = np.mean((y_hat - y) ** 2)
            self.loss_history.append(loss)

            # Backward pass — compute gradients
            error  = y_hat - y
            dw = (2/n_samples) * (X.T @ error)    # gradient w.r.t weights
            db = (2/n_samples) * error.sum()       # gradient w.r.t bias

            # Update parameters
            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict(self, X):
        return X @ self.w + self.b

# Train on the salary dataset
gd_model = LinearRegressionGD(lr=0.05, n_iterations=500)
gd_model.fit(X_tr_s, y_tr)

y_pred_gd = gd_model.predict(X_te_s)
rmse_gd   = np.sqrt(mean_squared_error(y_te, y_pred_gd))
r2_gd     = r2_score(y_te, y_pred_gd)

print("Gradient Descent Results:")
print(f"  RMSE: £{rmse_gd:,.0f}  |  R²: {r2_gd:.4f}")
print(f"\\nvsSklearn closed-form:")
print(f"  RMSE: £{np.sqrt(mean_squared_error(y_te, y_pred)):,.0f}  |  R²: {r2_score(y_te, y_pred):.4f}")
print("\\nThey converge to essentially the same answer — GD is just an approximation.")

# Plot loss convergence
plt.figure(figsize=(8, 3))
plt.plot(gd_model.loss_history, color="#4C72B0", lw=2)
plt.xlabel("Iteration"); plt.ylabel("MSE Loss")
plt.title("Gradient Descent Convergence — Loss Over Time")
plt.grid(alpha=0.3); plt.tight_layout(); plt.show()
"""),

md("## 3. Logistic Regression — Classification via a Sigmoid"),
code("""# ── The logistic (sigmoid) function ──────────────────────────────────────────
x = np.linspace(-8, 8, 300)
sigmoid = 1 / (1 + np.exp(-x))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(x, sigmoid, "#4C72B0", lw=2.5)
axes[0].axhline(0.5, color="gray", ls="--", alpha=0.7, label="Threshold = 0.5")
axes[0].axvline(0, color="gray", ls=":", alpha=0.5)
axes[0].fill_between(x, sigmoid, 0.5, where=(sigmoid > 0.5), alpha=0.15, color="#4C72B0", label="Approve region")
axes[0].fill_between(x, sigmoid, 0.5, where=(sigmoid < 0.5), alpha=0.15, color="#DD8452", label="Reject region")
axes[0].set_title("Sigmoid Function: σ(z) = 1/(1+e⁻ᶻ)")
axes[0].set_xlabel("z (linear combination of features)")
axes[0].set_ylabel("P(approved)"); axes[0].legend(); axes[0].grid(alpha=0.3)

# Decision boundary for 2 features
X2, y2 = make_classification(n_samples=200, n_features=2, n_redundant=0,
                               n_clusters_per_class=1, random_state=42)
lr = LogisticRegression().fit(X2, y2)

xx, yy = np.meshgrid(np.linspace(X2[:,0].min()-1, X2[:,0].max()+1, 200),
                      np.linspace(X2[:,1].min()-1, X2[:,1].max()+1, 200))
Z = lr.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,1].reshape(xx.shape)

axes[1].contourf(xx, yy, Z, levels=50, cmap="RdBu", alpha=0.6)
axes[1].contour(xx, yy, Z, levels=[0.5], colors="black", lw=2)
axes[1].scatter(X2[:,0], X2[:,1], c=y2, cmap="RdBu", edgecolors="white", s=50)
axes[1].set_title("Logistic Regression Decision Boundary\\n(contour = probability, line = threshold)")
axes[1].set_xlabel("Feature 1"); axes[1].set_ylabel("Feature 2")

plt.suptitle("Logistic Regression — The Sigmoid and Decision Boundary", fontsize=12)
plt.tight_layout(); plt.show()
"""),

code("""# ── Implementing logistic regression from scratch ─────────────────────────────

class LogisticRegressionGD:
    \"\"\"
    Binary logistic regression trained with gradient descent.
    Uses cross-entropy loss and sigmoid activation.
    \"\"\"
    def __init__(self, lr=0.1, n_iterations=1000):
        self.lr = lr; self.n_iterations = n_iterations
        self.w = None; self.b = None; self.loss_history = []

    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0.0

        for _ in range(self.n_iterations):
            y_hat = self.sigmoid(X @ self.w + self.b)

            # Cross-entropy loss
            eps = 1e-8
            loss = -np.mean(y*np.log(y_hat+eps) + (1-y)*np.log(1-y_hat+eps))
            self.loss_history.append(loss)

            # Gradients
            error = y_hat - y
            self.w -= self.lr / n_samples * (X.T @ error)
            self.b -= self.lr / n_samples * error.sum()

        return self

    def predict_proba(self, X):
        return self.sigmoid(X @ self.w + self.b)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)

# Test on the 2D dataset
sc2 = StandardScaler()
X2_tr, X2_te, y2_tr, y2_te = train_test_split(X2, y2, test_size=0.2, random_state=42)
X2_tr_s = sc2.fit_transform(X2_tr)
X2_te_s  = sc2.transform(X2_te)

lr_scratch = LogisticRegressionGD(lr=0.5, n_iterations=200)
lr_scratch.fit(X2_tr_s, y2_tr)

acc_scratch = accuracy_score(y2_te, lr_scratch.predict(X2_te_s))
acc_sklearn = accuracy_score(y2_te, LogisticRegression().fit(X2_tr_s, y2_tr).predict(X2_te_s))

print(f"From scratch accuracy: {acc_scratch:.3f}")
print(f"sklearn accuracy     : {acc_sklearn:.3f}")
print("\\nBoth converge to the same answer.")
"""),

md("## 4. Regularisation — L1 (Lasso) vs L2 (Ridge)"),
code("""# ── Effect of regularisation on coefficients ─────────────────────────────────

# Create a dataset with many features, some of which are irrelevant
np.random.seed(42)
n, d = 200, 20
X_reg = np.random.randn(n, d)
# Only first 5 features are truly informative
true_weights = np.array([3, -2, 1.5, -1, 0.5] + [0]*15)
y_reg = X_reg @ true_weights + np.random.randn(n) * 0.5

X_tr_r, X_te_r, y_tr_r, y_te_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
sc_r = StandardScaler()
X_tr_rs = sc_r.fit_transform(X_tr_r)
X_te_rs  = sc_r.transform(X_te_r)

# Fit all three models
models_reg = {
    "Linear (no reg)": LinearRegression().fit(X_tr_rs, y_tr_r),
    "Ridge (L2)"     : Ridge(alpha=1.0).fit(X_tr_rs, y_tr_r),
    "Lasso (L1)"     : Lasso(alpha=0.1).fit(X_tr_rs, y_tr_r),
}

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
feature_labels = [f"F{i+1}" for i in range(d)]
x_pos = np.arange(d)

for ax, (name, mod) in zip(axes, models_reg.items()):
    colors = ["#4C72B0" if i < 5 else "#DD8452" for i in range(d)]
    ax.bar(x_pos, mod.coef_, color=colors, edgecolor="white", alpha=0.8)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_title(name, fontsize=11)
    ax.set_xlabel("Feature"); ax.set_xticks(x_pos[::5]); ax.set_xticklabels(feature_labels[::5])
    ax.set_ylabel("Coefficient"); ax.grid(alpha=0.3, axis="y")
    n_zero = (np.abs(mod.coef_) < 0.01).sum()
    ax.set_xlabel(f"Feature ({n_zero} near-zero coefficients)")

from matplotlib.patches import Patch
legend = [Patch(color="#4C72B0", label="Truly informative"), Patch(color="#DD8452", label="Irrelevant")]
axes[0].legend(handles=legend, fontsize=8)
plt.suptitle("Regularisation Effect on Coefficients\n(Blue = informative features, Orange = irrelevant)", fontsize=12)
plt.tight_layout(); plt.show()

print("L1 (Lasso) sets irrelevant coefficients to exactly zero — feature selection built in.")
print("L2 (Ridge) shrinks all coefficients but rarely eliminates them entirely.")
"""),

md("""## Exercises

1. **Learning rate sensitivity**: Train the `LinearRegressionGD` class with learning rates of 0.001, 0.01, 0.1, and 1.0 for 300 iterations each. Plot all four loss curves on the same graph. What happens at lr=1.0?

2. **Logistic regression from scratch**: Extend `LogisticRegressionGD` to record and plot the training accuracy (not just loss) at each iteration.

3. **Regularisation path**: For Lasso regression, train models with alpha values from 0.001 to 100 (use `np.logspace`). Plot how many features have non-zero coefficients vs alpha. At what alpha value does the model become completely zero?

4. **Coefficient interpretation**: For the salary dataset, un-standardise the coefficients (multiply by the scaler's standard deviation) to get them back in £ per year. What does the coefficient for education actually mean in plain English?

---

## Summary

| Algorithm | Type | Key parameter | Regularisation |
|---|---|---|---|
| Linear regression | Regression | Coefficients (w, b) | Ridge/Lasso |
| Logistic regression | Classification | Sigmoid of linear combo | C (inverse λ) |
| Gradient descent | Optimisation | Learning rate, iterations | — |
| L1 (Lasso) | Regularisation | Alpha | Sets weights to zero |
| L2 (Ridge) | Regularisation | Alpha | Shrinks weights |

**Next — Lesson 3.2: Decision Trees and Random Forests**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 3.2 — Decision Trees and Random Forests
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_3_2_Decision_Trees_and_Random_Forests.ipynb", [
md("""# Lesson 3.2 — Decision Trees and Random Forests
### Foundational ML Algorithms | AgenticLabs.ng

---

## Learning Objectives
- Understand how decision trees split data using impurity measures
- Build a decision tree from scratch and visualise the splitting process
- Explain why single trees overfit and how ensembles fix this
- Understand bagging, feature randomness, and the random forest algorithm
- Tune decision tree and random forest hyperparameters effectively
- Interpret feature importance from tree-based models
- Apply gradient boosting (XGBoost) as a more powerful alternative

---

## The Core Idea

A decision tree repeatedly splits the data into smaller groups by asking binary questions ("Is income > £40,000?"). The goal at each split is to produce groups that are as pure as possible — ideally containing only one class.

Random forests build hundreds of these trees independently and average their predictions. The key insight is that combining many imperfect, independent models reduces variance even if no single model is great.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
print("Libraries ready")
"""),

md("## 1. How Decision Trees Split Data"),
code("""# ── Impurity measures from scratch ───────────────────────────────────────────

def gini_impurity(y):
    \"\"\"
    Gini impurity: 1 - sum(p_i^2)
    0 = perfectly pure node, 0.5 = worst case for binary classification
    \"\"\"
    if len(y) == 0: return 0
    probs = np.bincount(y, minlength=2) / len(y)
    return 1 - np.sum(probs ** 2)

def entropy(y):
    \"\"\"
    Information entropy: -sum(p_i * log2(p_i))
    0 = pure, 1 = completely impure for binary classification
    \"\"\"
    if len(y) == 0: return 0
    probs = np.bincount(y, minlength=2) / len(y)
    probs = probs[probs > 0]   # avoid log(0)
    return -np.sum(probs * np.log2(probs))

def information_gain(y_parent, y_left, y_right):
    \"\"\"Reduction in impurity from splitting parent into left and right.\"\"\"
    n = len(y_parent)
    n_l, n_r = len(y_left), len(y_right)
    gain = entropy(y_parent) - (n_l/n * entropy(y_left) + n_r/n * entropy(y_right))
    return gain

# Demonstrate on toy examples
print("Impurity Examples:")
pure_node     = np.array([0, 0, 0, 0, 0])       # all one class
impure_node   = np.array([0, 1, 0, 1, 0, 1])    # mixed
perfect_split_l = np.array([0, 0, 0])
perfect_split_r = np.array([1, 1, 1])

print(f"  Pure node (all 0s)       Gini: {gini_impurity(pure_node):.3f} | Entropy: {entropy(pure_node):.3f}")
print(f"  Impure node (50/50)      Gini: {gini_impurity(impure_node):.3f} | Entropy: {entropy(impure_node):.3f}")
print(f"\\n  IG from perfect split: {information_gain(impure_node, perfect_split_l, perfect_split_r):.3f}")
print(f"  IG from no-op split  : {information_gain(impure_node, impure_node[:3], impure_node[3:]):.3f}")
"""),

code("""# ── Visualise how a tree builds splits ───────────────────────────────────────

# 2D classification for easy visualisation
X2, y2 = make_classification(n_samples=300, n_features=2, n_redundant=0,
                               n_clusters_per_class=1, random_state=5)
X_tr2, X_te2, y_tr2, y_te2 = train_test_split(X2, y2, test_size=0.2, random_state=42)

fig, axes = plt.subplots(1, 4, figsize=(18, 4))

for i, max_d in enumerate([1, 2, 4, 10]):
    tree = DecisionTreeClassifier(max_depth=max_d, random_state=42)
    tree.fit(X_tr2, y_tr2)

    h = 0.05
    xx, yy = np.meshgrid(np.arange(X2[:,0].min()-0.5, X2[:,0].max()+0.5, h),
                          np.arange(X2[:,1].min()-0.5, X2[:,1].max()+0.5, h))
    Z = tree.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    axes[i].contourf(xx, yy, Z, alpha=0.3, cmap="RdBu")
    axes[i].scatter(X2[:,0], X2[:,1], c=y2, cmap="RdBu", s=25, edgecolors="white", lw=0.3)

    tr_acc = accuracy_score(y_tr2, tree.predict(X_tr2))
    te_acc = accuracy_score(y_te2, tree.predict(X_te2))
    axes[i].set_title(f"Depth={max_d}\\nTrain:{tr_acc:.2f} | Test:{te_acc:.2f}", fontsize=10)
    axes[i].set_xlabel("Feature 1")
    if i == 0: axes[i].set_ylabel("Feature 2")

plt.suptitle("Decision Tree Complexity: Underfitting → Overfitting", fontsize=12)
plt.tight_layout(); plt.show()
print("Note: depth=1 underfits, depth=10 perfectly memorises training data (overfits).")
"""),

md("## 2. Random Forests — From Trees to Ensembles"),
code("""# ── Why random forests work ───────────────────────────────────────────────────

# Use breast cancer dataset — a real binary classification problem
cancer = load_breast_cancer()
X_c, y_c = cancer.data, cancer.target
X_tr_c, X_te_c, y_tr_c, y_te_c = train_test_split(X_c, y_c, test_size=0.2,
                                                    stratify=y_c, random_state=42)

# Single tree
single_tree = DecisionTreeClassifier(random_state=42)
single_tree.fit(X_tr_c, y_tr_c)

# Random forest
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_tr_c, y_tr_c)

print(f"Breast Cancer Dataset — {X_c.shape[0]} samples, {X_c.shape[1]} features")
print(f"\\nSingle Decision Tree:")
print(f"  Train accuracy : {accuracy_score(y_tr_c, single_tree.predict(X_tr_c)):.3f}")
print(f"  Test accuracy  : {accuracy_score(y_te_c, single_tree.predict(X_te_c)):.3f}")
print(f"  Test AUC       : {roc_auc_score(y_te_c, single_tree.predict_proba(X_te_c)[:,1]):.3f}")

print(f"\\nRandom Forest (100 trees):")
print(f"  Train accuracy : {accuracy_score(y_tr_c, rf.predict(X_tr_c)):.3f}")
print(f"  Test accuracy  : {accuracy_score(y_te_c, rf.predict(X_te_c)):.3f}")
print(f"  Test AUC       : {roc_auc_score(y_te_c, rf.predict_proba(X_te_c)[:,1]):.3f}")
"""),

code("""# ── Forest size — how many trees do you need? ─────────────────────────────────

n_trees_range = [1, 5, 10, 25, 50, 100, 200, 500]
test_accs, test_aucs = [], []

for n in n_trees_range:
    rf_n = RandomForestClassifier(n_estimators=n, random_state=42, n_jobs=-1)
    rf_n.fit(X_tr_c, y_tr_c)
    test_accs.append(accuracy_score(y_te_c, rf_n.predict(X_te_c)))
    test_aucs.append(roc_auc_score(y_te_c, rf_n.predict_proba(X_te_c)[:,1]))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.semilogx(n_trees_range, test_accs, "b-o", ms=6)
ax1.set_xlabel("Number of trees"); ax1.set_ylabel("Test Accuracy")
ax1.set_title("Accuracy vs Number of Trees"); ax1.grid(alpha=0.3)

ax2.semilogx(n_trees_range, test_aucs, "r-o", ms=6)
ax2.set_xlabel("Number of trees"); ax2.set_ylabel("Test AUC-ROC")
ax2.set_title("AUC vs Number of Trees"); ax2.grid(alpha=0.3)

plt.suptitle("Random Forest: Performance Converges After ~100 Trees", fontsize=12)
plt.tight_layout(); plt.show()
print("Adding trees beyond ~100 gives diminishing returns. 100-300 is usually the sweet spot.")
"""),

md("## 3. Feature Importance"),
code("""# ── Tree-based feature importance ────────────────────────────────────────────

importances = rf.feature_importances_
indices = np.argsort(importances)[::-1][:15]    # top 15 features
top_names = [cancer.feature_names[i] for i in indices]
top_imps  = importances[indices]

plt.figure(figsize=(10, 5))
colors = ["#4C72B0"] * 5 + ["#88a8d4"] * 10
plt.barh(range(len(top_names)), top_imps[::-1], color=colors[::-1], edgecolor="white")
plt.yticks(range(len(top_names)), top_names[::-1])
plt.xlabel("Feature Importance (Mean Decrease in Impurity)")
plt.title("Random Forest — Top 15 Most Important Features")
plt.grid(alpha=0.3, axis="x"); plt.tight_layout(); plt.show()

print(f"Most important feature: {cancer.feature_names[indices[0]]}")
print(f"Importance score      : {importances[indices[0]]:.4f}")
print(f"\\nTop 5 features account for {sum(top_imps[:5]):.1%} of total importance")
"""),

md("## 4. Gradient Boosting — Sequential Ensembles"),
code("""# ── Gradient Boosting vs Random Forest ───────────────────────────────────────
# While RF trains trees in parallel and averages, GB trains them sequentially
# — each new tree corrects the errors of all previous trees

from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(
    n_estimators  = 100,
    learning_rate = 0.1,
    max_depth     = 3,
    random_state  = 42
)
gb.fit(X_tr_c, y_tr_c)

print("Algorithm Comparison — Breast Cancer Dataset:")
print(f"{'Algorithm':<30} | {'Train Acc':>9} | {'Test Acc':>8} | {'AUC':>6}")
print("-" * 60)

for name, mod in [
    ("Decision Tree", single_tree),
    ("Random Forest (100)", rf),
    ("Gradient Boosting (100)", gb),
]:
    tr_acc = accuracy_score(y_tr_c, mod.predict(X_tr_c))
    te_acc = accuracy_score(y_te_c, mod.predict(X_te_c))
    auc    = roc_auc_score(y_te_c, mod.predict_proba(X_te_c)[:,1])
    print(f"{name:<30} | {tr_acc:>9.3f} | {te_acc:>8.3f} | {auc:>6.3f}")

print("\\nGradient Boosting often outperforms Random Forest")
print("but is more sensitive to hyperparameters and slower to train.")
"""),

code("""# ── Staged predictions — watch the boosting process ───────────────────────────
# GB allows us to see performance as each new tree is added

staged_accs = []
for i, y_staged in enumerate(gb.staged_predict(X_te_c)):
    staged_accs.append(accuracy_score(y_te_c, y_staged))

plt.figure(figsize=(9, 4))
plt.plot(staged_accs, color="#4C72B0", lw=2)
plt.xlabel("Number of boosting rounds")
plt.ylabel("Test Accuracy")
plt.title("Gradient Boosting — Performance as Trees Are Added")
plt.axhline(accuracy_score(y_te_c, rf.predict(X_te_c)),
            color="red", ls="--", label=f"Random Forest baseline")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout(); plt.show()
"""),

md("""## Exercises

1. **Build a tree by hand**: On a paper or in code, manually compute the information gain for two possible splits on the following small dataset:
   - Feature A threshold 5: left=[0,0,0,1], right=[1,1,0,1]
   - Feature B threshold 3: left=[0,0,1,0], right=[1,1,0,1]
   Which split should the tree choose?

2. **Depth sensitivity**: Train decision trees with depths 1 through 20. Plot train and test accuracy. At what depth does overfitting visually begin?

3. **OOB score**: Enable `oob_score=True` in `RandomForestClassifier`. How does the OOB score compare to the proper test set score? What is OOB scoring and why is it useful?

4. **XGBoost**: Install `xgboost` and compare it against `GradientBoostingClassifier` on the breast cancer dataset. Does it run faster? Does it score better?

---

## Summary

| Algorithm | Key strength | Main weakness | Best for |
|---|---|---|---|
| Decision Tree | Fully interpretable | Overfits easily | Explainability-first use cases |
| Random Forest | Robust, fast to tune | Less interpretable | Most classification/regression tasks |
| Gradient Boosting | Often best accuracy | Sensitive to overfitting | Tabular data competitions |

**Next — Lesson 3.3: K-Nearest Neighbours and Clustering**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 3.3 — K-Nearest Neighbours and Clustering
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_3_3_KNN_and_Clustering.ipynb", [
md("""# Lesson 3.3 — K-Nearest Neighbours and Clustering
### Foundational ML Algorithms | AgenticLabs.ng

---

## Learning Objectives
- Understand instance-based learning and the KNN algorithm
- Implement KNN classification from scratch
- Know when KNN is and is not appropriate
- Understand K-Means clustering as an unsupervised algorithm
- Apply K-Means for customer segmentation and anomaly detection
- Use the elbow method and silhouette score to choose the number of clusters
- Apply DBSCAN for density-based clustering

---

## The Core Insight

KNN and K-Means both rely on distance between data points — but for completely different purposes. KNN uses the labels of nearby training examples to classify new points. K-Means groups unlabelled points together based on proximity to centroids.

Understanding both algorithms builds your geometric intuition for how machine learning algorithms think about data.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, make_blobs, make_moons
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, silhouette_score, classification_report
from sklearn.model_selection import train_test_split, cross_val_score
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
print("Libraries ready")
"""),

md("## 1. K-Nearest Neighbours — Instance-Based Learning"),
code("""# ── KNN from scratch ──────────────────────────────────────────────────────────

class KNNClassifier:
    \"\"\"
    K-Nearest Neighbours: stores all training data, classifies
    new points by majority vote among the K closest training points.
    No training phase — all computation happens at prediction time.
    \"\"\"
    def __init__(self, k=5, distance="euclidean"):
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        return self

    def _dist(self, a, b):
        if self.distance == "euclidean":
            return np.sqrt(np.sum((a - b) ** 2))
        elif self.distance == "manhattan":
            return np.sum(np.abs(a - b))

    def predict_single(self, x):
        distances = [self._dist(x, xi) for xi in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_labels  = self.y_train[k_indices]
        return np.bincount(k_labels).argmax()    # majority vote

    def predict(self, X):
        return np.array([self.predict_single(x) for x in X])


# Test on a small 2D dataset
X_small, y_small = make_classification(n_samples=100, n_features=2, n_redundant=0,
                                        n_clusters_per_class=1, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X_small, y_small, test_size=0.2, random_state=42)

sc = StandardScaler()
X_tr_s = sc.fit_transform(X_tr)
X_te_s  = sc.transform(X_te)

knn = KNNClassifier(k=5)
knn.fit(X_tr_s, y_tr)
y_pred = knn.predict(X_te_s)

acc_scratch = accuracy_score(y_te, y_pred)
acc_sklearn = accuracy_score(y_te, KNeighborsClassifier(n_neighbors=5).fit(X_tr_s, y_tr).predict(X_te_s))

print(f"KNN from scratch : {acc_scratch:.3f}")
print(f"sklearn KNN      : {acc_sklearn:.3f}")
"""),

code("""# ── Effect of K on decision boundary ─────────────────────────────────────────

fig, axes = plt.subplots(1, 4, figsize=(18, 4))
k_values = [1, 5, 15, 50]

for ax, k in zip(axes, k_values):
    knn_sk = KNeighborsClassifier(n_neighbors=k)
    knn_sk.fit(X_tr_s, y_tr)

    h = 0.08
    xx, yy = np.meshgrid(np.arange(X_tr_s[:,0].min()-0.5, X_tr_s[:,0].max()+0.5, h),
                          np.arange(X_tr_s[:,1].min()-0.5, X_tr_s[:,1].max()+0.5, h))
    Z = knn_sk.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.3, cmap="RdBu")
    ax.scatter(X_tr_s[:,0], X_tr_s[:,1], c=y_tr, cmap="RdBu", s=30, edgecolors="white", lw=0.3)
    ax.scatter(X_te_s[:,0], X_te_s[:,1], c=y_te, cmap="RdBu", s=60, marker="*", edgecolors="black", lw=0.5)

    tr_acc = accuracy_score(y_tr, knn_sk.predict(X_tr_s))
    te_acc = accuracy_score(y_te, knn_sk.predict(X_te_s))
    ax.set_title(f"K={k}\\nTrain:{tr_acc:.2f} | Test:{te_acc:.2f}", fontsize=10)

plt.suptitle("KNN Decision Boundaries — Small K Overfits, Large K Underfits", fontsize=12)
plt.tight_layout(); plt.show()
"""),

code("""# ── Choosing K with cross-validation ─────────────────────────────────────────
k_range = range(1, 31)
cv_scores_mean = []
cv_scores_std  = []

for k in k_range:
    knn_cv = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn_cv, X_tr_s, y_tr, cv=5, scoring="accuracy")
    cv_scores_mean.append(scores.mean())
    cv_scores_std.append(scores.std())

cv_scores_mean = np.array(cv_scores_mean)
cv_scores_std  = np.array(cv_scores_std)
best_k = k_range[np.argmax(cv_scores_mean)]

plt.figure(figsize=(9, 4))
plt.plot(k_range, cv_scores_mean, "b-o", ms=5, lw=2)
plt.fill_between(k_range, cv_scores_mean-cv_scores_std,
                  cv_scores_mean+cv_scores_std, alpha=0.2, color="blue")
plt.axvline(best_k, color="red", ls="--", label=f"Best K={best_k}")
plt.xlabel("K (number of neighbours)"); plt.ylabel("CV Accuracy")
plt.title("Choosing K via Cross-Validation"); plt.legend(); plt.grid(alpha=0.3)
plt.tight_layout(); plt.show()
print(f"Optimal K = {best_k} (CV accuracy = {cv_scores_mean[best_k-1]:.3f})")
"""),

md("## 2. K-Means Clustering — Finding Structure Without Labels"),
code("""# ── K-Means from scratch ──────────────────────────────────────────────────────

class KMeansManual:
    \"\"\"
    K-Means clustering: iteratively assigns points to the nearest centroid
    and updates centroids as the mean of assigned points.
    \"\"\"
    def __init__(self, k=3, max_iterations=100, random_state=42):
        self.k = k; self.max_iterations = max_iterations
        self.random_state = random_state
        self.centroids = None; self.labels = None; self.inertia_history = []

    def fit(self, X):
        rng = np.random.RandomState(self.random_state)
        # Initialise centroids by randomly picking K data points
        idx = rng.choice(len(X), self.k, replace=False)
        self.centroids = X[idx].copy()

        for iteration in range(self.max_iterations):
            # Assign each point to the nearest centroid
            distances = np.array([np.sqrt(((X - c) ** 2).sum(axis=1))
                                   for c in self.centroids])
            labels = distances.argmin(axis=0)

            # Compute inertia (sum of squared distances to centroids)
            inertia = sum(((X[labels==k] - self.centroids[k])**2).sum()
                          for k in range(self.k) if (labels==k).sum() > 0)
            self.inertia_history.append(inertia)

            # Update centroids
            new_centroids = np.array([X[labels == k].mean(axis=0)
                                       if (labels == k).sum() > 0
                                       else self.centroids[k]
                                       for k in range(self.k)])

            if np.allclose(self.centroids, new_centroids):
                print(f"  Converged at iteration {iteration+1}")
                break
            self.centroids = new_centroids

        self.labels = labels
        return self

    def predict(self, X):
        distances = np.array([np.sqrt(((X - c)**2).sum(axis=1)) for c in self.centroids])
        return distances.argmin(axis=0)

# Generate a clear cluster dataset
X_blobs, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)
sc2 = StandardScaler()
X_blobs_s = sc2.fit_transform(X_blobs)

kmeans_manual = KMeansManual(k=4)
kmeans_manual.fit(X_blobs_s)

# Visualise
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

axes[0].scatter(X_blobs_s[:,0], X_blobs_s[:,1], c="gray", s=30, alpha=0.5)
axes[0].set_title("Raw Data — No Labels"); axes[0].grid(alpha=0.3)

for k in range(4):
    mask = kmeans_manual.labels == k
    axes[1].scatter(X_blobs_s[mask,0], X_blobs_s[mask,1],
                     c=colors[k], s=40, alpha=0.7, label=f"Cluster {k+1}")
axes[1].scatter(kmeans_manual.centroids[:,0], kmeans_manual.centroids[:,1],
                 c="black", s=200, marker="X", zorder=5, label="Centroids")
axes[1].set_title("After K-Means Clustering (K=4)"); axes[1].legend(fontsize=8); axes[1].grid(alpha=0.3)

plt.suptitle("K-Means: Discovering Structure in Unlabelled Data", fontsize=12)
plt.tight_layout(); plt.show()
"""),

md("## 3. Choosing K — The Elbow Method and Silhouette Score"),
code("""# ── Elbow method ──────────────────────────────────────────────────────────────

k_range = range(1, 11)
inertias    = []
silhouettes = []

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_blobs_s)
    inertias.append(km.inertia_)
    if k > 1:
        silhouettes.append(silhouette_score(X_blobs_s, labels))
    else:
        silhouettes.append(0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(k_range, inertias, "b-o", ms=7, lw=2)
ax1.axvline(4, color="red", ls="--", alpha=0.7, label="True K=4")
ax1.set_xlabel("K"); ax1.set_ylabel("Inertia (WCSS)")
ax1.set_title("Elbow Method — Choose K at the Elbow")
ax1.legend(); ax1.grid(alpha=0.3)

ax2.plot(list(k_range)[1:], silhouettes[1:], "r-o", ms=7, lw=2)
ax2.axvline(4, color="red", ls="--", alpha=0.7, label="True K=4")
ax2.set_xlabel("K"); ax2.set_ylabel("Silhouette Score")
ax2.set_title("Silhouette Score — Higher is Better")
ax2.legend(); ax2.grid(alpha=0.3)

plt.suptitle("Choosing K: Elbow Method + Silhouette Score", fontsize=12)
plt.tight_layout(); plt.show()

print(f"Best K by silhouette: {np.argmax(silhouettes[1:]) + 2}")
"""),

md("## 4. Customer Segmentation — A Practical Application"),
code("""# ── Customer segmentation with K-Means ───────────────────────────────────────

np.random.seed(42)
n = 500
customers = pd.DataFrame({
    "annual_spend"    : np.random.lognormal(8, 0.8, n),
    "purchase_freq"   : np.random.randint(1, 52, n),
    "avg_order_value" : np.random.lognormal(4, 0.6, n),
    "customer_age"    : np.random.randint(18, 70, n),
    "months_active"   : np.random.randint(1, 60, n),
})

sc_cust = StandardScaler()
X_cust  = sc_cust.fit_transform(customers)

km_cust = KMeans(n_clusters=4, random_state=42, n_init=10)
customers["segment"] = km_cust.fit_predict(X_cust)

# Profile each segment
print("Customer Segment Profiles:")
print(customers.groupby("segment")[["annual_spend","purchase_freq","avg_order_value"]].mean().round(0).to_string())

segment_names = {0: "Occasional Buyer", 1: "High-Value Regular",
                  2: "Frequent Low-Spend", 3: "New/Inactive"}

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
colors_seg = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

for seg in range(4):
    mask = customers["segment"] == seg
    axes[0].scatter(customers.loc[mask, "annual_spend"],
                     customers.loc[mask, "purchase_freq"],
                     c=colors_seg[seg], alpha=0.5, s=30,
                     label=f"Seg {seg}: {segment_names.get(seg,'')}")
axes[0].set_xlabel("Annual Spend (£)"); axes[0].set_ylabel("Purchase Frequency")
axes[0].set_title("Customer Segments (Spend vs Frequency)")
axes[0].legend(fontsize=8); axes[0].grid(alpha=0.3)

seg_sizes = customers["segment"].value_counts().sort_index()
axes[1].pie(seg_sizes, labels=[f"Seg {i}" for i in seg_sizes.index],
             autopct="%1.0f%%", colors=colors_seg, startangle=90)
axes[1].set_title("Segment Sizes")

plt.suptitle("K-Means Customer Segmentation", fontsize=12)
plt.tight_layout(); plt.show()
"""),

md("""## Exercises

1. **KNN on text**: Vectorise 20 sentences using word-count vectors (bag of words), then use KNN to classify them. What happens when K=1 vs K=10?

2. **K-Means sensitivity to initialisation**: Run K-Means 10 times with different random seeds on the blobs dataset. Do you always get the same cluster assignments? Why or why not? How does `n_init` address this?

3. **DBSCAN**: Apply `sklearn.cluster.DBSCAN` to the `make_moons` dataset (which K-Means handles poorly). DBSCAN should handle the crescent shapes. Plot both K-Means and DBSCAN results side by side.

4. **Real application**: Download a customer transaction dataset from Kaggle and apply K-Means segmentation. How would you market differently to each segment?

---

## Summary

| Algorithm | Type | Key parameter | Best for |
|---|---|---|---|
| KNN | Supervised | K (number of neighbours) | Small datasets, non-linear boundaries |
| K-Means | Unsupervised | K (number of clusters) | Customer segmentation, compression |
| DBSCAN | Unsupervised | eps, min_samples | Irregular shapes, anomaly detection |

**Next — Lesson 3.4: Support Vector Machines**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 3.4 — Support Vector Machines
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_3_4_Support_Vector_Machines.ipynb", [
md("""# Lesson 3.4 — Support Vector Machines
### Foundational ML Algorithms | AgenticLabs.ng

---

## Learning Objectives
- Understand the maximum margin classifier concept
- Explain support vectors and why only they determine the decision boundary
- Understand soft margin SVM and the C hyperparameter
- Apply the kernel trick to handle non-linearly separable data
- Know when SVMs outperform simpler models
- Apply SVM for text classification (a domain where SVMs still excel)

---

## The Big Idea

Instead of finding any boundary that separates classes, SVM finds the **maximum margin boundary** — the decision surface that is as far as possible from the nearest training examples of either class. These nearest examples are called **support vectors**.

This geometry-driven approach makes SVMs theoretically elegant and very effective in high-dimensional spaces, which is why they dominated NLP before deep learning.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_circles, make_moons
from sklearn.svm import SVC, LinearSVC, SVR
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
print("Libraries ready")
"""),

md("## 1. Maximum Margin Classifier — The Core Geometry"),
code("""# ── Visualise the maximum margin concept ──────────────────────────────────────

# Generate linearly separable data
X2, y2 = make_classification(n_samples=80, n_features=2, n_redundant=0,
                               n_clusters_per_class=1, class_sep=2.0, random_state=5)
y2 = np.where(y2 == 0, -1, 1)   # SVM uses -1/+1 convention internally

X_tr, X_te, y_tr, y_te = train_test_split(X2, y2, test_size=0.25, random_state=42)
sc = StandardScaler()
X_tr_s = sc.fit_transform(X_tr)
X_te_s  = sc.transform(X_te)

# Fit a linear SVM
svm_linear = SVC(kernel="linear", C=1.0)
svm_linear.fit(X_tr_s, y_tr)

# Extract decision boundary and margins
w  = svm_linear.coef_[0]
b  = svm_linear.intercept_[0]
sv = svm_linear.support_vectors_

x_range = np.linspace(X_tr_s[:,0].min()-0.5, X_tr_s[:,0].max()+0.5, 300)

# Hyperplane: w[0]*x + w[1]*y + b = 0 → y = (-w[0]*x - b) / w[1]
y_decision = -(w[0] * x_range + b) / w[1]
y_margin_p = -(w[0] * x_range + b - 1) / w[1]
y_margin_n = -(w[0] * x_range + b + 1) / w[1]

fig, ax = plt.subplots(figsize=(9, 6))

# Plot decision regions
xx, yy = np.meshgrid(np.linspace(X_tr_s[:,0].min()-0.5, X_tr_s[:,0].max()+0.5, 200),
                      np.linspace(X_tr_s[:,1].min()-0.5, X_tr_s[:,1].max()+0.5, 200))
Z = svm_linear.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
ax.contourf(xx, yy, Z, alpha=0.15, cmap="RdBu")

# Data points
pos = y_tr == 1
ax.scatter(X_tr_s[pos,0],  X_tr_s[pos,1],  c="#4C72B0", s=60, edgecolors="white", zorder=2, label="Class +1")
ax.scatter(X_tr_s[~pos,0], X_tr_s[~pos,1], c="#DD8452", s=60, edgecolors="white", zorder=2, label="Class -1")

# Decision boundary and margins
ax.plot(x_range, y_decision, "k-",  lw=2, label="Decision boundary")
ax.plot(x_range, y_margin_p, "b--", lw=1.5, label="Margin boundary (+1)")
ax.plot(x_range, y_margin_n, "r--", lw=1.5, label="Margin boundary (-1)")
ax.fill_between(x_range, y_margin_p, y_margin_n, alpha=0.1, color="gray", label="Margin region")

# Support vectors
ax.scatter(sv[:,0], sv[:,1], s=200, linewidths=2, facecolors="none",
            edgecolors="black", zorder=4, label=f"Support vectors ({len(sv)})")

ax.legend(fontsize=9, loc="upper right"); ax.grid(alpha=0.3)
ax.set_xlabel("Feature 1"); ax.set_ylabel("Feature 2")
ax.set_title("Linear SVM — Maximum Margin Classifier\\n"
              "Only the support vectors define the decision boundary")
plt.tight_layout(); plt.show()

print(f"Number of support vectors: {len(sv)}")
print(f"Margin width             : {2 / np.linalg.norm(w):.4f}")
print(f"Test accuracy            : {accuracy_score(y_te, svm_linear.predict(X_te_s)):.3f}")
"""),

md("## 2. The Soft Margin — Handling Noisy Data (C Parameter)"),
code("""# ── Effect of C on the decision boundary ─────────────────────────────────────
# C controls the tradeoff between maximising the margin and minimising violations
# Small C = wider margin, more violations allowed (soft boundary)
# Large C = narrow margin, fewer violations (hard boundary, may overfit)

X_noisy, y_noisy = make_classification(n_samples=150, n_features=2, n_redundant=0,
                                        n_clusters_per_class=1, class_sep=0.8, random_state=7)
y_noisy = np.where(y_noisy == 0, -1, 1)
sc2 = StandardScaler()
X_noisy_s = sc2.fit_transform(X_noisy)

fig, axes = plt.subplots(1, 4, figsize=(18, 4))
C_values = [0.01, 0.1, 1.0, 100.0]

for ax, C in zip(axes, C_values):
    svm_c = SVC(kernel="linear", C=C).fit(X_noisy_s, y_noisy)

    xx, yy = np.meshgrid(np.linspace(X_noisy_s[:,0].min()-0.5, X_noisy_s[:,0].max()+0.5, 200),
                          np.linspace(X_noisy_s[:,1].min()-0.5, X_noisy_s[:,1].max()+0.5, 200))
    Z = svm_c.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.2, cmap="RdBu")
    pos = y_noisy == 1
    ax.scatter(X_noisy_s[pos,0],  X_noisy_s[pos,1],  c="#4C72B0", s=30, edgecolors="white")
    ax.scatter(X_noisy_s[~pos,0], X_noisy_s[~pos,1], c="#DD8452", s=30, edgecolors="white")
    ax.scatter(svm_c.support_vectors_[:,0], svm_c.support_vectors_[:,1],
                s=150, facecolors="none", edgecolors="black", lw=1.5)

    acc = accuracy_score(y_noisy, svm_c.predict(X_noisy_s))
    n_sv = len(svm_c.support_vectors_)
    ax.set_title(f"C={C}\\nAcc={acc:.2f} | SVs={n_sv}", fontsize=10)
    ax.grid(alpha=0.2)

plt.suptitle("Soft Margin SVM — Effect of C Hyperparameter\\n"
              "Small C = Generous margin | Large C = Strict margin", fontsize=11)
plt.tight_layout(); plt.show()
"""),

md("## 3. The Kernel Trick — Non-Linear SVM"),
code("""# ── Kernels for non-linearly separable data ───────────────────────────────────
# The kernel trick implicitly maps data to higher dimensions where it becomes
# linearly separable, without ever computing the transformation explicitly.

X_circles, y_circles = make_circles(n_samples=200, noise=0.1, factor=0.4, random_state=42)
X_moons, y_moons     = make_moons(n_samples=200, noise=0.1, random_state=42)

sc_k = StandardScaler()

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
datasets = [("Circles", X_circles, y_circles), ("Moons", X_moons, y_moons)]

for row_idx, (name, X_k, y_k) in enumerate(datasets):
    X_k_s = sc_k.fit_transform(X_k)
    kernels = [
        ("Linear",  SVC(kernel="linear",  C=1.0)),
        ("RBF",     SVC(kernel="rbf",     C=1.0, gamma="scale")),
        ("Poly d=3",SVC(kernel="poly",    C=1.0, degree=3)),
    ]
    for col_idx, (kern_name, svm_k) in enumerate(kernels):
        ax = axes[row_idx, col_idx]
        svm_k.fit(X_k_s, y_k)

        h = 0.05
        xx, yy = np.meshgrid(np.arange(X_k_s[:,0].min()-0.5, X_k_s[:,0].max()+0.5, h),
                               np.arange(X_k_s[:,1].min()-0.5, X_k_s[:,1].max()+0.5, h))
        Z = svm_k.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

        ax.contourf(xx, yy, Z, alpha=0.3, cmap="RdBu")
        ax.scatter(X_k_s[:,0], X_k_s[:,1], c=y_k, cmap="RdBu", s=30, edgecolors="white", lw=0.3)

        acc = accuracy_score(y_k, svm_k.predict(X_k_s))
        ax.set_title(f"{name} — {kern_name}\\nAcc: {acc:.2f}", fontsize=10)
        ax.grid(alpha=0.2)

plt.suptitle("Kernel SVM — RBF Handles Non-Linear Patterns", fontsize=12)
plt.tight_layout(); plt.show()

print("Key insight: Linear SVM fails on circles and moons.")
print("RBF kernel implicitly maps data to infinite dimensions where it becomes separable.")
"""),

md("## 4. SVM for Text Classification — A Real-World Win"),
code("""# ── SVM on high-dimensional text data ────────────────────────────────────────
# SVMs with linear kernels were the gold standard for text classification
# before deep learning. They still outperform many neural networks on small datasets.

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

# Load two news categories — a binary classification problem
categories = ["sci.space", "talk.politics.guns"]
newsgroups = fetch_20newsgroups(subset="all", categories=categories,
                                  remove=("headers","footers","quotes"))
X_text, y_text = newsgroups.data, newsgroups.target

X_tr_t, X_te_t, y_tr_t, y_te_t = train_test_split(X_text, y_text, test_size=0.2,
                                                     stratify=y_text, random_state=42)

print(f"Dataset: {len(X_text)} documents | 2 categories")
print(f"Categories: {newsgroups.target_names}")
print(f"\\nSample document (truncated):\\n{X_text[0][:200]}...")
"""),

code("""# ── Build SVM text classifier ────────────────────────────────────────────────

text_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=10000, ngram_range=(1,2),
                               sublinear_tf=True, min_df=3)),
    ("svm",   LinearSVC(C=1.0, max_iter=2000))
])

text_pipeline.fit(X_tr_t, y_tr_t)
y_pred_t = text_pipeline.predict(X_te_t)

print("SVM Text Classification Results:")
print(f"  Test Accuracy: {accuracy_score(y_te_t, y_pred_t):.3f}")
print()
print(classification_report(y_te_t, y_pred_t, target_names=newsgroups.target_names))

# Most discriminative words
vectoriser = text_pipeline.named_steps["tfidf"]
svm_model  = text_pipeline.named_steps["svm"]
feature_names_arr = vectoriser.get_feature_names_out()
coef = svm_model.coef_[0]

top_pos = feature_names_arr[np.argsort(coef)[-10:]]
top_neg = feature_names_arr[np.argsort(coef)[:10]]

print(f"\\nTop words for '{newsgroups.target_names[1]}':")
print(" ", list(top_pos))
print(f"\\nTop words for '{newsgroups.target_names[0]}':")
print(" ", list(top_neg))
"""),

md("""## Exercises

1. **Hyperparameter grid search**: Apply `GridSearchCV` to find the best `C` and `gamma` for an RBF SVM on the circles dataset. How much does tuning improve accuracy?

2. **SVM vs Logistic Regression**: On the breast cancer dataset from Lesson 3.2, compare SVM (RBF kernel) with logistic regression across 5-fold CV. Which performs better? Which is faster to train?

3. **Kernel comparison**: Create a dataset with three concentric rings. Test linear, RBF, and polynomial kernels. Which generalises best?

4. **Text classification extension**: Add a third news category to the text classification task. How does SVM handle 3-class classification? Look up how scikit-learn handles multi-class SVMs internally.

---

## Summary

| Concept | Key insight |
|---|---|
| Maximum margin | SVM finds the widest possible separation between classes |
| Support vectors | Only the closest points define the boundary — the rest are ignored |
| C parameter | Small C = wide margin + more violations; Large C = narrow margin + fewer violations |
| Kernel trick | Maps data to higher dimensions implicitly — no explicit computation |
| RBF kernel | Best default for non-linear SVM; controlled by gamma parameter |

**Next — Lesson 3.5: Choosing the Right Algorithm**
""")
])

# ─────────────────────────────────────────────────────────────────────────────
# LESSON 3.5 — Choosing the Right Algorithm
# ─────────────────────────────────────────────────────────────────────────────
save("Lesson_3_5_Choosing_the_Right_Algorithm.ipynb", [
md("""# Lesson 3.5 — Choosing the Right Algorithm
### Foundational ML Algorithms | AgenticLabs.ng

---

## Learning Objectives
- Apply a systematic framework for choosing the right algorithm
- Understand the tradeoffs between interpretability, accuracy, speed, and scalability
- Compare all algorithms from this course on the same dataset
- Understand the No Free Lunch theorem and what it means in practice
- Connect classical ML algorithms to deep learning (bridge lesson)
- Build a repeatable algorithm selection workflow

---

## There Is No "Best" Algorithm

The No Free Lunch theorem proves that no single algorithm outperforms all others across all problems. The choice depends on your data, your constraints, and your requirements. This lesson gives you the tools to make that choice confidently and systematically.
"""),
code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import (make_classification, make_regression,
                               load_breast_cancer, load_diabetes)
from sklearn.linear_model  import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.tree          import DecisionTreeClassifier
from sklearn.ensemble      import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors     import KNeighborsClassifier
from sklearn.svm           import SVC
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline      import Pipeline
from sklearn.metrics       import roc_auc_score
import time
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
print("All algorithms loaded and ready for comparison")
"""),

md("## 1. The Algorithm Selection Framework"),
code("""# ── A decision framework for algorithm selection ─────────────────────────────

decision_factors = {
    "Problem type": {
        "Continuous output (predict a number)": "→ Linear Regression, Random Forest Regressor, SVR",
        "Binary output (yes/no)"              : "→ Logistic Regression, SVM, Random Forest",
        "Multi-class output (A/B/C/D)"        : "→ Softmax Logistic Regression, Random Forest, SVM (OvR)",
        "No labels (discover structure)"      : "→ K-Means, DBSCAN, PCA",
    },
    "Dataset size": {
        "Very small (<1K rows)"  : "→ SVM, KNN, Logistic Regression (high variance risk with complex models)",
        "Small (1K-10K rows)"    : "→ Any algorithm; prefer interpretable ones",
        "Medium (10K-1M rows)"   : "→ Random Forest, Gradient Boosting, Logistic Regression",
        "Large (>1M rows)"       : "→ Linear models, Gradient Boosting (XGBoost); neural networks if deep features",
    },
    "Interpretability need": {
        "Must explain every decision"    : "→ Logistic Regression (coefficients), Decision Tree (rules)",
        "General feature importance OK"  : "→ Random Forest (feature importance)",
        "Black box acceptable"           : "→ SVM (RBF), Gradient Boosting, Neural Networks",
    },
    "Data properties": {
        "High dimensional, sparse (text)": "→ Linear SVM, Logistic Regression (L1)",
        "Non-linear relationships"       : "→ Random Forest, Gradient Boosting, SVM (RBF), Neural Networks",
        "Many missing values"            : "→ Random Forest (handles naturally), XGBoost",
        "Outliers in features"           : "→ Tree models (split-based), avoid KNN and SVM",
    },
}

for category, factors in decision_factors.items():
    print(f"\\n{category}:")
    for condition, recommendation in factors.items():
        print(f"  {condition}")
        print(f"    {recommendation}")
"""),

md("## 2. Benchmark — All Algorithms on the Same Datasets"),
code("""# ── Side-by-side comparison on two real datasets ─────────────────────────────

# Dataset 1: Breast cancer (30 features, binary classification)
cancer = load_breast_cancer()
X_c, y_c = cancer.data, cancer.target

# Dataset 2: Synthetic non-linear (2 features, visualisable)
X_nl, y_nl = make_classification(n_samples=500, n_features=20, n_informative=5,
                                   n_redundant=3, random_state=42)

datasets = {
    "Breast Cancer (30 features, 569 rows)"   : (X_c,  y_c),
    "Synthetic Non-linear (20 features, 500 rows)": (X_nl, y_nl),
}

algorithms = [
    ("Logistic Regression",    Pipeline([("s", StandardScaler()), ("m", LogisticRegression(max_iter=1000, random_state=42))])),
    ("Decision Tree",          Pipeline([("s", StandardScaler()), ("m", DecisionTreeClassifier(max_depth=5, random_state=42))])),
    ("Random Forest",          Pipeline([("s", StandardScaler()), ("m", RandomForestClassifier(n_estimators=100, random_state=42))])),
    ("Gradient Boosting",      Pipeline([("s", StandardScaler()), ("m", GradientBoostingClassifier(n_estimators=100, random_state=42))])),
    ("KNN (K=7)",              Pipeline([("s", StandardScaler()), ("m", KNeighborsClassifier(n_neighbors=7))])),
    ("SVM (RBF)",              Pipeline([("s", StandardScaler()), ("m", SVC(kernel="rbf", C=1.0, probability=True))])),
]

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
results_all = {}

print(f"{'Algorithm':<25}", end="")
for ds_name in datasets:
    short_name = ds_name.split("(")[0].strip()[:20]
    print(f"  {short_name:>20}", end="")
print()
print("-" * 75)

for alg_name, pipeline in algorithms:
    row = {"Algorithm": alg_name}
    print(f"{alg_name:<25}", end="")

    for ds_name, (X, y) in datasets.items():
        start = time.time()
        scores = cross_val_score(pipeline, X, y, cv=cv, scoring="roc_auc")
        elapsed = time.time() - start
        mean_auc = scores.mean()
        row[ds_name] = mean_auc
        print(f"  {mean_auc:>20.3f}", end="")

    results_all[alg_name] = row
    print()

print("\\n(All values are 5-fold CV AUC-ROC)")
"""),

code("""# ── Visualise the comparison ──────────────────────────────────────────────────

results_df = pd.DataFrame(results_all).T
results_df = results_df.drop(columns=["Algorithm"])
results_df = results_df.astype(float)

fig, ax = plt.subplots(figsize=(12, 5))
x = np.arange(len(algorithms))
width = 0.35
ds_names_short = ["Breast Cancer", "Synthetic Non-linear"]
colors_bar = ["#4C72B0", "#DD8452"]

for i, (ds_long_name, color) in enumerate(zip(list(datasets.keys()), colors_bar)):
    vals = [results_all[alg][ds_long_name] for alg, _ in algorithms]
    bars = ax.bar(x + i*width - width/2, vals, width-0.05, label=ds_names_short[i],
                   color=color, edgecolor="white", alpha=0.85)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.003,
                f"{val:.3f}", ha="center", va="bottom", fontsize=7.5)

ax.set_xticks(x)
ax.set_xticklabels([a for a,_ in algorithms], rotation=25, ha="right")
ax.set_ylabel("AUC-ROC (5-fold CV)"); ax.set_ylim(0.85, 1.02)
ax.set_title("Algorithm Comparison — AUC-ROC Across Two Datasets")
ax.legend(); ax.grid(alpha=0.3, axis="y")
plt.tight_layout(); plt.show()
"""),

md("## 3. Training Time vs Performance Tradeoff"),
code("""# ── Time each algorithm ───────────────────────────────────────────────────────

timing_results = []
X_time = X_c; y_time = y_c
sc_t = StandardScaler()
X_time_s = sc_t.fit_transform(X_time)

timing_algs = [
    ("Logistic Regression", LogisticRegression(max_iter=1000, random_state=42)),
    ("Decision Tree",       DecisionTreeClassifier(max_depth=5, random_state=42)),
    ("Random Forest",       RandomForestClassifier(n_estimators=100, random_state=42)),
    ("Gradient Boosting",   GradientBoostingClassifier(n_estimators=100, random_state=42)),
    ("KNN",                 KNeighborsClassifier(n_neighbors=7)),
    ("SVM (RBF)",           SVC(kernel="rbf", C=1.0, probability=True)),
]

for name, alg in timing_algs:
    t_start = time.time()
    alg.fit(X_time_s, y_time)
    train_time = time.time() - t_start

    t_start = time.time()
    alg.predict(X_time_s[:100])
    pred_time = time.time() - t_start

    auc = cross_val_score(alg, X_time_s, y_time, cv=3, scoring="roc_auc").mean()
    timing_results.append({"Algorithm": name, "Train (s)": round(train_time, 3),
                             "Predict (ms)": round(pred_time*1000, 2), "AUC": round(auc, 3)})

timing_df = pd.DataFrame(timing_results)
print("Training Time vs Performance (Breast Cancer Dataset):")
print(timing_df.to_string(index=False))
"""),

md("## 4. Bridge to Deep Learning\n\nAll classical ML algorithms you have learned are still used — but they have limitations that motivated the development of neural networks."),
code("""# ── Where classical ML hits its limits ────────────────────────────────────────

print("How Traditional ML Concepts Extend into Deep Learning")
print("=" * 65)

bridges = [
    {
        "Classical concept"   : "Linear regression",
        "Deep learning form"  : "A single neuron with no activation function",
        "Key difference"      : "Neural networks stack thousands of these",
    },
    {
        "Classical concept"   : "Logistic regression",
        "Deep learning form"  : "A single neuron with sigmoid activation",
        "Key difference"      : "NNs compose many of these into layers",
    },
    {
        "Classical concept"   : "Decision tree splitting (information gain)",
        "Deep learning form"  : "Attention mechanisms choose what to focus on",
        "Key difference"      : "Attention is differentiable; trees are not",
    },
    {
        "Classical concept"   : "Gradient descent",
        "Deep learning form"  : "Identical — used to train every neural network",
        "Key difference"      : "Scale: millions of parameters vs dozens",
    },
    {
        "Classical concept"   : "Regularisation (L1/L2)",
        "Deep learning form"  : "Dropout, weight decay, batch normalisation",
        "Key difference"      : "DL needs more regularisation due to capacity",
    },
    {
        "Classical concept"   : "Feature engineering",
        "Deep learning form"  : "Learnt automatically by early network layers",
        "Key difference"      : "DL removes the need for manual features on raw data",
    },
    {
        "Classical concept"   : "Kernel trick (SVM)",
        "Deep learning form"  : "Hidden layers — implicit non-linear transformation",
        "Key difference"      : "Kernels are fixed; hidden layers are learned",
    },
]

for b in bridges:
    print(f"\\nClassical : {b['Classical concept']}")
    print(f"DL form   : {b['Deep learning form']}")
    print(f"Difference: {b['Key difference']}")
"""),

code("""# ── When to use classical ML vs deep learning ─────────────────────────────────

comparison_table = [
    ("Tabular/structured data",      "Classical ML wins",     "Tree models often beat NNs on tables"),
    ("Images",                       "Deep Learning wins",    "CNNs learn spatial features automatically"),
    ("Natural language",             "Deep Learning wins",    "Transformers capture long-range context"),
    ("Audio / speech",               "Deep Learning wins",    "CNNs / RNNs handle sequential structure"),
    ("Small dataset (<10K)",         "Classical ML safer",    "DL overfits without enough data"),
    ("Large dataset (>100K)",        "Deep Learning can win", "NNs benefit most from scale"),
    ("Need interpretability",        "Classical ML",          "Linear/tree models are explainable"),
    ("Production latency <1ms",      "Classical ML",          "Simple models infer faster"),
    ("No GPU available",             "Classical ML",          "DL training is compute-intensive"),
]

print(f"{'Scenario':<35} | {'Recommendation':<25} | Reason")
print("-" * 90)
for scenario, rec, reason in comparison_table:
    print(f"{scenario:<35} | {rec:<25} | {reason}")
"""),

md("## 5. Your Algorithm Selection Checklist"),
code("""# ── The complete selection workflow ───────────────────────────────────────────

workflow = [
    ("Step 1", "Define the output type",
     "Continuous → regression. Binary → binary classification. Multiple classes → multiclass."),
    ("Step 2", "Check dataset size",
     "< 1K: KNN, SVM, LR. 1K-100K: Random Forest / Gradient Boosting. > 100K: add DL to the list."),
    ("Step 3", "Check interpretability requirement",
     "Legal/compliance constraints? → LR or Decision Tree."),
    ("Step 4", "Assess data complexity",
     "Non-linear boundaries? → SVM (RBF) or Random Forest."),
    ("Step 5", "Consider training/prediction time",
     "Real-time needs? → Logistic Regression or KNN."),
]

print("Algorithm Selection Checklist")
print("=" * 65)
for step, description, advice in workflow:
    print(f"\\n{step}: {description}")
    print(f"   Advice: {advice}")
"""),

md("""## Exercises

1. **Benchmark test**: Load the `load_diabetes` dataset (regression). Compare Linear Regression, Ridge, and Random Forest. Which achieves the lowest Mean Squared Error?

2. **Speed vs Accuracy**: Use `make_classification` to create a large dataset (e.g. 50,000 rows). Compare the training time of a Logistic Regression vs a Support Vector Machine (RBF). Does the extra time for SVM pay off in accuracy?

3. **Interpretability trade-off**: Train a Random Forest on the breast cancer dataset. Identify the top 3 features. Now train a Logistic Regression and interpret the coefficients for those same 3 features. Do they agree on what makes a tumour malignant?

4. **Neural Network intro**: Take the logistic regression code from Lesson 3.1 and "stack" it — if you had two of these functions where the output of the first was the input to the second, what would you have created?

---

## Summary

| Factor | Preferred Algorithm | Why? |
|---|---|---|
| **Speed** | Logistic Regression / KNN | Simple math, fast prediction |
| **Accuracy** | Gradient Boosting / SVM (RBF) | Handles complex non-linear boundaries |
| **Interpretability** | Decision Tree / Logistic Regression | You can see the 'why' behind each guess |
| **Small Data** | SVM / Naive Bayes | Geometric or probabilistic priors help |
| **Large Data** | Random Forest / XGBoost | Parallelisable and handles scale well |

**Congratulations! You have completed Course 3: Foundational ML Algorithms.**
""")
])

print("\\nCourse 3 notebooks generated successfully.")
