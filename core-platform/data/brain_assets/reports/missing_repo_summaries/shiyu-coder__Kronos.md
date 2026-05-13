# Missing Repo Summary Source: shiyu-coder/Kronos

- URL: https://github.com/shiyu-coder/Kronos
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/shiyu-coder__Kronos
- Clone Status: cloned
- Language: Python
- Stars: 24062
- Topics: 
- Description: Kronos: A Foundation Model for the Language of Financial Markets

## Extracted README / Docs / Examples



# FILE: README.md

<div align="center">
  <h2><b>Kronos: A Foundation Model for the Language of Financial Markets </b></h2>
</div>


<div align="center">

</a> 
<a href="https://huggingface.co/NeoQuasar"> 
<img src="https://img.shields.io/badge/🤗-Hugging_Face-yellow" alt="Hugging Face"> 
</a> 
<a href="https://shiyu-coder.github.io/Kronos-demo/"> <img src="https://img.shields.io/badge/🚀-Live_Demo-brightgreen" alt="Live Demo"> </a>
<a href="https://github.com/shiyu-coder/Kronos/graphs/commit-activity"> 
<img src="https://img.shields.io/github/last-commit/shiyu-coder/Kronos?color=blue" alt="Last Commit"> 
</a> 
<a href="https://github.com/shiyu-coder/Kronos/stargazers"> 
<img src="https://img.shields.io/github/stars/shiyu-coder/Kronos?color=lightblue" alt="GitHub Stars"> 
</a> 
<a href="https://github.com/shiyu-coder/Kronos/network/members"> 
<img src="https://img.shields.io/github/forks/shiyu-coder/Kronos?color=yellow" alt="GitHub Forks"> 
</a> 
<a href="./LICENSE"> 
<img src="https://img.shields.io/github/license/shiyu-coder/Kronos?color=green" alt="License"> 
</a>

</div>

<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://zdoc.app/de/shiyu-coder/Kronos">Deutsch</a> | 
  <a href="https://zdoc.app/es/shiyu-coder/Kronos">Español</a> | 
  <a href="https://zdoc.app/fr/shiyu-coder/Kronos">Français</a> | 
  <a href="https://zdoc.app/ja/shiyu-coder/Kronos">日本語</a> | 
  <a href="https://zdoc.app/ko/shiyu-coder/Kronos">한국어</a> | 
  <a href="https://zdoc.app/pt/shiyu-coder/Kronos">Português</a> | 
  <a href="https://zdoc.app/ru/shiyu-coder/Kronos">Русский</a> | 
  <a href="https://zdoc.app/zh/shiyu-coder/Kronos">中文</a>
</div>

<p align="center">

<img src="./figures/logo.png" width="100">

</p>

> Kronos is the **first open-source foundation model** for financial candlesticks (K-lines), 
> trained on data from over **45 global exchanges**.


</div>

