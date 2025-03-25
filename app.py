# app.py

import streamlit as st
import backend
import os
import numpy as np
import pandas as pd
import io
from streamlit_modal import Modal  # Import streamlit-modal for pop-up functionality

# Initialize modal for introduction
modal = Modal(key="Demo Key", title="Welcome to Datacynte")

# Constants
PLOTS_DIR = "/home/user/gen-ai/plots"

# Ensure plots directory exists
if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)

# Set page config
st.set_page_config(
    page_title="Datacynte",
    page_icon="🌟",  # A star emoji for that spark of insight
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "data" not in st.session_state:
    st.session_state.data = None
if "query_counter" not in st.session_state:
    st.session_state.query_counter = 0
if "data_updated" not in st.session_state:
    st.session_state.data_updated = False  # Flag to track if data has been modified
if "first_load" not in st.session_state:
    st.session_state.first_load = True  # Flag to track if this is the first load

# Sidebar configuration
with st.sidebar:
    st.header("🔑 Configuration")

    gemini_api_key = st.text_input("Gemini API Key", type="password", help="Required for AI functionality")
    astra_token = st.text_input("Astra DB Token (Optional)", type="password")
    astra_endpoint = st.text_input("Astra DB Endpoint (Optional)", type="password")

    store_history = st.checkbox("Store Chat History", value=bool(astra_token and astra_endpoint))

    uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

# Load dataset
if uploaded_file and st.session_state.data is None:
    try:
        st.session_state.data = backend.load_data(uploaded_file)
        if st.session_state.data is not None:
            st.success("✅ Dataset loaded successfully!")
        else:
            st.error("❌ Failed to load dataset. Please check the file format.")
    except Exception as e:
        st.error(f"❌ Error loading dataset: {str(e)}")

model, astra_client, db = backend.initialize_clients(
    gemini_api_key, astra_token, astra_endpoint if store_history else None
)

if db:
    backend.create_collection(db)

def cool_title(title_text):
    st.markdown(
        f"""
        <div style="background-color:#f63366;padding:10px;border-radius:10px;font-family: 'Times New Roman', Times, serif;">
        <h1 style="color:white;text-align:center;">{title_text}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main Chat Interface
cool_title("🌟 Datacynte")
st.markdown('<h3 style="text-align: center; font-size: 20px;">A spark of genius—ignite your data with AI to uncover dazzling truths!</h3>', unsafe_allow_html=True)
# Show modal on first load
if st.session_state.first_load:
    with modal.container():
        st.markdown("""
        #### Ignite Your Data Journey
        From the faintest flicker of data comes a blaze of revelation. Datacynte is your spark of genius, fusing AI brilliance with analytical finesse to transform numbers into narratives. Every query fans the flame of discovery, lighting up the unseen.

        #### What Fuels Datacynte’s Glow?
        - **AI Alchemy**: Driven by the Gemini API (key required), it forges precise Python code to answer your call.
        - **Vector Vault**: Add an Astra DB token and endpoint, and your insights are stored in a vector database—a timeless ember of knowledge.
        - **Seamless Spark**: Upload your CSV, ask boldly, and refine your data with a flicker of ease.

        *“From faint traces to dazzling truths—Datacynte sparks the way.”*
        """)
    st.session_state.first_load = False  # Set to False after showing the modal

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "plot_path" in message and os.path.exists(message["plot_path"]):
            st.image(message["plot_path"], use_container_width=True)

# Chat input
query = st.chat_input("Ask Datacynte a data question (e.g., 'find the max of 12percentage' or 'plot Salary trends')...")

if query and st.session_state.data is not None:
    with st.spinner("🌟 Datacynte is sparking..."):
        try:
            st.session_state.query_counter += 1

            # Define plot path for this query
            plot_filename = f"plot_{st.session_state.query_counter}.png"
            plot_path = os.path.join(PLOTS_DIR, plot_filename)

            # Display user message in chat
            with st.chat_message("user"):
                st.markdown(query)

            st.session_state.messages.append({"role": "user", "content": query})

            # Initialize AI clients
            model, astra_client, db = backend.initialize_clients(
                gemini_api_key, astra_token, astra_endpoint if store_history else None
            )
            if model is None:
                raise ValueError("Failed to initialize AI model. Check your Gemini API key.")

            # Generate AI code
            code, dependencies = backend.generate_code(model, query, st.session_state.data, plot_path)

            # Display AI-generated code in chat
            with st.chat_message("assistant"):
                st.markdown("🌟 **Datacynte’s Code:**")
                st.code(code, language="python")

            # Execute the generated code
            stdout, stderr = backend.execute_code(code, st.session_state.data, dependencies, plot_path)

            # Display execution results
            with st.chat_message("assistant"):
                if stderr:
                    st.error(f"❌ Execution Error:\n{stderr}")
                else:
                    st.markdown("✅ **Datacynte’s Output:**")
                    if stdout:
                        st.text(stdout)
                    else:
                        st.text("No output generated.")

                    # Check if the query involves plotting or preprocessing
                    is_plot_query = any(keyword in code.lower() for keyword in ["plt.", "matplotlib", "plotly", "px."])
                    is_preprocessing_query = any(keyword in code.lower() for keyword in ["fillna", "replace", "dropna", "impute"])

                    if is_plot_query and os.path.exists(plot_path) and os.path.getsize(plot_path) > 0:
                        st.image(plot_path, use_container_width=True)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": "✅ Datacynte completed with a plot.",
                            "plot_path": plot_path
                        })
                    else:
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": f"✅ Datacynte completed.\n```\n{stdout}\n```" if stdout else "✅ Datacynte completed with no output."
                        })

                    # If preprocessing occurred, update the dataset and set the flag
                    if is_preprocessing_query:
                        exec(code, {"data": st.session_state.data, "pd": pd, "np": np})
                        st.session_state.data_updated = True
                        st.success("✅ Dataset updated with preprocessing!")

            # Store in Astra (if enabled)
            if store_history and db:
                backend.store_in_astra(db, query, code, stdout)

        except ValueError as ve:
            st.error(f"❌ Value Error: {str(ve)}")
        except Exception as e:
            st.error(f"❌ Unexpected Error: {str(e)}")

    # Add download button if dataset has been updated
    if st.session_state.data_updated:
        csv_buffer = io.StringIO()
        st.session_state.data.to_csv(csv_buffer, index=False)
        csv_data = csv_buffer.getvalue()
        csv_buffer.close()

        st.download_button(
            label="📥 Download Updated Dataset",
            data=csv_data,
            file_name="updated_dataset.csv",
            mime="text/csv",
        )

elif query and st.session_state.data is None:
    st.error("❌ Please upload a dataset before asking questions.")
