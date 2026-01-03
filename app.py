import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr

# ----------------------------
# Load Data
# ----------------------------
DATA_PATH = "data/synthetic_dataset.csv"
df = pd.read_csv(DATA_PATH)

# Ensure correct sorting
df = df.sort_values(by=["zone_id", "time_index"])

# ----------------------------
# Dashboard Logic
# ----------------------------
def dashboard(zone_id):
    zone_data = df[df["zone_id"] == zone_id].tail(100)

    rolling_risk = zone_data["rolling_risk"].iloc[-1]
    risk_level = zone_data["risk_level"].iloc[-1]
    alert_message = zone_data["alert_message"].iloc[-1]

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(zone_data["time_index"], zone_data["rolling_risk"], label="Rolling Risk")
    ax.axhline(
        zone_data["zone_baseline"].iloc[-1],
        linestyle="--",
        label="Zone Baseline"
    )

    ax.set_title(f"Zone {zone_id} – Risk Trend")
    ax.set_xlabel("Time")
    ax.set_ylabel("Risk Index")
    ax.legend()
    ax.grid(alpha=0.3)

    return round(rolling_risk, 3), risk_level, alert_message, fig


# ----------------------------
# Custom CSS (Futuristic)
# ----------------------------
custom_css = """
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
h1, h2, h3 {
    color: #eaeaea;
}
"""

# ----------------------------
# Gradio UI
# ----------------------------
with gr.Blocks(css=custom_css, title="AI-Based Rockfall Prediction & Alert System") as demo:

    gr.Markdown("""
    # 🪨 AI-Based Rockfall Prediction & Alert System  
    ### Intelligent real-time risk monitoring for open-pit mines
    ---
    """)

    with gr.Row():
        zone_selector = gr.Dropdown(
            choices=[0, 1, 2, 3, 4],
            value=0,
            label="🗺️ Select Mine Zone"
        )

    with gr.Row():
        rolling_risk_out = gr.Number(
            label="📈 Current Rolling Risk",
            interactive=False
        )
        risk_level_out = gr.Textbox(
            label="🚦 Risk Level",
            interactive=False
        )

    alert_out = gr.Textbox(
        label="⚠️ Alert Status",
        interactive=False
    )

    gr.Markdown("### 📊 Recent Risk Trend")

    plot_out = gr.Plot()

    zone_selector.change(
        fn=dashboard,
        inputs=zone_selector,
        outputs=[
            rolling_risk_out,
            risk_level_out,
            alert_out,
            plot_out
        ]
    )

demo.launch()
