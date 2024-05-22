<h1>VIX Tracking Fund Construction - Creating an Optimized ETF to track the VIX Index</h1>

<h2>Description</h2>

<h3>Project Overview:</h3>

<h4>Goal:</h4> To design a portfolio that closely tracks the performance of the VIX index, leveraging a variety of financial instruments such as ETFs, single stocks, and VIX futures, similar to how the VXX (managed by Barclays) operates.

<h3>Data Acquisition:</h3>

<h4>Sources:</h4> Utilized Yahoo Finance to gather daily Open-High-Low-Close (OHLC) data for both the VIX index and the SPY (S&P 500 ETF), for understanding market and volatility.

<h4>Adjustments:</h4> Distinguished between closing prices and adjusted closing prices, the latter of which accounts for dividends, stock splits, etc., offering a truer reflection of stock value over time.

<h3>Data Cleaning:</h3>

<h4>Missing Values:</h4> Implemented forward filling or interpolation strategies to address gaps in the data, ensuring a complete dataset for accurate analysis.

<h4>Trading Days Alignment:</h4> Harmonized the trading days for VIX and SPY data to ensure consistency, essential for comparative analysis and modeling.

<h3>Initial Analysis:</h3>

<h4>Daily Returns Calculation:</h4> Determined daily returns using the formula
(Price at time t–Price at time t−1)/Price at time t−1, which is fundamental for calculating portfolio returns.

<h4>Sample Portfolio:</h4> Constructed a portfolio with 90% SPY and 10% VIX allocation. Evaluated its performance in terms of standard deviation and Sharpe Ratio, comparing it against SPY alone to assess outperformance.

<h3>In-depth VXX Analysis:</h3>

<h4>Objective:</h4> Conducted a thorough review of the VXX fund by Barclays to understand its structure, benefits, and limitations, informing the design of the new tracking fund.
     
<h3>Project Implementation Steps:</h3>

<h4>Benchmark Portfolio Management:</h4> The goal is to create a passive portfolio that accurately mirrors the VIX's movements, setting a benchmark for comparison.

<h4>Investable Universe Definition:</h4> Identified and select a subset of securities believed to exhibit strong correlations with the VIX (compute Pearson correlation coeZicients between daily returns of VIX and each of the selected securities and then assess statistical significance through hypothesis testing), including negative beta stocks (which move inversely to the market) and high volatility stocks.

<h4>Download Securities Data:</h4> Focused on specific securities such as PSQ, SH, CLX, TORM, AGBA, COMP, PIXY, VTYX, DG, GME, MCY, KR, VIX, which are selected based on their potential to track the VIX.

<h3>Data Analysis & Optimization:</h3>

Conducted comprehensive data analysis, including summary statistics, hypothesis testing, and exploratory analysis using techniques like clustering and principal components analysis.

Built correlation, covariance, and mean-variance correlation matrices to understand the relationships among the selected securities.

Formulated and solved a portfolio optimization problem using CVXPY, aiming to minimize the Daily Sum of Squared Errors between the portfolio and the VIX. This includes setting constraints for shorting and leveraging.

<h3>Future Considerations:</h3>

Explore strategies for model validation using in-sample (training) and out-of-sample (testing) data sets. Consider periodic model retraining and testing to adapt to market changes.

<h4>Advanced Data Analysis Techniques:</h4>

<h5>Machine Learning Models:</h5> Incorporate machine learning models to predict the VIX movements based on historical data and other market indicators. Techniques such as time series forecasting (ARIMA, LSTM networks) could provide insights into future volatility trends.

<h5>Sentiment Analysis:</h5> Utilize sentiment analysis on financial news and social media to gauge market sentiment, which could be a leading indicator of volatility. Integrating this data might improve the tracking fund’s responsiveness to market changes.

<h4>Portfolio Optimization Enhancements:</h4>

<h5>Dynamic Rebalancing:</h5> Implement a dynamic rebalancing strategy that adjusts the portfolio composition based on real-time market conditions rather than relying on a fixed allocation. This could involve setting thresholds for rebalancing based on volatility forecasts or market sentiment.

<h5>Alternative Optimization Criteria:</h5> Beyond minimizing the sum of squared errors, consider alternative optimization objectives such as maximizing the portfolio's Sharpe Ratio or minimizing maximum drawdown, which could oZer better risk-adjusted returns.

<h4>Risk Management:</h4>

<h5>Stress Testing:</h5> Conduct stress testing under various market scenarios (e.g., financial crises, rapid interest rate changes) to understand the portfolio's potential vulnerabilities and resilience against extreme market movements.

<h5>Liquidity Analysis:</h5> Assess the liquidity of the selected securities to ensure the portfolio can be adjusted quickly without significant market impact. This is crucial for dynamic rebalancing strategies.

<h4>Diversification Strategies:</h4>

<h5>Global Volatility Instruments:</h5> Explore incorporating volatility instruments from global markets to diversify exposure beyond the US market.

<h5>Derivatives and Structured Products:</h5> Consider the use of options, futures, and structured products to gain exposure to volatility in a more capital-eZicient manner. This includes exploring VIX options and futures for direct exposure.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>SQL</b>
- <b>Libraries: pandas, numpy, scikitlearn, seaborn, keras, tensorflow, pytorch</b>
- <b>Models: Multivariate Regression, Random Forest, XGBoost, Gradient Boosting, Neural Newtowrks (LSTM), Transformers</b>

<h2>Environments Used </h2>

- <b>Kaggle and Google Colab</b>

<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select the disk:  <br/>
<img src="https://i.imgur.com/tcTyMUE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