## 📰 News
*   🚩 **[2025.11.10]** Kronos has been accpeted by AAAI 2026.
*   🚩 **[2025.08.17]** We have released the scripts for fine-tuning! Check them out to adapt Kronos to your own tasks.
*   🚩 **[2025.08.02]** Our paper is now available on [arXiv](https://arxiv.org/abs/2508.02739)!

<p align="center">

## 📜 Introduction

**Kronos** is a family of decoder-only foundation models, pre-trained specifically for the "language" of financial markets—K-line sequences. Unlike general-purpose TSFMs, Kronos is designed to handle the unique, high-noise characteristics of financial data. It leverages a novel two-stage framework: 
1. A specialized tokenizer first quantizes continuous, multi-dimensional K-line data (OHLCV) into **hierarchical discrete tokens**. 
2. A large, autoregressive Transformer is then pre-trained on these tokens, enabling it to serve as a unified model for diverse quantitative tasks.

<p align="center">
    <img src="figures/overview.png" alt="" align="center" width="700px" />
</p>

## ✨ Live Demo 
We have set up a live demo to visualize Kronos's forecasting results. The webpage showcases a forecast for the **BTC/USDT** trading pair over the next 24 hours. 

**👉 [Access the Live Demo Here](https://shiyu-coder.github.io/Kronos-demo/)** 

## 📦 Model Zoo 
We release a family of pre-trained models with varying capacities to suit different computational and application needs. All models are readily accessible from the Hugging Face Hub.

| Model        | Tokenizer                                                                       | Context length | Params  | Open-source                                                               |
|--------------|---------------------------------------------------------------------------------| -------------- | ------ |---------------------------------------------------------------------------|
| Kronos-mini  | [Kronos-Tokenizer-2k](https://huggingface.co/NeoQuasar/Kronos-Tokenizer-2k)     | 2048           | 4.1M   | ✅ [NeoQuasar/Kronos-mini](https://huggingface.co/NeoQuasar/Kronos-mini)  |
| Kronos-small | [Kronos-Tokenizer-base](https://huggingface.co/NeoQuasar/Kronos-Tokenizer-base) | 512            | 24.7M  | ✅ [NeoQuasar/Kronos-small](https://huggingface.co/NeoQuasar/Kronos-small) |
| Kronos-base  | [Kronos-Tokenizer-base](https://huggingface.co/NeoQuasar/Kronos-Tokenizer-base) | 512            | 102.3M | ✅ [NeoQuasar/Kronos-base](https://huggingface.co/NeoQuasar/Kronos-base)   |
| Kronos-large | [Kronos-Tokenizer-base](https://huggingface.co/NeoQuasar/Kronos-Tokenizer-base) | 512            | 499.2M | ❌                                                                         |


## 🚀 Getting Started

### Installation

1. Install Python 3.10+, and then install the dependencies:

```shell
pip install -r requirements.txt
```

### 📈 Making Forecasts

Forecasting with Kronos is straightforward using the `KronosPredictor` class. It handles data preprocessing, normalization, prediction, and inverse normalization, allowing you to get from raw data to forecasts in just a few lines of code.

**Important Note**: The `max_context` for `Kronos-small` and `Kronos-base` is **512**. This is the maximum sequence length the model can process. For optimal performance, it is recommended that your input data length (i.e., `lookback`) does not exceed this limit. The `KronosPredictor` will automatically handle truncation for longer contexts.

Here is a step-by-step guide to making your first forecast.

#### 1. Load the Tokenizer and Model

First, load a pre-trained Kronos model and its corresponding tokenizer from the Hugging Face Hub.

```python
from model import Kronos, KronosTokenizer, KronosPredictor

# Load from Hugging Face Hub
tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = Kronos.from_pretrained("NeoQuasar/Kronos-small")
```

#### 2. Instantiate the Predictor

Create an instance of `KronosPredictor`, passing the model, tokenizer, and desired device.

```python
# Initialize the predictor
predictor = KronosPredictor(model, tokenizer, max_context=512)
```

#### 3. Prepare Input Data

The `predict` method requires three main inputs:
-   `df`: A pandas DataFrame containing the historical K-line data. It must include columns `['open', 'high', 'low', 'close']`. `volume` and `amount` are optional.
-   `x_timestamp`: A pandas Series of timestamps corresponding to the historical data in `df`.
-   `y_timestamp`: A pandas Series of timestamps for the future periods you want to predict.

```python
import pandas as pd

# Load your data
df = pd.read_csv("./data/XSHG_5min_600977.csv")
df['timestamps'] = pd.to_datetime(df['timestamps'])

# Define context window and prediction length
lookback = 400
pred_len = 120

# Prepare inputs for the predictor
x_df = df.loc[:lookback-1, ['open', 'high', 'low', 'close', 'volume', 'amount']]
x_timestamp = df.loc[:lookback-1, 'timestamps']
y_timestamp = df.loc[lookback:lookback+pred_len-1, 'timestamps']
```

#### 4. Generate Forecasts 

Call the `predict` method to generate forecasts. You can control the sampling process with parameters like `T`, `top_p`, and `sample_count` for probabilistic forecasting.

```python
# Generate predictions
pred_df = predictor.predict(
    df=x_df,
    x_timestamp=x_timestamp,
    y_timestamp=y_timestamp,
    pred_len=pred_len,
    T=1.0,          # Temperature for sampling
    top_p=0.9,      # Nucleus sampling probability
    sample_count=1  # Number of forecast paths to generate and average
)

print("Forecasted Data Head:")
print(pred_df.head())
```

The `predict` method returns a pandas DataFrame containing the forecasted values for `open`, `high`, `low`, `close`, `volume`, and `amount`, indexed by the `y_timestamp` you provided.

For efficient processing of multiple time series, Kronos provides a `predict_batch` method that enables parallel prediction on multiple datasets simultaneously. This is particularly useful when you need to forecast multiple assets or time periods at once.

```python
# Prepare multiple datasets for batch prediction
df_list = [df1, df2, df3]  # List of DataFrames
x_timestamp_list = [x_ts1, x_ts2, x_ts3]  # List of historical timestamps
y_timestamp_list = [y_ts1, y_ts2, y_ts3]  # List of future timestamps

# Generate batch predictions
pred_df_list = predictor.predict_batch(
    df_list=df_list,
    x_timestamp_list=x_timestamp_list,
    y_timestamp_list=y_timestamp_list,
    pred_len=pred_len,
    T=1.0,
    top_p=0.9,
    sample_count=1,
    verbose=True
)

# pred_df_list contains prediction results in the same order as input
for i, pred_df in enumerate(pred_df_list):
    print(f"Predictions for series {i}:")
    print(pred_df.head())
```

**Important Requirements for Batch Prediction:**
- All series must have the same historical length (lookback window)
- All series must have the same prediction length (`pred_len`)
- Each DataFrame must contain the required columns: `['open', 'high', 'low', 'close']`
- `volume` and `amount` columns are optional and will be filled with zeros if missing

The `predict_batch` method leverages GPU parallelism for efficient processing and automatically handles normalization and denormalization for each series independently.

#### 5. Example and Visualization

For a complete, runnable script that includes data loading, prediction, and plotting, please see [`examples/prediction_example.py`](examples/prediction_example.py).

Running this script will generate a plot comparing the ground truth data against the model's forecast, similar to the one shown below:

<p align="center">
    <img src="figures/prediction_example.png" alt="Forecast Example" align="center" width="600px" />
</p>

Additionally, we provide a script that makes predictions without Volume and Amount data, which can be found in [`examples/prediction_wo_vol_example.py`](examples/prediction_wo_vol_example.py).


## 🔧 Finetuning on Your Own Data (A-Share Market Example)

We provide a complete pipeline for finetuning Kronos on your own datasets. As an example, we demonstrate how to use

# FILE: examples/get_akshare_date_2024-2025_x.py

import pandas as pd
import requests
import json
from datetime import datetime, timedelta
import os
import time
import random


def get_stock_market(stock_code):
    """
    根据股票代码判断市场类型
    返回: 市场前缀 '0'-深交所, '1'-上交所
    """
    if stock_code.startswith(('0', '2', '3')):
        return '0'  # 深交所
    elif stock_code.startswith(('6', '9')):
        return '1'  # 上交所
    else:
        return '1'  # 默认上交所


def get_stock_data_eastmoney(stock_code="002354", start_year=2024, end_year=2025):
    """
    使用东方财富网API获取指定年份范围的股票数据 - 修复版
    """
    try:
        print(f"正在从东方财富网获取股票 {stock_code} 的 {start_year}-{end_year} 年数据...")

        # 计算日期范围
        start_date = f"{start_year}0101"
        current_date = datetime.now()

        if current_date.year > end_year:
            end_date = f"{end_year}1231"
        else:
            end_date = current_date.strftime('%Y%m%d')

        print(f"时间范围: {start_date} 到 {end_date}")

        # 获取市场类型
        market = get_stock_market(stock_code)
        secid = f"{market}.{stock_code}"

        # 使用更简单的东方财富API
        url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"

        params = {
            'secid': secid,
            'fields1': 'f1,f2,f3,f4,f5,f6',
            'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
            'klt': '101',  # 日线
            'fqt': '1',    # 前复权
            'beg': start_date,
            'end': end_date,
            'lmt': '10000',
            'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
            'cb': f'jQuery{random.randint(1000000, 9999999)}_{int(time.time()*1000)}'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'Referer': 'https://quote.eastmoney.com/',
            'Accept': '*/*',
        }

        time.sleep(random.uniform(1, 2))

        response = requests.get(url, params=params, headers=headers, timeout=10)

        print(f"API响应状态码: {response.status_code}")

        if response.status_code == 200:
            # 处理JSONP响应
            response_text = response.text

            # 提取JSON数据（处理JSONP格式）
            if response_text.startswith('/**/'):
                response_text = response_text[4:]

            # 查找JSON数据的开始和结束位置
            start_idx = response_text.find('(')
            end_idx = response_text.rfind(')')

            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx + 1:end_idx]
                try:
                    data = json.loads(json_str)
                except json.JSONDecodeError:
                    print("❌ JSON解析失败，尝试直接解析...")
                    # 如果JSON解析失败，尝试直接提取数据
                    return parse_kline_data_directly(response_text, stock_code, start_year, end_year)
            else:
                print("❌ 无法找到JSON数据边界")
                return None

            print(f"API返回数据状态: {data.get('rc', 'N/A')}")

            if data and data.get('data') i

# FILE: examples/prediction_new.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from datetime import datetime, timedelta
import warnings
import requests
import json
import time
import random
import akshare as ak
from typing import Dict, List, Tuple, Optional

warnings.filterwarnings('ignore')

# 添加项目路径以便导入自定义模块
sys.path.append("../")
try:
    from model import Kronos, KronosTokenizer, KronosPredictor
except ImportError:
    print("⚠️ 无法导入Kronos模型，预测功能将不可用")

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# ==================== 基础数据获取函数 ====================
def ensure_output_directory(output_dir):
    """确保输出目录存在，如果不存在则创建"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ 创建输出目录: {output_dir}")
    return output_dir


def fetch_real_stock_data(stock_code, period="daily", adjust="qfq"):
    """
    使用AKShare获取真实股票数据
    """
    try:
        print(f"📡 正在通过AKShare获取 {stock_code} 的真实股票数据...")

        # 获取股票数据
        df = ak.stock_zh_a_hist(symbol=stock_code, period=period, adjust=adjust)

        if df is None or df.empty:
            print(f"❌ 未获取到 {stock_code} 的数据")
            return None

        # 重命名列以统一格式
        column_mapping = {
            '日期': 'timestamps',
            '开盘': 'open',
            '收盘': 'close',
            '最高': 'high',
            '最低': 'low',
            '成交量': 'volume',
            '成交额': 'amount',
            '振幅': 'amplitude',
            '涨跌幅': 'pct_chg',
            '涨跌额': 'change_amount',
            '换手率': 'turnover'
        }

        # 只映射存在的列
        actual_mapping = {k: v for k, v in column_mapping.items() if k in df.columns}
        df = df.rename(columns=actual_mapping)

        # 确保时间戳格式正确
        df['timestamps'] = pd.to_datetime(df['timestamps'])
        df = df.sort_values('timestamps').reset_index(drop=True)

        # 添加股票代码列
        df['stock_code'] = stock_code

        print(f"✅ 成功获取 {len(df)} 条真实数据")
        print(f"📈 最新收盘价: {df['close'].iloc[-1]:.2f}元, 涨跌幅: {df['pct_chg'].iloc[-1]:.2f}%")
        print(f"📅 时间范围: {df['timestamps'].min()} 到 {df['timestamps'].max()}")

        return df

    except Exception as e:
        print(f"❌ AKShare数据获取失败: {e}")
        return None


def get_stock_data_with_retry_all_history(stock_code="600580", retry_count=2):
    """
    优化的数据获取函数 - 优先使用真实API数据
    """
    print(f"🔄 尝试获取股票 {stock_code} 的真实历史数据...")

    # 优先使用AKShare获取真实数据
    df = fetch_real_stock_data(stock_code, "daily", "qfq")

    if df is not None:
        return df
    else:
        print("⚠️ 真实数据获取失败，使用基于真实价格的模拟数据...")
        return create_realistic_fallback_data(stock_code)


def create_realistic_fallback_data(stock_code="600580"):
    """
    基于真实价格的备用数据生成函数
    """
    # 基于真实市场价格的参考数据
    real_stock_references = {
        '600580': {'name': '卧龙电驱', 'current_price': 15.20, 'range': (12.0, 20.0)},
        '300207': {'name': '欣旺达', 'current_price': 33.79, 'range': (28.0

# FILE: examples/prediction_example.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
from model import Kronos, KronosTokenizer, KronosPredictor


def plot_prediction(kline_df, pred_df):
    pred_df.index = kline_df.index[-pred_df.shape[0]:]
    sr_close = kline_df['close']
    sr_pred_close = pred_df['close']
    sr_close.name = 'Ground Truth'
    sr_pred_close.name = "Prediction"

    sr_volume = kline_df['volume']
    sr_pred_volume = pred_df['volume']
    sr_volume.name = 'Ground Truth'
    sr_pred_volume.name = "Prediction"

    close_df = pd.concat([sr_close, sr_pred_close], axis=1)
    volume_df = pd.concat([sr_volume, sr_pred_volume], axis=1)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax1.plot(close_df['Ground Truth'], label='Ground Truth', color='blue', linewidth=1.5)
    ax1.plot(close_df['Prediction'], label='Prediction', color='red', linewidth=1.5)
    ax1.set_ylabel('Close Price', fontsize=14)
    ax1.legend(loc='lower left', fontsize=12)
    ax1.grid(True)

    ax2.plot(volume_df['Ground Truth'], label='Ground Truth', color='blue', linewidth=1.5)
    ax2.plot(volume_df['Prediction'], label='Prediction', color='red', linewidth=1.5)
    ax2.set_ylabel('Volume', fontsize=14)
    ax2.legend(loc='upper left', fontsize=12)
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


# 1. Load Model and Tokenizer
tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = Kronos.from_pretrained("NeoQuasar/Kronos-small")

# 2. Instantiate Predictor
predictor = KronosPredictor(model, tokenizer, max_context=512)

# 3. Prepare Data
df = pd.read_csv("./data/XSHG_5min_600977.csv")
df['timestamps'] = pd.to_datetime(df['timestamps'])

lookback = 400
pred_len = 120

x_df = df.loc[:lookback-1, ['open', 'high', 'low', 'close', 'volume', 'amount']]
x_timestamp = df.loc[:lookback-1, 'timestamps']
y_timestamp = df.loc[lookback:lookback+pred_len-1, 'timestamps']

# 4. Make Prediction
pred_df = predictor.predict(
    df=x_df,
    x_timestamp=x_timestamp,
    y_timestamp=y_timestamp,
    pred_len=pred_len,
    T=1.0,
    top_p=0.9,
    sample_count=1,
    verbose=True
)

# 5. Visualize Results
print("Forecasted Data Head:")
print(pred_df.head())

# Combine historical and forecasted data for plotting
kline_df = df.loc[:lookback+pred_len-1]

# visualize
plot_prediction(kline_df, pred_df)



# FILE: examples/prediction_batch_example.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
from model import Kronos, KronosTokenizer, KronosPredictor


def plot_prediction(kline_df, pred_df):
    pred_df.index = kline_df.index[-pred_df.shape[0]:]
    sr_close = kline_df['close']
    sr_pred_close = pred_df['close']
    sr_close.name = 'Ground Truth'
    sr_pred_close.name = "Prediction"

    sr_volume = kline_df['volume']
    sr_pred_volume = pred_df['volume']
    sr_volume.name = 'Ground Truth'
    sr_pred_volume.name = "Prediction"

    close_df = pd.concat([sr_close, sr_pred_close], axis=1)
    volume_df = pd.concat([sr_volume, sr_pred_volume], axis=1)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax1.plot(close_df['Ground Truth'], label='Ground Truth', color='blue', linewidth=1.5)
    ax1.plot(close_df['Prediction'], label='Prediction', color='red', linewidth=1.5)
    ax1.set_ylabel('Close Price', fontsize=14)
    ax1.legend(loc='lower left', fontsize=12)
    ax1.grid(True)

    ax2.plot(volume_df['Ground Truth'], label='Ground Truth', color='blue', linewidth=1.5)
    ax2.plot(volume_df['Prediction'], label='Prediction', color='red', linewidth=1.5)
    ax2.set_ylabel('Volume', fontsize=14)
    ax2.legend(loc='upper left', fontsize=12)
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


# 1. Load Model and Tokenizer
tokenizer = KronosTokenizer.from_pretrained('/home/csc/huggingface/Kronos-Tokenizer-base/')
model = Kronos.from_pretrained("/home/csc/huggingface/Kronos-base/")

# 2. Instantiate Predictor
predictor = KronosPredictor(model, tokenizer, device="cuda:0", max_context=512)

# 3. Prepare Data
df = pd.read_csv("./data/XSHG_5min_600977.csv")
df['timestamps'] = pd.to_datetime(df['timestamps'])

lookback = 400
pred_len = 120

dfs = []
xtsp = []
ytsp = []
for i in range(5):
    idf = df.loc[(i*400):(i*400+lookback-1), ['open', 'high', 'low', 'close', 'volume', 'amount']]
    i_x_timestamp = df.loc[(i*400):(i*400+lookback-1), 'timestamps']
    i_y_timestamp = df.loc[(i*400+lookback):(i*400+lookback+pred_len-1), 'timestamps']

    dfs.append(idf)
    xtsp.append(i_x_timestamp)
    ytsp.append(i_y_timestamp)

pred_df = predictor.predict_batch(
    df_list=dfs,
    x_timestamp_list=xtsp,
    y_timestamp_list=ytsp,
    pred_len=pred_len,
)


# FILE: examples/prediction_new_GUI.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from datetime import datetime, timedelta
import warnings
import requests
import json
import time
import random
import akshare as ak
from typing import Dict, List, Tuple, Optional
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

warnings.filterwarnings('ignore')

# 添加项目路径以便导入自定义模块
sys.path.append("../")
try:
    from model import Kronos, KronosTokenizer, KronosPredictor
except ImportError:
    print("⚠️ 无法导入Kronos模型，预测功能将不可用")

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class StockPredictorGUI:
    """股票预测图形界面"""

    def __init__(self, root):
        self.root = root
        self.root.title("Kronos股票预测系统")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        # 初始化市场分析器
        self.market_analyzer = EnhancedMarketFactorAnalyzer()

        # 创建界面
        self.create_widgets()

        # 默认配置
        self.default_config = {
            "stock_code": "600580",
            "stock_name": "卧龙电驱",
            "data_dir": r"D:\lianghuajiaoyi\Kronos\examples\data",
            "output_dir": r"D:\lianghuajiaoyi\Kronos\examples\yuce",
            "pred_days": 60,
            "history_years": 1
        }

    def create_widgets(self):
        """创建界面组件"""
        # 主标题
        title_label = tk.Label(
            self.root,
            text="🤖 Kronos股票预测系统",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=10)

        # 说明标签
        desc_label = tk.Label(
            self.root,
            text="基于Kronos模型的多维度股票价格预测系统",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        desc_label.pack(pady=5)

        # 创建主框架
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # 输入框架
        input_frame = tk.LabelFrame(main_frame, text="股票参数设置", font=("Arial", 11, "bold"),
                                    bg='#f0f0f0', fg='#2c3e50')
        input_frame.pack(fill=tk.X, pady=10)

        # 股票代码输入
        tk.Label(input_frame, text="股票代码:", bg='#f0f0f0', font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W,
                                                                                       padx=5, pady=5)
        self.stock_code_var = tk.StringVar(value="600580")
        stock_code_entry = tk.Entry(input_frame, textvariable=self.stock_code_var, font=("Arial", 10), width=15)
        stock_code_entry.grid(row=0, column=1, padx=5, pady=5)

        # 股票名称输入
        tk.Label(input_frame, text="股票名称:", bg='#f0f0f0', font=("Arial", 10)).grid(row=0, column=2, sticky=tk.W,
                       

# FILE: examples/get_date_new.py

import pandas as pd
import requests
import json
from datetime import datetime, timedelta
import os
import time
import random


def get_stock_market(stock_code):
    """
    根据股票代码判断市场类型
    返回: 市场前缀 '0'-深交所, '1'-上交所
    """
    if stock_code.startswith(('0', '2', '3')):
        return '0'  # 深交所
    elif stock_code.startswith(('6', '9')):
        return '1'  # 上交所
    else:
        return '1'  # 默认上交所


def get_stock_data_eastmoney_all_history(stock_code="002354"):
    """
    使用东方财富网API获取股票所有历史数据
    """
    try:
        print(f"正在从东方财富网获取股票 {stock_code} 的全部历史数据...")

        # 获取市场类型
        market = get_stock_market(stock_code)
        secid = f"{market}.{stock_code}"

        # 使用东方财富API获取所有历史数据
        url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"

        # 设置足够早的起始日期（中国股市从1990年开始）
        start_date = "19900101"
        end_date = datetime.now().strftime('%Y%m%d')

        params = {
            'secid': secid,
            'fields1': 'f1,f2,f3,f4,f5,f6',
            'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
            'klt': '101',  # 日线
            'fqt': '1',  # 前复权
            'beg': start_date,
            'end': end_date,
            'lmt': '50000',  # 增加限制数量以获取更多历史数据
            'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
            'cb': f'jQuery{random.randint(1000000, 9999999)}_{int(time.time() * 1000)}'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'Referer': 'https://quote.eastmoney.com/',
            'Accept': '*/*',
        }

        time.sleep(random.uniform(1, 2))

        response = requests.get(url, params=params, headers=headers, timeout=15)

        print(f"API响应状态码: {response.status_code}")

        if response.status_code == 200:
            # 处理JSONP响应
            response_text = response.text

            # 提取JSON数据（处理JSONP格式）
            if response_text.startswith('/**/'):
                response_text = response_text[4:]

            # 查找JSON数据的开始和结束位置
            start_idx = response_text.find('(')
            end_idx = response_text.rfind(')')

            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx + 1:end_idx]
                try:
                    data = json.loads(json_str)
                except json.JSONDecodeError:
                    print("❌ JSON解析失败，尝试直接解析...")
                    return parse_kline_data_directly_all_history(response_text, stock_code)
            else:
                print("❌ 无法找到JSON数据边界")
                return None

            print(f"API返回数据状态: {data.get('rc', 'N/A')}")

            if data and data.get('data') is not None:
                klines = data['data'].get('klines', [])
                print(f"获取到 {len(klines)} 条历史K线数据")

                if not klines:
                    print("⚠️ K线数据为空")
                    return None

                # 解析数据
            

# FILE: examples/prediction_akshare_2024-2025.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

# 添加项目路径以便导入自定义模块
sys.path.append("../")
from model import Kronos, KronosTokenizer, KronosPredictor

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def ensure_output_directory(output_dir):
    """确保输出目录存在，如果不存在则创建"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ 创建输出目录: {output_dir}")
    return output_dir


def prepare_stock_data(csv_file_path, stock_code):
    """
    准备股票数据，转换为Kronos模型需要的格式

    参数:
    csv_file_path: CSV文件路径
    stock_code: 股票代码，用于显示信息

    返回:
    df: 处理后的DataFrame
    """
    print(f"正在加载和预处理股票 {stock_code} 数据...")

    # 读取CSV文件
    df = pd.read_csv(csv_file_path, encoding='utf-8-sig')

    # 检查数据列名并重命名为标准格式
    column_mapping = {
        '日期': 'timestamps',
        '开盘价': 'open',
        '最高价': 'high',
        '最低价': 'low',
        '收盘价': 'close',
        '成交量': 'volume',
        '成交额': 'amount'
    }

    # 只重命名存在的列
    actual_mapping = {k: v for k, v in column_mapping.items() if k in df.columns}
    df = df.rename(columns=actual_mapping)

    # 确保时间戳列存在并转换为datetime格式
    if 'timestamps' not in df.columns:
        # 如果数据有日期索引，重置索引
        if df.index.name == '日期':
            df = df.reset_index()
            df = df.rename(columns={'日期': 'timestamps'})

    df['timestamps'] = pd.to_datetime(df['timestamps'])

    # 按时间排序
    df = df.sort_values('timestamps').reset_index(drop=True)

    print(f"✅ 数据加载完成，共 {len(df)} 条记录")
    print(f"时间范围: {df['timestamps'].min()} 到 {df['timestamps'].max()}")
    print(f"数据列: {df.columns.tolist()}")

    return df


def calculate_prediction_parameters(df, target_days=100):
    """
    根据目标预测天数计算合适的参数

    参数:
    df: 股票数据DataFrame
    target_days: 目标预测天数（自然日）

    返回:
    lookback: 回看期数
    pred_len: 预测期数
    """
    # 计算平均交易日数量（考虑节假日）
    total_days = (df['timestamps'].max() - df['timestamps'].min()).days
    trading_days = len(df)
    trading_ratio = trading_days / total_days if total_days > 0 else 0.7  # 交易日比例

    # 计算目标预测的交易日数量
    pred_trading_days = int(target_days * trading_ratio)

    # 设置回看期数为预测期数的2-3倍，但不超过数据总量的70%
    max_lookback = int(len(df) * 0.7)
    lookback = min(pred_trading_days * 2, max_lookback, len(df) - pred_trading_days)
    pred_len = min(pred_trading_days, len(df) - lookback)

    print(f"📊 参数计算:")
    print(f"  目标预测天数: {target_days} 天（自然日）")
    print(f"  预计交易日数量: {pred_trading_days} 天")
    print(f"  回看期数 (lookback): {lookback}")
    print(f"  预测期数 (pred_len): {pred_len}")

    return lookback, pred_len


def generate_future_dates_with_holidays(last_date, pred_len):
    """
    生成未来的交易日日期，考虑中国节假日

    参数:
    last_date: 最后一个历史数据的日期
    pred_len: 预测期数

    返回:
    future_dates: 未来的交易日日期列表
    """
    # 中国主要节假日（需要根据实际情况调整）
    holidays_2025 = [
        # 2025年国庆

# FILE: examples/run_backtest_kronos.py

# run_backtest.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class KronosBacktester:
    """
    Kronos模型回测类
    """

    def __init__(self, data_dir, model_dir, initial_capital=100000):
        """
        初始化回测器

        参数:
        data_dir: 数据目录
        model_dir: 模型预测结果目录
        initial_capital: 初始资金
        """
        self.data_dir = data_dir
        self.model_dir = model_dir
        self.initial_capital = initial_capital
        self.results = {}

    def load_historical_data(self, stock_code):
        """
        加载历史数据
        """
        csv_file = os.path.join(self.data_dir, f"{stock_code}_stock_data.csv")
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"数据文件不存在: {csv_file}")

        df = pd.read_csv(csv_file, encoding='utf-8-sig')

        # 检查列名并标准化
        column_mapping = {
            '日期': 'date',
            '开盘价': 'open',
            '最高价': 'high',
            '最低价': 'low',
            '收盘价': 'close',
            '成交量': 'volume',
            '成交额': 'amount'
        }

        # 重命名列
        for old_col, new_col in column_mapping.items():
            if old_col in df.columns:
                df = df.rename(columns={old_col: new_col})

        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        df = df.sort_index()

        print(f"✅ 加载历史数据: {len(df)} 条记录")
        print(f"时间范围: {df.index.min()} 到 {df.index.max()}")

        return df

    def load_predictions(self, stock_code):
        """
        加载模型预测结果
        """
        # 尝试不同的预测文件命名
        pred_files = [
            os.path.join(self.model_dir, f"{stock_code}_kronos_predictions.csv"),
            os.path.join(self.model_dir, f"{stock_code}_detailed_predictions.csv"),
            os.path.join(self.model_dir, f"{stock_code}_predictions.csv")
        ]

        pred_df = None
        for pred_file in pred_files:
            if os.path.exists(pred_file):
                pred_df = pd.read_csv(pred_file, encoding='utf-8-sig')
                print(f"✅ 找到预测文件: {pred_file}")
                break

        if pred_df is None:
            raise FileNotFoundError(f"未找到预测文件，请检查目录: {self.model_dir}")

        # 标准化列名
        column_mapping = {
            '日期': 'date',
            '预测收盘价': 'predicted_close',
            '收盘价': 'predicted_close',
            '预测成交量': 'predicted_volume',
            '成交量': 'predicted_volume'
        }

        for old_col, new_col in column_mapping.items():
            if old_col in pred_df.columns:
                pred_df = pred_df.rename(columns={old_col: new_col})

        pred_df['date'] = pd.to_datetime(pred_df['date'])
        pred_df.set_index('date', inplace=True)
        pred_df = pred_df.sort_index()

        print(f"✅ 加载预测数据: {len(pred_df)} 条记录
