# Market Efficiency and Liquidity Dynamics in Indian Equity Indices  
**A Multi-Frequency Analysis (jan 2016–Dec 2024)**  

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
**Authors**: Nischay Soni 
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
- **Dataset**: Preprocessed OHLC data for Nifty indices (jan 2016–Dec 2024).  

---

## 📥 Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/indian-market-efficiency.git  
   cd indian-market-efficiency  


##📊 Results
Index	Interval	VR(10)	Roll Spread (Daily)
Nifty50	Weekly	1.117	0.00
Nifty100	Daily	0.960	48.74
Nifty200	15-minute	1.066	3.17
Interpretation:

High-frequency spreads reflect microstructure noise.

Daily spreads during COVID-19 (e.g., Nifty100: 48.74) indicate liquidity shocks.

##📄 Related Paper
A detailed manuscript titled "Market Efficiency and Liquidity Dynamics in Indian Equity Indices: A Multi-Frequency Analysis" is under review and will be published soon. Key contributions include:

Critique of closing-price-based liquidity metrics.

Policy recommendations for improving data transparency in emerging markets.

Citation (to be updated post-publication):

##🤝 Contributing
Contributions are welcome! Open an issue or submit a PR for:

Alternative liquidity estimators (e.g., Corwin-Schultz).

Extensions to mid/small-cap indices.

##📜 License
This project is licensed under the MIT License. See LICENSE for details.

##🙏 Acknowledgments
Data sourced from NSE India.

Methodological guidance from Fama (1970) and Roll (1984).
