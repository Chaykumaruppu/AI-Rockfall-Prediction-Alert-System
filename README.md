# AI-Based Rockfall Prediction & Alert System

An end-to-end **temporal deep learning framework** for real-time rockfall risk prediction and alerting in open-pit mines.

## 🔍 Problem Motivation
Rockfall incidents in open-pit mines pose severe safety risks. Traditional monitoring systems rely on static thresholds and manual inspection, failing to capture the **temporal evolution of slope instability**.

## 🧠 Proposed Solution
This project introduces a **temporal LSTM-based risk prediction system** that:
- Models continuous risk evolution
- Generates dynamic risk scores
- Triggers SAFE / WATCH / ALERT states
- Visualizes results through an interactive dashboard

## 🗂 Dataset
- Large-scale **synthetic temporal dataset**
- 50,000+ time-indexed samples
- 5 mine zones with distinct behavioral characteristics
- Multi-sensor inputs (displacement, strain, vibration, rainfall, etc.)

## 🏗 System Architecture
1. Continuous sensor data ingestion  
2. Sliding-window temporal sequence generation  
3. LSTM-based risk prediction  
4. Dynamic risk scoring & persistence-based alerts  
5. Real-time visualization via Gradio dashboard  

## 📊 Model Performance
| Model | MAE ↓ | RMSE ↓ |
|------|------|------|
| Linear Regression | 0.0221 | 0.0278 |
| Random Forest | 0.0310 | 0.0389 |
| **LSTM (Proposed)** | **0.0190** | **0.0240** |

## 🖥 Interactive Dashboard
The Gradio-based dashboard enables:
- Zone-wise monitoring
- Temporal risk visualization
- Real-time alert interpretation

*(Screenshot in `/assets`)*

## 📄 Research Paper
- IEEE conference-ready paper included  
- Covers dataset design, methodology, evaluation, and deployment

## 🚀 How to Run
```bash
pip install -r requirements.txt
python app.py
