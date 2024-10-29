# -*- coding: utf-8 -*-
"""VIX Tracking Fund Construction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f2hok3tlsNjjATJTcMKPVcprpwg-znAY

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a  href="#Data" data-toc-modified-id="Data-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Data</a></span><ul class="toc-item"><li><span><a href="#Yahoo!-Finance" data-toc-modified-id="Yahoo!-Finance-4.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Yahoo! Finance</a></span></li><li><span><a href="#S&amp;P-500-and-the-VIX" data-toc-modified-id="S&amp;P-500-and-the-VIX-4.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>S&amp;P 500 and the VIX</a></span><ul class="toc-item"><li><span><a href="#Prices-and-Returns-from-Yahoo!-Finance" data-toc-modified-id="Prices-and-Returns-from-Yahoo!-Finance-4.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Prices and Returns from Yahoo! Finance</a></span></li></ul></li><li><span><a href="#Tradeable-VIX-like-Products" data-toc-modified-id="Tradeable-VIX-like-Products-4.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Tradeable VIX-like Products</a></span></li><li><span><a href="#CBOE-Historical-Data" data-toc-modified-id="CBOE-Historical-Data-4.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span><a href="https://www.cboe.com/tradable_products/vix/vix_historical_data/" rel="nofollow" target="_blank">CBOE Historical Data</a></a></span></li></ul></li><li><span><a href="#Portfolio-Management-Relative-To-a-Benchmark" data-toc-modified-id="Portfolio-Management-Relative-To-a-Benchmark-5"><span class="toc-item-num">2&nbsp;&nbsp;</span>Portfolio Management Relative To a Benchmark</a></span><ul class="toc-item"><li><span><a href="#What's-the-Investable-Universe?" data-toc-modified-id="What's-the-Investable-Universe?-5.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>What's the Investable Universe?</a></span></li><li><span><a href="#Active-Management-Formulation" data-toc-modified-id="Active-Management-Formulation-5.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Active Management Formulation</a></span></li><li><span><a href="#Least-Squares-Formulation" data-toc-modified-id="Least-Squares-Formulation-5.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span><a href="https://www.cvxpy.org/examples/basic/least_squares.html" rel="nofollow" target="_blank">Least Squares Formulation</a></a></span></li></ul></li><li><span><a href="#Constructing-a-Volatility-Index-Tracking-Fund" data-toc-modified-id="Constructing-a-Volatility-Index-Tracking-Fund-6"><span class="toc-item-num">3&nbsp;&nbsp;</span>Constructing a Volatility Index Tracking Fund</a></span><ul class="toc-item"><li><span><a href="#Tracking-the-VIX-with-an-Investable-Universe" data-toc-modified-id="Tracking-the-VIX-with-an-Investable-Universe-6.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Tracking the VIX with an Investable Universe</a></span><ul class="toc-item"><li><span><a href="#Tracking-the-VIX-with-Futures" data-toc-modified-id="Tracking-the-VIX-with-Futures-6.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Tracking the VIX with Futures</a></span></li><li><span><a href="#Tracking-the-VIX-with-Negative-Beta-Stocks" data-toc-modified-id="Tracking-the-VIX-with-Negative-Beta-Stocks-6.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Tracking the VIX with Negative Beta Stocks</a></span></li><li><span><a href="#Tracking-the-VIX-with-High-Volatility-Stocks" data-toc-modified-id="Tracking-the-VIX-with-High-Volatility-Stocks-6.1.3"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>Tracking the VIX with High Volatility Stocks</a></span></li><li><span><a href="#Tracking-the-VIX-with-High-Correlation-with-VIX-Stocks" data-toc-modified-id="Tracking-the-VIX-with-High-Correlation-with-VIX-Stocks-6.1.4"><span class="toc-item-num">3.1.4&nbsp;&nbsp;</span>Tracking the VIX with High Correlation with VIX Stocks</a></span></li><li><span><a href="#Constructing-the-Investable-Universe-Returns-Data-Set" data-toc-modified-id="Constructing-the-Investable-Universe-Returns-Data-Set-6.1.5"><span class="toc-item-num">3.1.5&nbsp;&nbsp;</span>Constructing the Investable Universe Returns Data Set</a></span></li></ul></li><li><span><a href="#Decision-Variables" data-toc-modified-id="Decision-Variables-6.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Decision Variables</a></span></li><li><span><a href="#Objective" data-toc-modified-id="Objective-6.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Objective</a></span></li><li><span><a href="#Constraints" data-toc-modified-id="Constraints-6.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Constraints</a></span></li><li><span><a href="#Solution-and-Analysis" data-toc-modified-id="Solution-and-Analysis-6.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Solution and Analysis</a></span></li></ul></li><li><span><a

$\rule{800pt}{20pt}$

# Imports
"""

import os
import sys

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
import cvxpy as cp

from google.colab import drive
drive.mount('/content/drive')

