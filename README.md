# 📊 Expected Value

> A Python-based educational tool for descriptive statistics — calculate **mean**, **variance**, and **standard deviation** with interactive input and rich visualizations.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/license-Educational-green.svg" alt="License">
  <img src="https://img.shields.io/badge/status-active-success.svg" alt="Status">
</p>

---

## �‌ Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Example Output](#-example-output)
- [Roadmap](#-roadmap)
- [Author](#-author)
- [License](#-license)

---

## 🔎 Overview

**Expected Value** is a simple, interactive command-line tool that helps students and
beginners understand core concepts of descriptive statistics — *expected value*,
*variance*, *standard deviation*, and *sampling behavior* — through hands-on input
and visualization.

---

## ✨ Features

- **Statistics**
  - Mean
  - Variance
  - Standard Deviation
- **Flexible data input**
  - Manual entry from the keyboard
  - Load from a `data.txt` file
  - Built-in default dataset
- **Visualizations**
  - Histogram of the input data
  - Normally distributed sample based on the dataset's mean & std
  - Sample means plot via bootstrap-style resampling
- **Quality of life**
  - Colored terminal output with `colorama`
  - Graceful error handling with automatic fallback to default data

---

## 🛠 Tech Stack

| Component   | Purpose                          |
|-------------|----------------------------------|
| Python 3    | Core language                    |
| NumPy       | Numerical computation            |
| Matplotlib  | Plotting & visualization         |
| Colorama    | Cross-platform colored output    |
| os / platform | Terminal & OS handling         |

---

## 📁 Project Structure
```text
Expected-value/
├── Expected-value.py   # Main script
├── data.txt            # Optional input dataset
└── README.md           # Documentation

---

## ⚙️ Installation

Clone the repository:

bash
git clone https://github.com/Abolfazlilka/Expected-value.git
cd Expected-value

Install the required libraries:

bash
pip install numpy matplotlib colorama

---

## ▶️ Usage

Run the script:

bash
python Expected-value.py

Then follow the interactive prompts in the terminal.

---

## 🧠 How It Works

On launch, the program asks you to choose an input method:

1. **Manual input** — enter values one by one from the keyboard.
2. **Text file input** — load values from `data.txt`.
3. **Default data** — use the predefined built-in dataset.

After the data is loaded, it computes the **mean**, **variance**, and
**standard deviation**, then lets you optionally:

- Draw a **histogram** of the original data
- Generate a **normal sample** based on the data's mean and std
- Draw a **sample means plot** using bootstrap-style resampling

---

## 📤 Example Output

text
Data Summary:
  Mean:               78.54
  Variance:           33.12
  Standard Deviation:  5.75

Available plots:

- Histogram of the original dataset
- Histogram of generated normal data
- Sample means distribution plot

---

## 🚀 Roadmap

- [ ] CSV file input support
- [ ] Improved plot styling and labeling
- [ ] Median, mode, and additional descriptive statistics
- [ ] GUI version
- [ ] Unit tests
- [ ] Refactor into functions and modules

---

## 👤 Author

**Abolfazl Ilka**

---

## 📄 License

This project is open source and free for **educational and personal use**.
`
دم.
- بخش‌ها را با جداکننده (`---`) و آیکون مرتب کردم و Roadmap را به‌صورت checklist درآوردم.

اگر بخواهی می‌تونم نسخه‌ی کاملاً انگلیسی بدون ایموجی (مناسب محیط‌های رسمی‌تر) یا یک نسخه‌ی دوزبانه فارسی/انگلیسی هم برات بسازم.
