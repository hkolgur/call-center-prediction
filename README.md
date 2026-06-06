# Call Center Analytics: Hourly Call Volume Prediction

## 📋 Sprint Story Context
**Jira Ticket:** ETCC-402  
**Epic:** Call Center Capacity Planning  
**Story Description:** As a workforce management analyst, I need to understand the probability distribution of incoming customer service calls so that we can optimize staffing levels and minimize customer wait times.

### Problem Statement
Historical data establishes that call volume follows a **Poisson distribution** with an average ($\mu$) of **5 calls per hour**. We must evaluate the mathematical likelihood of receiving **exactly 3 calls** in any given hour to stress-test low-volume staffing baselines.

---

## 🚀 Environment Setup
This project uses `uv` to manage isolated Python virtual environments and dependencies.

### Prerequisites
Ensure you have [uv](https://astral.sh) installed on your Mac. If you do not have it, install it via Homebrew:
```bash
brew install uv
```

### Installation
1. Clone the repository:
   ```bash
   git clone repo link
   cd call-center-prediction
   ```
2. **Sync the environment:**
   This command automatically creates a virtual environment (`.venv`) and installs all necessary project dependencies using `uv`.
   ```bash
   uv sync
   ```
---

## 📈 Analysis & Output
Run the evaluation suite within your managed environment using:

```bash
uv run python poisson_analysis.py
```

### Key Metrics Deliverable
* **Calculated Probability ($k=3, \mu=5$):** `0.1404` (~14.04%)
* **Interpretation:** There is a 14.04% chance that the center will receive exactly 3 calls in the next hour. This dictates that while 5 is the average, the workforce team must still plan for significant variance.

### Visual Artifacts
The script automatically exports an analytics graphic (`call_volume_distribution.png`) showcasing the Probability Mass Function (PMF) and Cumulative Distribution Function (CDF) to assist stakeholders in visualizing operational thresholds.