print("python \t {}".format(".".join(map(str, sys.version_info[:3]))))
print("numpy \t {}".format(np.__version__))
print("pandas \t {}".format(pd.__version__))
print("cvxpy \t {}".format(cp.__version__))
print("seaborn \t {}".format(sns.__version__))
print("matplotlib \t {}".format(matplotlib.__version__))
print("pandas-datareader {}".format(pdr.__version__))

"""$\rule{800pt}{20pt}$

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Comparison_of_three_stock_indices_after_1975.svg/1200px-Comparison_of_three_stock_indices_after_1975.svg.png" width="550">

# Data

## Yahoo! Finance
<br>
<font size="+1">
    <ul>
        <li>We will use a Python package called <a href="https://pandas-datareader.readthedocs.io/en/latest/">Pandas Data Reader</a> to quickly scrape data from Yahoo! Finance.</li>
        <br>
        <li>Pandas Data Reader has additional interesting functionality that is worth checking out, if interested.</li>
        <br>
    </ul>
</font>
"""

! pip install pandas-datareader

##### Imports

import pandas_datareader as pdr
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import cvxpy as cp

"""$\rule{800pt}{20pt}$

## S&P 500 and the VIX
<br>
<font size="+1">
    <ul>
        <li>We will download daily OHLC (Open-High-Low-Close) variables for the VIX index as well as the S&P 500 ETF (SPY).</li>
        <br>
        <ul>
            <font color="green"><li style="color:green">It would be a good idea to write a function that allows us to grab any ticker we want from Yahoo! Finance and return a merged data frame consisting of adjusted closing prices and single period close-to-close returns, for each ticker.</li></font>
            <br>
        </ul>
        <li>We will see, empirically, one particular benefit of being able to have a tradable asset that replicates the VIX, which motivates the need for developing such a product.</li>
        <br>
    </ul>
</font>
"""

import pandas_datareader as pdr
import yfinance as yf
import datetime


spy = yf.download('SPY', start='1980-09-10', end=datetime.date.today())

vix = yf.download('^VIX', start='1980-09-10', end=datetime.date.today())

spy.head()

# Plot the difference between SPY's close and adjusted closing prices
spy[['Close', 'Adj Close']].plot(alpha=0.7)

vix[['Close', 'Adj Close']].plot(alpha=0.7)

"""<br>
<font size="+1">
    <ul>
        <li>There is a difference between the <b>closing price</b> and the <b>adjusted closing price</b> (<a href="https://help.yahoo.com/kb/SLN28256.html#:~:text=Adjusted%20close%20is%20the%20closing,Security%20Prices%20(CRSP)%20standards.">described by Yahoo! Finance</a>).</li>
        <br>
        <ul>
            <li>The closing price is simply the cash value of that specific piece of stock at day's end while the adjusted closing price reflects the closing price of the stock in relation to other stock attributes.</li>
            <br>
            <li>In general, the adjusted closing price is considered to be a more technically accurate reflection of the true value of the stock.</li>
            <br>
            <li>The closing price of a stock is only its cash value at day's end, whereas the adjusted closing price factors in things like dividends, stock splits and new stock offerings.</li>
            <br>
            <li>For more, see <a href="https://finance.zacks.com/impact-stock-splits-total-stockholders-equity-3325.html">here.</a></li>
            <br>
        </ul>
    </ul>
</font>

### Prices and Returns from Yahoo! Finance
<br>
<font size="+1">
    <ul>
        <li>The data, reported after closing (4pm ET), contains prices stamped at various times throughout the day ($t$):
        $$
        P^{open}_t, P^{high}_t, P^{low}_t, P^{close}_t,
        $$
        as well as a measure of volume ($V_t$) and a closing price that is adjusted for various corporate actions $$P^{adj -close}_t.$$</li>
        <br>
        <li>Note, the <b>return</b> of a security can be defined as the percentage change of the security's price $$r_{i,t} = \frac{P_{i,t} - P_{i,t-1}}{P_{i,t-1}},$$ where $P_{i,t}$ is the price of security $i$ at time $t$.</li>
        <br>
        <li>Additionally, we can make a very crude estimate of the expected return of a security by taking the sample average of a time series of returns $$\mathbb{E}[r_{i,t}] \approx \frac{1}{T}\sum_{j=0}^{T-1} r_{i, t-j} \ .$$</li>
        <br>
    </ul>
</font>

$\square$
"""

# Create a data frame for daily returns

spy_vix_returns = pd.DataFrame()

spy_vix_returns['SPY_ret'] = (spy.loc[:, 'Adj Close'] / spy.loc[:, 'Adj Close'].shift()) - 1

spy_vix_returns['VIX_ret'] = (vix.loc[:, 'Adj Close'] / vix.loc[:, 'Adj Close'].shift()) - 1

# Create a portfolio that does a daily rebalancing to ensure there is 90% SPY and 10% VIX portfolio weights
spy_vix_returns['(0.9SPY+0.1VIX)_ret'] = 0.9*spy_vix_returns['SPY_ret'] + 0.1*spy_vix_returns['VIX_ret']

# (Arithmetic) Average of returns of the two portfolios
spy_vix_returns[['SPY_ret', '(0.9SPY+0.1VIX)_ret']].mean()

