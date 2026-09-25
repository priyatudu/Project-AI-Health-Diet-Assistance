**🩺 AI Health & Diet Assistance**

An AI-powered personal health and diet assistance application built with
**Python, LLM, RAG, and Streamlit**.

The application provides personalized health information based on user
details such as age, gender, height, weight, and activity level. It
calculates important health and energy-related metrics and provides
diet recommendations along with an AI-powered health assistance feature.

---

## Overview

The **AI Health & Diet Assistance** application combines traditional
health calculations with Generative AI and Retrieval-Augmented Generation
(RAG) to provide an interactive health and nutrition assistance experience.

Users provide basic information such as:

- Gender
- Age
- Weight
- Height
- Activity Level
- Health-related goals/preferences

The application then calculates health metrics such as **BMI, BMR,
TDEE, and estimated calorie requirements** and provides personalized
diet recommendations.

The application also includes an **AI Health Assistance** feature that
allows users to interact with an AI assistant for health-related
information.

---

## ✨ Key Features

### 📊 Health Information

The application calculates and displays:

- **BMI (Body Mass Index)**
- **BMR (Basal Metabolic Rate)**
- **TDEE (Total Daily Energy Expenditure)**
- **Estimated daily calorie requirement**

### 🥗 Diet Recommendation

Based on the user's profile and calculated energy requirements, the
application provides a personalized diet recommendation.

### 🤖 AI Health Assistance

Users can interact with an AI-powered health assistant to ask
health-related questions and receive context-aware responses.

### 🧠 RAG-Based Question Answering

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve
relevant information from the available knowledge base before generating
responses with an LLM.

### 🌐 Streamlit Interface

The application provides an interactive web interface built using
Streamlit.

---

## 🧠 How It Works

```text
User Information
       │
       ▼
Age / Gender / Height / Weight / Activity
       │
       ▼
Health Metric Calculation
       │
       ├── BMI
       ├── BMR
       ├── TDEE
       └── Calorie Requirement
       │
       ▼
Diet Recommendation
       │
       ▼
AI Health Assistance
       │
       ▼
RAG Retrieval
       │
       ▼
Relevant Context
       │
       ▼
LLM
       │
       ▼
AI-Generated Response
