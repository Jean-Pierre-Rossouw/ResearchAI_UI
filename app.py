import streamlit as st
from streamlit_chat import message
from langserve import RemoteRunnable

# Configuration
st.set_page_config(
    page_title="Research Assistant",
    layout="wide",
)

# TODO: Setup LLM via RemoteRunnable

# Page Title
st.markdown(
    "<h1 style='text-align: center;'>Research Assistant</h1>", unsafe_allow_html=True
)

# Initialise sessions state if needed
if "report" not in st.session_state:
    st.session_state["report"] = []


# Helper functions
def export_report():
    # TODO: Export report to file
    pass


def clear_report():
    st.session_state["report"] = []
    st.session_state["Input"] = ""


# Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Options</h2>", unsafe_allow_html=True)
    st.button("Export Report", on_click=export_report)
    st.button("Clear Report", on_click=clear_report)

# Main input and report display
if prompt := st.text_input("Enter research question...", key="Input"):
    with st.spinner("Generating research report..."):
        try:
            report = "Generated report"
            st.session_state["report"].append(report)
        except Exception as e:
            st.error(f"Error generating report: {e}")

    if len(st.session_state["report"]) > 0:
        st.markdown(st.session_state["report"][-1], unsafe_allow_html=True)
    else:
        st.markdown("No report generated yet.")