# Standard deviation of daily returns of the two portfolios
spy_vix_returns[['SPY_ret', '(0.9SPY+0.1VIX)_ret']].std()

# Sharpe ratio of the daily returns of the two portfolios
spy_vix_returns[['SPY_ret', '(0.9SPY+0.1VIX)_ret']].mean() / \
 spy_vix_returns[['SPY_ret', '(0.9SPY+0.1VIX)_ret']].std()

"""<br>
<font size="+1">
    <ul>
        <li>It is always a good idea to plot your data and see what you observe.</li>
        <br>
        <li style="color:blue">This is one area where the skills you have developed in DSO 545 and GSBA 545 can be deployed.</li>
        <br>
        <ul style="color:blue">
            <li>Summary statistics and hypothesis testing,</li>
            <br>
            <li>time series and histogram visualizations,</li>
            <br>
            <li>algorithmic exploratory data analysis - clustering, principal components or factor analysis, etc.,</li>
            <br>
            <li>etc.</li>
            <br>
        </ul>
    </ul>
</font>
"""

# Plot a time series of the daily returns
spy_vix_returns[['SPY_ret', '(0.9SPY+0.1VIX)_ret']].plot(alpha=0.8)

# Plot a histogram of the daily returns
spy_vix_returns[['SPY_ret', '(0.9SPY+0.1VIX)_ret']].plot(kind='hist', bins=100, figsize=(16,8), alpha=0.2)

portfolio = spy_vix_returns[['SPY_ret', '(0.9SPY+0.1VIX)_ret']].copy()

portfolio.dropna(inplace=True)

# Period where US suffered credit rating downgrade by Standard and Poor's

(portfolio+1).loc['2011-01':'2011-09'].cumprod().plot()

(portfolio+1).loc['2014-01':'2014-12'].cumprod().plot()

(portfolio+1).loc['2019-01':'2020-12'].cumprod().plot()

(portfolio+1).loc['2021-01':].cumprod().plot()

# Plot the Gross Return of SPY and the SPY-VIX daily rebalanced portfolio for the full sample

(portfolio+1).cumprod().plot()

"""$\rule{800pt}{20pt}$

## Tradeable VIX-like Products
<br>
<font size="+1">
    <ul>
        <li>We will download daily OHLC (Open-High-Low-Close) variables for the VIX, and its associated ETFs and ETNs that are supposed to benchmark to the VIX.</li>
        <br>
        <li>This will show us how the current existing products are failing to adequately replicate the VIX index.</li>
        <br>
    </ul>
</font>
"""

# VXXB = yf.download('VXXB', start='1980-09-10', end=datetime.date.today())|

vix = yf.download('^VIX', start='1980-09-10', end=datetime.date.today())

# UVXY is one of the worst ETFs in terms of decay.
# If you buy and hold, you are likely to lose a lot.
# Your $28.00 stock was once worth $1.461 million adjusted for reverse stock splits.

uvxy = yf.download('UVXY', start='1980-09-10', end=datetime.date.today())

vxx = yf.download('VXX', start='1980-09-10', end=datetime.date.today())

vixy = yf.download('VIXY', start='1980-09-10', end=datetime.date.today())

# The ETNs are linked to the daily return of the index and do not represent an investment in the VIX.
viix = yf.download('VIIX', start='1980-09-10', end=datetime.date.today())

# View a sample of the data
vix.head()

vxx.head()

# Plot the VIX
vix['Adj Close'].plot()

# Plot the full sample of the LEVEL
vix['Adj Close'].plot()

vxx['Adj Close'].plot()

# Plot a sub-sample of the LEVEL
vix['Adj Close'].loc['2018':].plot(legend=True, label='VIX')

vxx['Adj Close'].loc['2018':].plot(legend=True, label='VXX')

# # Plot the VIX and the normalized VXX
# vix['Adj Close'].loc['2018':].plot(legend=True, label='VIX')

# # VXX is normalized by the inital value of VIX from the subsample
# (vxx['Adj Close'].loc['2018':]/vix['Adj Close'].loc['2018':].iloc[0]).plot(legend=True, label='VXX')

# Plot a sub-sample of the RETURN
vix['Adj Close'].loc['2018':].pct_change().plot(legend=True, label='VIX')

vxx['Adj Close'].loc['2018':].pct_change().plot(legend=True, label='VXX')

"""<br>
<font size="+1">
    <ul>
        <li>We will do further sub-sample analysis to investigate the tracking quality of the VXX (in terms of both the level and percentage change of the VIX) during different time periods.</li>
        <br>
    </ul>
</font>
"""

# Plot a different sub-sample of the LEVEL
vix['Adj Close'].loc['2021':].plot(legend=True, label='VIX')

vxx['Adj Close'].loc['2021':].plot(legend=True, label='VXX')

# Plot a different sub-sample of the RETURN
vix['Adj Close'].pct_change().loc['2021':].plot(legend=True, label='VIX')

vxx['Adj Close'].pct_change().loc['2021':].plot(legend=True, label='VXX')

