# Flask Answers

A structured collection of answers, solutions, and reference implementations for a **6-hour Flask curriculum**. It contains **360 theory answers** and **90 practical coding solutions**, progressing from Flask fundamentals all the way to a fully-featured real-world market application.

## Contents at a Glance

| Section | Items | Location | Index |
| :--- | :---: | :--- | :--- |
| Theory answers | 360 | [`theory/`](theory/) | [`theory/hour_N.md`](theory/hour_1.md) |
| Practical solutions | 90 | [`practical/`](practical/) | [`practical/hour_N/README.md`](practical/hour_1/README.md) |

## Repository Structure

```
Flask_Answers/
├── README.md
├── theory/
│   ├── hour_1.md              # Hour 1 catalog (index of 60 answers)
│   ├── hour_1/                # 60 standalone theory answers (q01 ... q60)
│   ├── hour_2.md
│   ├── hour_2/
│   ├── ...
│   └── hour_6/
└── practical/
    ├── hour_1/
    │   ├── README.md          # Hour 1 solution catalog
    │   └── task_01_*.py ... task_15_*.py
    ├── hour_2/
    ├── ...
    └── hour_6/
```

- Each **theory answer** is a standalone Markdown file named `q##_<slug>.md` and is listed in its hour's catalog (`theory/hour_N.md`).
- Each **practical solution** is a runnable Python file named `task_##_<slug>.py` and is listed in its hour's catalog (`practical/hour_N/README.md`).

## Curriculum Overview

| Hour | Topic | Theory | Practical | Tier |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Flask fundamentals: app setup, routing, templates, Jinja | [Catalog](theory/hour_1.md) | [Catalog](practical/hour_1/README.md) | Beginner |
| 2 | Templates & databases: inheritance, `url_for`, SQLAlchemy ORM | [Catalog](theory/hour_2.md) | [Catalog](practical/hour_2/README.md) | Elementary |
| 3 | App structure & relationships: packages, circular imports, model relations | [Catalog](theory/hour_3.md) | [Catalog](practical/hour_3/README.md) | Intermediate |
| 4 | Forms & validation: WTForms, CSRF, validators, flash messages | [Catalog](theory/hour_4.md) | [Catalog](practical/hour_4/README.md) | Advanced |
| 5 | Authentication & security: bcrypt hashing, login manager, sessions | [Catalog](theory/hour_5.md) | [Catalog](practical/hour_5/README.md) | Advanced |
| 6 | Real-world market app: buying/selling items, modals, forms | [Catalog](theory/hour_6.md) | [Catalog](practical/hour_6/README.md) | Expert |

## How to Use

1. **Study the theory** – open an hour catalog (e.g. [`theory/hour_4.md`](theory/hour_4.md)) and jump into any individual answer.
2. **Practice the code** – open the matching practical catalog for runnable solutions.
3. **Run a solution** – each practical file is self-contained and prints a pass message when its assertions succeed:

```bash
python practical/hour_1/task_01_app_initialization.py
```

## Requirements

The practical solutions use the following packages:

```bash
pip install flask flask-wtf wtforms flask-sqlalchemy flask-bcrypt flask-login
```

| Package | Used In |
| :--- | :--- |
| `flask` | All hours |
| `flask-sqlalchemy` | Hours 2–6 |
| `wtforms` / `flask-wtf` | Hours 4, 6 |
| `flask-bcrypt` | Hour 5 |
| `flask-login` | Hours 5–6 |

## Notes

- Theory answers are presented in multiple formats (`Single-Word`, `Short-Answer`, `Code-Snippet`, `Multiple-Choice`) as noted in each catalog.
- Practical files are written as concise reference solutions and are intended for learning, not production use.
