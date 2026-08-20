# 🤖 CodeSense AI

CodeSense AI is a Python-based code analysis tool built with **Streamlit**. It helps users identify Python errors and understand what went wrong through simple error explanations.

## 🚀 Features

* 🔍 Analyze Python code
* 🐛 Detect common Python errors
* 💡 Explain errors in simple language
* 📝 Show error type and details
* ⚡ Fast and easy-to-use Streamlit interface
* 🎯 Beginner-friendly debugging assistance

## 🖥️ Demo

Run the application locally and open it in your browser.

```bash
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## 📂 Project Structure

```text
codesense-ai/
│
├── app.py
├── error_engine.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shivenchaware995-spec/codesense-ai.git
```

### 2. Open the project folder

```bash
cd codesense-ai
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run CodeSense AI

```bash
python -m streamlit run app.py
```

## 🧪 Example

Input:

```python
numbers = [10, 20, 30]
print(numbers[5])
```

CodeSense AI identifies the problem as an:

```text
IndexError
```

It explains that the list contains only indexes `0`, `1`, and `2`, while index `5` does not exist.

## 🎯 Purpose

The goal of CodeSense AI is to make Python debugging easier for beginners by turning complicated error messages into simple explanations.

## 👨‍💻 Author

**Shiven Chaware**

GitHub: https://github.com/shivenchaware995-spec