"""<br>
<font size="+1">
    <ul>
        <li>How can we attempt to find a better alternative?</li>
        <br>
    </ul>
</font>

$\rule{800pt}{20pt}$

## <a href="https://www.cboe.com/tradable_products/vix/vix_historical_data/">CBOE Historical Data</a>
<br>
<font size="+1">
    <ul>
        <li><a href="https://www.cboe.com/us/futures/market_statistics/historical_data/">CBOE Futures Historical Data</a></li>
        <br>
        <li><a href="https://www.cboe.com/tradable_products/vix/vix_futures/specifications/">CBOE VIX Futures contract specifications</a></li>
        <br>
        <li><a href="https://www.cboe.com/us/futures/market_statistics/historical_data/archive/">CBOE VIX products historical archived data</a></li>
        <br>
    </ul>
</font>

$\rule{800pt}{20pt}$

<a href="https://www.amazon.com/Active-Portfolio-Management-Quantitative-Controlling/dp/0070248826"><img src="https://m.media-amazon.com/images/I/41wADnIW1jL._AC_SY780_.jpg" width="250"></a>

# Portfolio Management Relative To a Benchmark
<br>
<font size="+1">
    <ul>
        <li>In an investment portfolio, the <i>security selection</i> problem is concerned with determining the holdings of specific securities within a given <i>investable universe</i>.</li>
        <br>
        <li>It is customary to manage and evaluate the portfolio of securities <b>relative</b> to some predefined <b>benchmark portfolio</b> that represents a particular investable universe.</li>
        <br>
        <li>The <b>benchmark portfolio</b> provides a reference point for the construction of a portfolio.</li>
        <br>
        <li>The management of a portfolio of securities relative to a benchmark could be <i>passive</i> or <i>active</i>.</li>
        <br>
        <li>The goal of <i>passive</i> security portfolio management is to <b>replicate</b> the benchmark and the goal of the <i>active</i> security portfolio management is to <b>beat</b> the benchmark.</li>
        <br>
        $\rule{800pt}{10pt}$
        <br>
        <font color="blue"><li style="color:blue">Our goal is to create a <i>passive</i> portfolio that adequately tracks the VIX index (as opposed to an <i>active</i> portfolio that trys to beat the VIX index) using only <i>primitive</i> securities, such as stocks, (as opposed to futures or other derivatives).</li></font>
        <br>
        <ul style="color:blue">
            <font color="blue"><li>This is a very vague objective!</li>
            <br>
            <li>Our task is to <b>quantify</b> this goal.</li></font>
            <br>
        </ul>
    </ul>
</font>

$\square$

$\rule{800pt}{20pt}$

## What's the Investable Universe?
<br>
<font size="+1">
    <ul>
        <li>The <b>investable universe</b> is the collection of all tradable assets (stocks, bonds, futures, options, etc.) that are going to make up our portfolio that is designed to track the benchmark.</li>
        <br>
        <li>Our formulation will crucially depend on how the tracking portfolio's investable universe compares to the benchmark's investable universe.</li>
        <br>
        <li>In general, the benchmark does not need to be constructed from an universe of investable securities, it is simply a number that represents some quantity.</li>
        <br>
        <li>In particular, assume we want to construct a portfolio from an investable universe of \begin{equation}n\end{equation} securities with percentage holdings
        \begin{equation}
        \bar{w} = \begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_n\end{bmatrix}.
        \end{equation}</li>
        <br>
    </ul>
</font>

$\square$

$\rule{800pt}{20pt}$

## Active Management Formulation
<br>
<font size="+1">
    <ul>
        <li>Recall:</li>
        <br>
        <ul style="color:blue">
            <font color="blue"><li>We can define a return as the relative price change, or growth rate, of the share price $$r_{i,t} = \frac{P_{i,t} - P_{i,t-1}}{P_{i,t-1}}$$</li>
            <br>
            <li>Fix a point in time $t$, and drop the time subscript from the returns.</li>
            <br>
            <li>We can define a portfolio as a linear combination of individual securities' returns $$r_p = w_1 r_1 + w_2 r_2 + \cdots w_n r_n = \bar{w}^T \bar{r}, $$ where $n$ is the total number of securities in your investable universe and $w_i$ is the percentage of your capital that you want to invest in the $i^{th}$ security.</li>
            <br>
            <li>The expected rate of return of the portfolio is given by $$\mathbb{E}[r_p] = \sum_{i=1}^n w_i \mathbb{E}[r_i] = \bar{w}^T \bar{\mu},$$ where $\bar{w}$ is the vector of weights and $\bar{\mu}$ is vector of expected returns.</li></font>
            <br>
        </ul>
        <font color="red"><li style="color:red"><b>Assume the benchmark is constructed from the same investable universe as your managed portfolio.</b></li></font>
        <br>
        <li>Consider a benchmark with returns $$r_b = w^b_1 r_1 + w^b_2 r_2 + \cdots w^b_n r_n = \bar{w_b}^T \bar{r}.$$</li>
        <br>
        <li>Then the difference between the portfolio return and the benchmark return $$r_p - r_b =  \bar{w_b}^T \bar{r} - \bar{w_b}^T \bar{r} = (\bar{w} - \bar{w_b})^T \bar{r}$$ is known as the <b>active return</b>, which is the return relative to the benchmark portfolio.</li>
        <br>
        <li>The vector $$\bar{w} - \bar{w_b}$$ is known as the <b>active holdings</b> of the portfolio.</li>
        <br>
        <li>If we assume the variance to be our measure of <i>risk</i>, then we can consider the variance of the active return, known as <b>active risk</b> or <b>tracking error</b> $$Var(r_p - r_b)= Var((\bar{w} - \bar{w_b})^T \bar{r}) = \sum_{i=1}^n \sum_{j=1}^n (w_i - w_i^b) (w_j - w_j^b) Cov(r_i, r_j)$$ $$\Updownarrow$$ $$Var(r_b - r_p) = Var((\bar{w} - \bar{w_b})^T \bar{r}) = (\bar{w}-\bar{w_b})^T \Sigma (\bar{w}-\bar{w_b}),$$ where $(\bar{w}-\bar{w_b})$ is the vector of active weights and $\Sigma$ is the matrix of covariances of returns.</li>
        <br>
        <font color="blue"><li style="color:blue">\begin{equation} Var(r_b - r_p) = Var((\bar{w} - \bar{w_b})^T \bar{r}) = (\bar{w}-\bar{w_b})^T \Sigma (\bar{w}-\bar{w_b}) =
        \underbrace{\begin{bmatrix}
        w_1 - w_1^b & w_2 - w_2^b & \cdots & w_n - w_n^b \\
        \end{bmatrix}}_{\underbrace{(\bar{w} - \bar{w_b})^T}_{(1\times n)}}
        \underbrace{\begin{bmatrix}
Cov(r_1,r_1) & Cov(r_1, r_2) & \cdots & Cov(r_1, r_n)\\
\vdots & \vdots & \cdots & \vdots \\
Cov(r_n, r_1) & Cov(r_n, r_2) & \vdots & Cov(r_n, r_n) \\
            \end{bmatrix}}_{\underbrace{\Sigma}_{(n\times n)}}
            \underbrace{\begin{bmatrix}
        w_1 - w_1^b \\ w_2 - w_2^b \\ \vdots \\ w_n - w_n^b \\
        \end{bmatrix}}_{\underbrace{(\bar{w} - \bar{w_b})}_{(n\times 1)}}\end{equation}</li></font>
        <br>
        <font color="green"><li style="color:green">We can construct a wide range of goals and constraints to achieve a portfolio replication that satisfies active return and tracking error goals and constraints.</li>
        <br>
        <li style="color:green">Be aware that different formulations have different qualities of solutions, so additional experimentation will be warranted.</li>
        <br>
        <li style="color:green">Also, what if your benchmark isn't constructed from the same set of investable securities that you want to use to form your managed portfolio? </li>
        <br>
        <li style="color:green">What if your benchmark isn't constructed from any set investable securities?</li>
        <br>
        <li style="color:green"><b>We need a reformulation!</b></li></font>
        <br>
    </ul>
</font>

$\square$

$\rule{800pt}{20pt}$

## <a href="https://www.cvxpy.org/examples/basic/least_squares.html">Least Squares Formulation</a>
<br>
<font size="+1">
    <ul>
        <font color="red"><li style="color:red"><b>Assume the benchmark is NOT constructed from the same investable universe as your managed portfolio.</b></li></font>
        <br>
        <font color="red"><li style="color:red"><b>In particular, assume the benchmark is just a number that we want to track.</b></li></font>
        <br>
        <li>One (non-unique) way of interpreting this vague objective is by <i>determining</i> a portfolio whose value is <i>close</i> to the benchmark that we want to track.</li>
        <br>
        <ul>
            <li>How do you <i>determine</i> a portfolio?</li>
            <br>
            <li>How do you stay <i>close</i> to a benchmark?</li>
            <br>
            <li>How do you measure <i>closeness</i>?</li>
            <br>
        </ul>
        <li>The answers to these questions are entirely in our creative control!</li>
        <br>
        $\rule{800pt}{10pt}$
        <br>
        <li>Assume we are trying to track the returns to the VIX (our benchmark), which we can denote as $r_b$, with some portfolio with returns $r_p$, for all time $t$.</li>
        <br>
        <li>We decide to measure closeness between the tracker and benchmark portfolios as the daily sum of squared errors \begin{equation} SSE(r_p, r_b) = \sum_{t=1}^T (r_{p, t} - r_{b, t})^2 = \cdots = ||r_p - r_b||_2^2 = \cdots = ||R\bar{w} - r_b||_2^2 ,\end{equation} where \begin{equation}R = \begin{bmatrix}r_{1,1} & r_{1,2} & \cdots & r_{1,n} \\
        r_{2,1} & r_{2,2} & \cdots & r_{2,n} \\
        \vdots & \vdots & \cdots & \vdots \\
        r_{T,1} & r_{T,2} & \cdots & r_{T,n} \\
        \end{bmatrix}_{ \ (\text{time} \times \text{assets})}.\end{equation} is the matrix (table) of historical returns of all assets in the tracking portfolio's investable universe.</li>
        <br>
        <li>Every column in $R$ represents the history of a particular asset $i$, and every row in $R$ represents the cross-section of asset returns at a particular time $t$.</li>
        <br>
        <font color="green"><li style="color:green">This formulation allows us to track a number using any investable universe, or set of securities, we want!</li></font>
        <br>
    </ul>
</font>

$\square$

$\rule{800pt}{20pt}$

# Constructing a Volatility Index Tracking Fund
<br>
<font size="+1">
    <ul>
        <li>As mentioned before, this is a real problem that has been studied from various angles.</li>
        <br>
        <li>Two such angles are: <a href="https://arxiv.org/pdf/1907.00293.pdf">Tracking VIX with VIX Futures: Portfolio Construction and Performance</a>, and <a href="https://www.dallasfed.org/~/media/documents/banking/occasional/1401.pdf">Constructing Zero-Beta VIX Portfolios
with Dynamic CAPM</a>.</li>
        <br>
        <li>We will be taking a less technical and more experimental approach, which should cause us to have low expectations of success; however, our approach can be iterated upon and extended in many ways.</li>
        <br>
        <font color="red"><li style="color:red">This problem gives a playground to apply all fields of analytics from the descriptive, to the predictive, and finally to the prescriptive!</li></font>
        <br>
    </ul>
</font>

$\rule{800pt}{20pt}$

## Tracking the VIX with an Investable Universe
<br>
<font size="+1">
    <ul>
        <li>We have to answer the following question:</li>
        <br>
        <ul>
            <li><b>What products do we want to manage to track the VIX index?</b></li>
            <br>
        </ul>
        <li>Answering this question requires a lot of data analysis, as well as some domain knowledge.</li>
        <br>
        <li>In the interest of time, we will look at a small subset of securities that we hope will have some signal.</li>
        <br>
    </ul>
</font>

$\rule{800pt}{20pt}$

### Tracking the VIX with Futures
<br>
<font size="+1">
    <ul>
        <li>The universe of futures would be a very good starting point, however, they are a more complicated product that requires more advanced data wrangling techniques.</li>
        <br>
        <li>If you are up for the challenge, feel free to use these products as part of your investable universe!</li>
        <br>
        <ul>
            <li>I have downloaded data on these products from the CBOE, and have placed the files on the Google drive.</li>
            <br>
        </ul>
    </ul>
</font>

$\rule{800pt}{20pt}$

### Tracking the VIX with Negative Beta Stocks
"""

