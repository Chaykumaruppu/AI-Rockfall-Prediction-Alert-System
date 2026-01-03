<div align="center">

<h1 style="font-size:38px; font-weight:700;">
🪨 AI-Based Rockfall Prediction & Alert System
</h1>

<p style="font-size:18px; max-width:900px;">
An end-to-end <b>temporal deep learning framework</b> for real-time rockfall risk prediction, dynamic alerting, and decision support in open-pit mining environments.
</p>

<p>
<b>IEEE Research Project · Temporal AI · Safety-Critical Systems</b>
</p>

</div>

<hr/>

## 🚀 Project Overview

Rockfalls and slope instabilities are among the most dangerous hazards in open-pit mining, often leading to severe accidents, equipment damage, and operational shutdowns.  
Most existing monitoring systems rely on **static thresholds**, **manual inspection**, or **snapshot-based models**, making them ineffective for detecting **gradual and evolving instability patterns**.

This project introduces a **temporal deep learning–driven safety intelligence system** that continuously monitors mine conditions, predicts future risk states, and generates **reliable early warnings** using an integrated AI pipeline.

---

## 🎯 Key Contributions

<ul>
<li>📊 <b>Large-scale synthetic temporal dataset</b> modeling realistic open-pit mine behavior across multiple zones</li>
<li>🧠 <b>LSTM-based temporal risk prediction model</b> capturing long-term instability trends</li>
<li>⚖️ <b>Dynamic risk scoring and persistence-aware alert logic</b> to reduce false alarms</li>
<li>📈 <b>Interactive real-time dashboard</b> for operational decision support</li>
<li>📄 <b>IEEE-style research paper</b> with quantitative validation against classical baselines</li>
</ul>

---

## 🏗️ System Architecture

<b>End-to-End Pipeline:</b>
Sensor Data → Time Windowing → LSTM Model → Risk Scoring Engine
        → Thresholding & Persistence Logic → Alerts → Dashboard


The system is designed to be **modular, explainable, and deployable** in real-world mining environments.

---

## 📊 Dataset Design

- **Type:** Synthetic temporal dataset
- **Samples:** 50,000+ time-indexed records
- **Zones:** 5 independent mine zones
- **Sampling:** Continuous monitoring simulation

### Monitored Features
- Surface displacement  
- Internal strain  
- Pore water pressure  
- Micro-seismic vibration  
- Rainfall intensity  
- Ambient temperature  

### Target Variable
- Continuous **Risk Index ∈ [0,1]**
- Smooth transitions between:
  - Normal
  - Stressed
  - Critical states

---

## 🧠 Model Details

### Proposed Model
- **Architecture:** LSTM → Dense Output
- **Input:** Sliding temporal windows (30 timesteps)
- **Loss:** Mean Squared Error (MSE)
- **Optimizer:** Adam
- **Regularization:** Early stopping

### Baseline Models
| Model | MAE ↓ | RMSE ↓ |
|------|------|-------|
| Linear Regression | 0.0221 | 0.0278 |
| Random Forest | 0.0310 | 0.0389 |
| **LSTM (Proposed)** | **0.0190** | **0.0240** |

📌 Temporal modeling significantly outperforms static baselines.

---

## 🚨 Risk Scoring & Alert Logic

The system converts raw predictions into actionable safety states:

| State | Condition |
|-----|----------|
| 🟢 SAFE | Risk below baseline |
| 🟡 WATCH | Rising risk trend |
| 🔴 ALERT | Sustained high risk |

✔ Alerts are triggered **only when risk persists over time**, preventing noise-induced false alarms.

---

## 🖥️ Interactive Dashboard

The Gradio-based dashboard enables:
- Zone-wise monitoring
- Real-time risk visualization
- Rolling trend analysis
- Live alert status updates

Designed as a **Safety Command Center** for operators and engineers.

---

## 📂 Repository Structure

AI-Rockfall-Prediction-Alert-System/
│
├── app.py # Gradio dashboard application
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── data/
│ └── synthetic_rockfall_dataset.csv
│
├── notebooks/
│ └── Rockfall_Prediction.ipynb
│
├── IEEE Paper/
│ └── IEEE_Paper.pdf
│
└── presentation/
└── Project_Presentation.pdf


---

## 📄 Research Paper

A complete **IEEE conference-ready paper** is included, covering:
- Problem formulation
- Dataset design
- Methodology
- Experimental validation
- System deployment

📌 Suitable for academic review and technical evaluation.

---

## 🔮 Limitations & Future Work

- Incorporation of real sensor data
- Multi-horizon forecasting
- Transformer-based temporal models
- Edge deployment on mine-site hardware
- Integration with geotechnical simulation tools

---

## 👤 Author

<b>Uppu Chaithanya Kumar</b>  
Department of Computer Science & Engineering  
Lovely Professional University  

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and build upon with attribution.

---

<div align="center">
<b>If this project helped you, consider starring ⭐ the repository.</b>
</div>




        

