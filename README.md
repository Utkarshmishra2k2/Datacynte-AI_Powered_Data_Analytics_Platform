# 📊 **Datacynte: AI-Powered Data Analytics Platform**

Datacynte is an intelligent platform designed to simplify and enhance **data analysis** and **data analytics** workflows. By integrating **Google Gemini AI** with **Astra DB**, Datacynte empowers users to perform complex data operations, generate insightful visualizations, and automate data preprocessing through natural language queries.

---

## 🚀 **Key Features**

### ✅ AI-Powered Data Analysis
- Leverages **Google Gemini AI** to generate Python code for data analysis, statistics, and visualization.
- Supports queries related to **data exploration**, **cleaning**, and **statistical analysis**.

### ✅ Data Visualization and Insights
- Automatically generates visualizations using **Matplotlib** and **Plotly**.
- Displays interactive plots and statistical summaries.

### ✅ Data Preprocessing and Cleaning
- Handles missing values, data transformation, and outlier detection.
- Allows users to update and download the modified dataset.

### ✅ Astra DB Integration (Optional)
- Stores query history, generated code, and results in **Astra DB** for future reference.
- Enables retrieval and review of previous analyses.

### ✅ User-Friendly Interface
- Interactive **Streamlit** interface with a chat-based workflow.
- Upload CSV datasets and perform data analysis through natural language queries.

---

## 🎥 **Application Walkthrough**
_A demonstration video showcasing the functionality and features of the application will be provided here soon._

[![Datacynte Walkthrough](https://github.com/user-attachments/assets/32cc44b6-021d-417a-8fcc-e9445b5aac14)](https://github.com/user-attachments/assets/32cc44b6-021d-417a-8fcc-e9445b5aac14)

---

## 🛠️ **Tech Stack**

### **Frontend:**
- [Streamlit] – Interactive web application for data exploration.

### **Backend:**
- **Google Gemini AI** – AI-powered code generation for data analysis.
- **Astra DB** – (Optional) Vector database for storing query history.

### **Environment:**
- Python environment with automatic dependency management.

---

## 📂 **Project Structure**

```
.   
├── backend.py        # Backend logic: AI code generation, DB interactions, and execution  
├── app.py           # Streamlit app with chat-based data exploration  
├── requirements.txt # List of dependencies  
├── README.md        # Project documentation  
├── /plots           # Directory for storing generated visualizations  
```

---

## 🚀 **Getting Started**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Utkarshmishra2k2/Datacynte-AI_Powered_Data_Analytics_Platform.git
cd Datacynte-AI_Powered_Data_Analytics_Platform
```

### 2️⃣ Install Dependencies
Install all required Python libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```

---

## 📊 **Data Storage in Astra DB**

If Astra DB integration is enabled:
- Queries, generated code, and execution outputs are stored in the `chat_sessions` collection.
- You can retrieve and review previous analyses for future reference.

---

## ✨ **Acknowledgments**
Developed by **Utkarsh Mishra**  
Powered by **Google Gemini AI, Astra DB, and Streamlit**

