import streamlit as st
import requests

API_URL = "https://prompt-rewriter-cloudflare.vullagantiramakrishna.workers.dev"

st.set_page_config(page_title="Prompt Rewriter", page_icon="✍️")

st.title("✍️ Prompt Rewriter AI")
st.write("Rewrite prompts for clarity while preserving intent.")

prompt = st.text_area(
    "Enter your prompt",
    placeholder="e.g. ai agents are confusing",
    height=150
)

if st.button("Rewrite"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Rewriting..."):
            response = requests.post(
                API_URL,
                json={"prompt": prompt},
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                st.subheader("Rewritten Prompt")
                st.success(data["rewritten_prompt"])
            else:
                st.error(f"Error {response.status_code}: {response.text}")