# https://www.suredividend.com/negative-beta-stocks/
# https://www.marketbeat.com/market-data/negative-beta-stocks/
# https://seekingalpha.com/news/3730901-inverse-qqq-etfs

"""<br>
<font size="+1">
    <ul>
        <li>We will download daily OHLC (Open-High-Low-Close) variables for a few securities that we believe tend move in opposite directions as the S&P 500.</li>
        <br>
        <li>We hope these securities are related to the VIX.</li>
        <br>
    </ul>
</font>
"""

import datetime as dt

# PSQ, SH, CLX, TORM

# ProShares Short QQQ ETF
psq = yf.download('PSQ', start='1980-09-10', end=datetime.date.today())

# ProShares Short S&P500 ETF
sh = yf.download('SH', start='1980-09-10', end=datetime.date.today())

# Clorox Co
clx = yf.download('CLX', start='1980-09-10', end=datetime.date.today())

# TORM is a world-leading specialist carrier of energy and clean petroleum products
torm = yf.download('TORM', start='1980-09-10', end=datetime.date.today())

psq.head()

"""$\rule{800pt}{20pt}$

### Tracking the VIX with High Volatility Stocks
"""

# https://www.tradingview.com/markets/stocks-usa/market-movers-most-volatile/

"""<br>
<font size="+1">
    <ul>
        <li>We will download daily OHLC (Open-High-Low-Close) variables for a few securities that we believe tend to move around a lot and have high volatility.</li>
        <br>
        <li>We hope these securities are related to the VIX.</li>
        <br>
    </ul>
</font>
"""

