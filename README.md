# Datacynte-AI Powered Data Analytics Platform

# 📊 **Datacynte: AI-Powered Data Analysis and Analytics Platform**

**Datacynte** is an intelligent platform designed to simplify and enhance **data analysis** and **data analytics** workflows. By combining **Google Gemini AI** with **Astra DB** integration, Datacynte empowers users to perform complex data operations, generate insightful visualizations, and automate data preprocessing through natural language queries.

---

## 🚀 **Key Features**

- ✅ **AI-Powered Data Analysis:**  
   - Leverages **Google Gemini AI** to generate Python code for performing data analysis, statistics, and visualization.  
   - Supports queries related to **data exploration**, **cleaning**, and **statistical analysis**.  

- ✅ **Data Visualization and Insights:**  
   - Automatically generates visualizations using **Matplotlib** and **Plotly**.  
   - Displays interactive plots and statistical summaries.  

- ✅ **Data Preprocessing and Cleaning:**  
   - Supports operations such as handling missing values, data transformation, and outlier detection.  
   - Allows users to update and download the modified dataset.  

- ✅ **Astra DB Integration (Optional):**  
   - Stores query history, generated code, and results in **Astra DB** for future reference.  
   - Enables retrieval and review of previous analyses.  

- ✅ **User-Friendly Interface:**  
   - Interactive **Streamlit** interface with a chat-based workflow.  
   - Upload CSV datasets and perform data analysis through natural language queries.  

---

## 🛠️ **Tech Stack**

- **Frontend:**  
    - [Streamlit](https://streamlit.io) – Interactive web application for data exploration.  
- **Backend:**  
    - **Google Gemini AI** – AI-powered code generation for data analysis.  
    - **Astra DB** – (Optional) Vector database for storing query history.  
- **Environment:**  
    - Python environment with automatic dependency management.  

---

## 📂 **Project Structure**

├── backend.py # Backend logic: AI code generation, DB interactions, and execution
├── app.py # Streamlit app with chat-based data exploration
├── requirements.txt # List of dependencies
├── README.md # Project documentation
├── /plots # Directory for storing generated visualizations
