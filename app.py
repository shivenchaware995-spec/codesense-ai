import streamlit as st

from error_engine import run_code, explain_error


st.set_page_config(
    page_title="CodeSense AI",
    page_icon="🐍",
    layout="wide"
)


st.title("🐍 CodeSense AI")
st.subheader("Beginner-Friendly Python Error Explainer")

st.write(
    "Write Python code below. CodeSense AI will run it, "
    "detect errors and explain them in simple language."
)


default_code = """numbers = [10, 20, 30]

print(numbers[5])
"""


code = st.text_area(
    "💻 Enter Python Code",
    value=default_code,
    height=250
)


if st.button("🔍 Analyze Code", use_container_width=True):

    if not code.strip():
        st.warning("Please enter some Python code.")
    else:

        result = run_code(code)

        if result["success"]:

            st.success("✅ Code executed successfully!")

        else:

            error = result["error"]

            explanation = explain_error(error)

            st.error(
                f"❌ {explanation['type']}: "
                f"{explanation['message']}"
            )

            st.markdown("### 🧠 What happened?")

            st.info(explanation["meaning"])

            st.markdown("### 💡 How to fix it")

            st.warning(explanation["fix"])

            st.markdown("### ✅ Example")

            st.code(
                explanation["example"],
                language="python"
            )

            st.markdown("### 🔎 Error Type")

            st.write(explanation["type"])

            st.markdown("### 📋 Your Code")

            st.code(code, language="python")