# AGBA, COMP, PIXY, VTYX

# AGBA Acquisition Ltd
agba = yf.download('AGBA', start='1980-09-10', end=datetime.date.today())

# Compass Inc
comp = yf.download('COMP', start='1980-09-10', end=datetime.date.today())

# ShiftPixy Inc
pixy = yf.download('PIXY', start='1980-09-10', end=datetime.date.today())

# Ventyx Biosciences, Inc.
vtyx = yf.download('VTYX', start='1980-09-10', end=datetime.date.today()) #PLXP

agba.head()

"""$\rule{800pt}{20pt}$

### Tracking the VIX with High Correlation with VIX Stocks
"""

# https://www.businessinsider.com/investing-101-five-profitable-stocks-with-a-strong-vix-correlation-2011-9
# https://seekingalpha.com/article/823781-10-high-yield-dividend-stocks-with-positive-vix-correlation

"""<br>
<font size="+1">
    <ul>
        <li>We will download daily OHLC (Open-High-Low-Close) variables for a few securities that we believe tend move in the same directions as the VIX index.</li>
        <br>
        <li>We hope these securities are related to the VIX.</li>
        <br>
    </ul>
</font>
"""

# DG, GME, MCY, KR

# Dollar General
dg = yf.download('DG', start='1980-09-10', end=datetime.date.today())

