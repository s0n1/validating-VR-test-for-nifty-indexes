# Market Efficiency and Liquidity Dynamics in Indian Equity Indices  
**A Multi-Frequency Analysis (2016–2023)**  

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
**Authors**: [Your Name]  
**Paper Status**: *Preprint under review. Manuscript will be published soon.*  

---

## 📜 Overview  
This repository contains code and data for analyzing weak-form market efficiency and liquidity dynamics in India’s benchmark indices (**Nifty50, Nifty100, Nifty200**) across 15-minute, hourly, daily, and weekly intervals (2016–2023). The study employs:  
- **Variance Ratio (VR) Tests** to detect deviations from the random walk hypothesis.  
- **Roll Model** to estimate bid-ask spreads and assess liquidity anomalies.  

**Key Findings**:  
1. **Weak-form efficiency holds**: No statistically significant deviations (∣M(q)∣ < 1.96) across all indices and intervals.  
2. **Liquidity anomalies**: COVID-19-induced spreads invalidate the Roll model at daily frequencies.  
3. **Time horizon effects**: Momentum strengthens with holding periods (VR(q) ↑ with q), while short-term mean reversion lacks significance.  

---

## 🛠️ Features  
- **Multi-frequency analysis**: Code for 15-minute, hourly, daily, and weekly data.  
- **Statistical tests**:  
  - Lo-MacKinlay Variance Ratio test with heteroskedasticity-robust adjustments.  
  - Roll spread estimator with covariance checks.  
- **Visualization**: Interactive plots for VR trends, spread dynamics, and crisis periods (e.g., COVID-19).  
- **Dataset**: Preprocessed OHLC data for Nifty indices (2016–2023).  

---

## 📥 Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/indian-market-efficiency.git  
   cd indian-market-efficiency  