# GameStop Corp.
gme = yf.download('GME', start='1980-09-10', end=datetime.date.today())

# Mercury General Corp
mcy = yf.download('MCY', start='1980-09-10', end=datetime.date.today())

# # Credit Suisse Group AG
# cs = yf.download('CS', start='1980-09-10', end=datetime.date.today())

# Kroger
kr = yf.download('KR', start='1980-09-10', end=datetime.date.today())

kr.head()

"""$\rule{800pt}{20pt}$

### Constructing the Investable Universe Returns Data Set
<br>
<font size="+1">
    <ul>
        <li>\begin{equation}R\end{equation} is the matrix (table) of historical returns of all assets in the tracking portfolio's investable universe, that is:
        \begin{equation}R = \begin{bmatrix}r_{1,1} & r_{1,2} & \cdots & r_{1,n} \\
        r_{2,1} & r_{2,2} & \cdots & r_{2,n} \\
        \vdots & \vdots & \cdots & \vdots \\
        r_{T,1} & r_{T,2} & \cdots & r_{T,n} \\
        \end{bmatrix}_{ \ (\text{time} \times \text{assets})}.\end{equation}</li>
        <br>
        <li>Every column in $R$ represents the history of a particular asset $i$, and every row in $R$ represents the cross-section of asset returns at a particular time $t$.</li>
        <br>
    </ul>
</font>

$\square$
"""

today = datetime.date.today()

two_years_ago = today - datetime.timedelta(2*365)

returns = pd.DataFrame({'cash':0}, index=pd.date_range('1980-09-10', today, freq='b'))

ticker_symbols = ['PSQ', 'SH', 'CLX', 'TORM',
                 'AGBA', 'COMP', 'PIXY', 'VTYX',
                 'DG', 'GME', 'MCY', 'KR',
                 'VIX']

ticker_data = [psq, sh, clx, torm,
              agba, comp, pixy, vtyx,
              dg, gme, mcy, kr,
              vix]

for ticker, data in zip(ticker_symbols, ticker_data):
    returns[ticker+'_ret'] = data['Adj Close'].pct_change()

"""<br>
<font size="+1">
    <ul>
        <li>It is always a good idea to plot your data and see what you observe.</li>
        <br>
        <font color="blue"><li style="color:blue">This is one area where the skills you have developed in DSO 545 and GSBA 545 can be deployed.</li>
        <br>
        <ul style="color:blue">
            <font color="blue"><li>Summary statistics and hypothesis testing,</li>
            <br>
            <li>time series and histogram visualizations,</li>
            <br>
            <li>algorithmic exploratory data analysis - clustering, principal components or factor analysis, etc.,</li>
            <br>
            <li>etc.</li></font>
            <br>
        </ul>
    </ul>
</font>
"""

returns.plot(figsize=(16,8), legend=True)

plt.title('Daily Returns of Universe of Securities')

np.log(returns+1).plot(kind='hist', bins=100, alpha=0.5, figsize=(16,8))

mean_variance = pd.DataFrame({'Mean': returns.mean(),
                              'Volatility': returns.std()})

mean_variance

"""<br>
<font size="+1">
    <ul>
        <li>The see the expected return and variance of the three securities for a single day, as well as the cross-correlations between the securities.</li>
        <br>
        <font color="red"><li style="color:red">Recall, the correlation between two variables $(X_i, X_j)$ is defined as $$\rho_{X_i, X_j} = \frac{Cov(X_i, X_j)}{\sqrt{Var(X_i)} \ \sqrt{Var(X_j)}} \ , $$ and measures the extent to which the two variables <b>linearly</b> move together.</li></font>
        <br>
        <li>This is far from what you would use in practice, and there are so many ways to innovate on obtaining these estimates using analytics techniques, both old and new.</li>
        <br>
        <li>How might this change if we used different horizons?</li>
        <br>
        <li>How can you think of these estimates (pros and cons) and how they're going to be used from the different perspectives of</li>
        <br>
        <ul>
            <li>descriptive analytics,</li>
            <br>
            <li>predictive analytics,</li>
            <br>
            <li>prescriptive analytics,</li>
            <br>
            <li>and business development and strategy, as well as product management?</li>
            <br>
        </ul>
    </ul>
</font>

$\square$
"""

corr_matrix = returns.corr()

corr_matrix

covariance_matrix = returns.cov()

covariance_matrix

mean_variance_correlations = pd.concat([mean_variance, corr_matrix], axis=1)

mean_variance_correlations

"""$\rule{800pt}{20pt}$

## Decision Variables
<br>
<font size="+1">
    <ul>
        <li>We want to construct a portfolio from an investable universe of \begin{equation}n\end{equation} securities with percentage holdings
        \begin{equation}\bar{w} = \begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_n\end{bmatrix}.
        \end{equation}</li>
        <br>
    </ul>
</font>

$\square$
"""

# We choose to work with a subset of the data that is more relevant to future performance
returns = returns.loc[two_years_ago:today, :].copy()

# Number of nulls per column
returns.isna().sum()

# Drop the rows that have a null value
returns.dropna(axis=0, inplace=True)

returns.shape

# Returns contains the target variable, VIX, which we don't want a weight for
weights = cp.Variable(returns.shape[1] - 1)

"""$\rule{800pt}{20pt}$

## Objective
<br>
<font size="+1">
    <ul>
        <li>Assume we are trying to track the returns to the VIX (our benchmark), which we can denote as $r_b$, with some portfolio with returns $r_p$, for all time $t$.</li>
        <br>
        <li>We decide to measure closeness between the tracker and benchmark portfolios as the daily sum of squared errors.</li>
        <br>
        <li>We want to choose the portfolio weights that minimizes the distance, or error, between the tracking portfolio and the VIX portfolio.</li>
        <br>
        <li>\begin{align}
        \text{minimize: } & SSE(r_p, r_b) = \sum_{t=1}^T (r_{p, t} - r_{b, t})^2  = ||R\bar{w} - r_b||_2^2 \\
        \end{align}</li>
        <br>
    </ul>
</font>

$\square$
"""

# Matrix multiply the returns data frame (without the VIX ) and the weights vector
returns.iloc[:, :-1].values @ weights

# Define the error between the tracking portfolio and the VIX portfolio
error = returns.iloc[:,:-1].values @ weights - returns['VIX_ret'].values

# Compute the sum of squared errors between the tracking portfolio and the VIX portfolio
sum_of_squared_error = cp.sum_squares(error)

"""$\rule{800pt}{20pt}$

## Constraints
<br>
<font size="+1">
    <ul>
        <li>For simplicity, we will assume the sum of the weights must equal one.</li>
        <br>
        <li>$$\sum_{i=1}^n w_i = \bar{w}^T \bar{\mathbb{1}} = 1.$$</li>
        <br>
        <li>This allows for shorting and applying leverage, but typically keeps them from being too overweight in any given asset.</li>
        <br>
        <li>There are plenty more constraints that we should consider on a second passing.</li>
        <br>
    </ul>
</font>

$\square$
"""

prob = cp.Problem(cp.Minimize(sum_of_squared_error), [sum(weights)==1])

"""$\rule{800pt}{20pt}$

## Solution and Analysis
<br>
<font size="+1">
    <ul>
        <li>We're seeking a prescription regarding how to build a minimum error tracking portfolio for the VIX index.</li>
        <br>
    </ul>
</font>
"""

# Minimal error - needs to be compared with an existing product for reference, say VXX
prob.solve()

# Prescribed portfolio weights for constructing the tracking portfolio
np.round(weights.value, 2)

pd.DataFrame(np.round(weights.value, 2),
             index=returns.columns[:-1],
             columns=['weights'])

vix_returns = returns['VIX_ret']
vxx_returns = vxx.loc[returns.index, 'Adj Close'].pct_change()

error_between_vix_vxx = ((vix_returns - vxx_returns)**2).sum()

error_between_vix_vxx

dates = returns.index

# Performance of IN-SAMPLE tracking portfolio
tracking_portfolio = pd.Series(returns.iloc[:, :-1].values @ weights.value,
                               index=dates)

plt.figure(figsize=(16,8))

vix_returns.plot(label='VIX', legend=True, alpha=0.5)
vxx_returns.plot(label='VXX', legend=True, alpha=0.5)
tracking_portfolio.plot(label='Tracking_Port', legend=True, alpha=0.5)

"""<br>
<font size="+1">
    <ul>
        <li>Not a complete success, but also not bad for a first attempt!</li>
        <br>
        <li>Definitely more work to do, but it appears we are on a good track.</li>
        <br>
        <font color="red"><li style="color:red">Do we need to think about different time samples, such as in-sample sets, out-of-sample sets, or a portfolio prescription formed on a daily basis?</li></font>
        <br>
    </ul>
</font>
"""

# As a reference point, consider the error between the S&P 500 Index (SPX) and a popular ETF that tracks the index (SPY)

spy = yf.download('SPY', start='1980-09-10', end=datetime.date.today())
spx = yf.download('^SPX', start='1980-09-10', end=datetime.date.today())

spy_returns = spy.loc[returns.index, 'Adj Close'].pct_change()
spx_returns = spx.loc[returns.index, 'Adj Close'].pct_change()

error_between_spx_spy = ((spx_returns - spy_returns)**2).sum()
error_between_spx_spy

plt.figure(figsize=(16,8))

spx_returns.plot(label='SPX', legend=True, alpha=0.5)
spy_returns.plot(label='SPY', legend=True, alpha=0.5)

"""$\rule{800pt}{20pt}$"""