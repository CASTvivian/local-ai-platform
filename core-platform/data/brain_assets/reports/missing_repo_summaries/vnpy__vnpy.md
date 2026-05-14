# Missing Repo Summary Source: vnpy/vnpy

- URL: https://github.com/vnpy/vnpy
- Local Path: vnpy
- Clone Status: local_existing
- Language: Python
- Stars: 40442
- Topics: algotrading, finance, fintech, investment, python, quant, trading, vnpy
- Description: 基于Python的开源量化交易平台开发框架

## Extracted README / Docs / Examples


# FILE: README_ENG.md

# VeighNa - By Traders, For Traders, AI-Powered.

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/veighna-logo.png"/>
</p>

💬 Want to read this in **chinese** ? Go [**here**](README.md)

<p align="center">
    <img src ="https://img.shields.io/badge/version-4.3.0-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.10|3.11|3.12|3.13-blue.svg" />
    <img src ="https://img.shields.io/github/actions/workflow/status/vnpy/vnpy/pythonapp.yml?branch=master"/>
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

VeighNa is a Python-based open source quantitative trading system development framework that has grown step by step into a fully-featured quantitative trading platform with continuous contributions from the open source community. It currently has many users from domestic and international financial institutions, including hedge funds, investment banks, futures brokers, university research institutions, proprietary trading companies, etc.

If you have any questions about using VeighNa for secondary development (strategies, modules, etc.), please check the [**VeighNa Project Documentation**](https://www.vnpy.com/docs/cn/index.html). If you can't solve it, please go to the [Questions and Help] section of the [**Official Community Forum**](https://www.vnpy.com/forum/) for help, or share your experience in the [Experience Sharing] section!

**Want to get more information about VeighNa?** Please scan the QR code below to add the assistant and join the [VeighNa Community Exchange WeChat Group]:

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/github_wx.png"/, width=250>
</p>


## AI-Powered

On the tenth anniversary of VeighNa's release, version 4.0 officially introduces the [vnpy.alpha](./vnpy/alpha) module targeting AI quantitative strategies, providing professional quantitative traders with **an all-in-one multi-factor machine learning (ML) strategy development, research, and live trading solution**:

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/alpha_demo.jpg"/, width=500>
</p>

* :bar_chart: **[dataset](./vnpy/alpha/dataset)**: Factor Feature Engineering

    * Designed specifically for ML algorithm training optimization, supporting efficient batch feature calculation and processing
    * Built-in rich factor feature expression calculation engine, enabling rapid one-click generation of training data
    * [Alpha 158](./vnpy/alpha/dataset/datasets/alpha_158.py): A collection of stock market features from Microsoft's Qlib project, covering multiple dimensions of quantitative factors including K-line patterns, price trends, and time-series volatility

* :bulb: **[model](./vnpy/alpha/model)**: Prediction Model Training

    * Provides standardized ML model development templates, greatly simplifying model building and training processes
    * Unified API interface design, supporting seamless switching between different algorithms for performance comparison testing
    * Integrates multiple mainstream machine learning algorithms:
        * [Lasso](./vnpy/alpha/model/models/lasso_model.py): Classic Lasso regression model, implementing feature selection through L1 regularization
        * [LightGBM](./vnpy/alpha/model/models/lgb_model.py): Efficient gradient boosting decision tree with a training engine optimized for large-scale datasets
        * [MLP](./vnpy/alpha/model/models/mlp_model.py): Multi-layer perceptron neural network, suitable for modeling complex non-linear relationships

* :robot: **[strategy](./vnpy/alpha/strategy)**: Strategy Research and Development

    * Quickly build quantitative trading strategies based on ML signal prediction models
    * Support for both cross-sectional multi-asset and time-series single-asset strategy types

* :microscope: **[lab](./vnpy/alpha/lab.py)**: Research Process Management

    * Integrates complete workflow including data management, model training, signal generation, and strategy backtesting
    * Simple API design with built-in visualization analysis tools for intuitive evaluation of strategy performance and model effectiveness

* :book: **[notebook](./examples/alpha_research)**: Quantitative Research Demo

    * [download_data_rq](./examples/alpha_research/download_data_rq.ipynb): Download A-share index constituent stock data based on RQData, including index constituent tracking and historical market data retrieval
    * [download_data_xt](./examples/alpha_research/download_data_xt.ipynb): Download A-share index constituent historical changes and stock K-line data based on XtQuant data service
    * [research_workflow_lasso](./examples/alpha_research/research_workflow_lasso.ipynb): Quantitative research workflow based on Lasso regression model, demonstrating feature selection and prediction capability of linear models
    * [research_workflow_lgb](./examples/alpha_research/research_workflow_lgb.ipynb): Quantitative research workflow based on LightGBM gradient boosting tree, utilizing efficient ensemble learning methods for prediction
    * [research_workflow_mlp](./examples/alpha_research/research_workflow_mlp.ipynb): Quantitative research workflow based on multilayer perceptron neural network, demonstrating the application of deep learning in quantitative trading

The design concept of the vnpy.alpha module was inspired by the [Qlib](https://github.com/microsoft/qlib) project, providing powerful AI quantitative capabilities while maintaining ease of use. We would like to express our sincere gratitude to the Qlib development team!


## Functional Features

Modules marked with :arrow_up: have completed the upgrade compatibility testing for version 4.0. Additionally, the 4.0 core framework uses an upgrade approach that prioritizes compatibility, so most modules can also be used directly (interfaces involving C++ API encapsula


# FILE: README.md

# VeighNa - By Traders, For Traders, AI-Powered.

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/veighna-logo.png"/>
</p>

💬 Want to read this in **english** ? Go [**here**](README_ENG.md)

<p align="center">
    <img src ="https://img.shields.io/badge/version-4.3.0-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.10|3.11|3.12|3.13-blue.svg" />
    <img src ="https://img.shields.io/github/actions/workflow/status/vnpy/vnpy/pythonapp.yml?branch=master"/>
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

VeighNa是一套基于Python的开源量化交易系统开发框架，在开源社区持续不断的贡献下一步步成长为多功能量化交易平台，自发布以来已经积累了众多来自金融机构或相关领域的用户，包括私募基金、证券公司、期货公司等。

在使用VeighNa进行二次开发（策略、模块等）的过程中有任何疑问，请查看[**VeighNa项目文档**](https://www.vnpy.com/docs/cn/index.html)，如果无法解决请前往[**官方社区论坛**](https://www.vnpy.com/forum/)的【提问求助】板块寻求帮助，也欢迎在【经验分享】板块分享你的使用心得！

**想要获取更多关于VeighNa的资讯信息？** 请扫描下方二维码添加小助手加入【VeighNa社区交流微信群】：

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/github_wx.png"/, width=250>
</p>


## AI-Powered


VeighNa发布十周年之际正式推出4.0版本，重磅新增面向AI量化策略的[vnpy.alpha](./vnpy/alpha)模块，为专业量化交易员提供**一站式多因子机器学习（ML）策略开发、投研和实盘交易解决方案**：

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/alpha_demo.jpg"/, width=500>
</p>

* :bar_chart: **[dataset](./vnpy/alpha/dataset)**：因子特征工程

    * 专为ML算法训练优化设计，支持高效批量特征计算与处理
    * 内置丰富的因子特征表达式计算引擎，实现快速一键生成训练数据
    * [Alpha 158](./vnpy/alpha/dataset/datasets/alpha_158.py)：源于微软Qlib项目的股票市场特征集合，涵盖K线形态、价格趋势、时序波动等多维度量化因子

* :bulb: **[model](./vnpy/alpha/model)**：预测模型训练

    * 提供标准化的ML模型开发模板，大幅简化模型构建与训练流程
    * 统一API接口设计，支持无缝切换不同算法进行性能对比测试
    * 集成多种主流机器学习算法：
        * [Lasso](./vnpy/alpha/model/models/lasso_model.py)：经典Lasso回归模型，通过L1正则化实现特征选择
        * [LightGBM](./vnpy/alpha/model/models/lgb_model.py)：高效梯度提升决策树，针对大规模数据集优化的训练引擎
        * [MLP](./vnpy/alpha/model/models/mlp_model.py)：多层感知机神经网络，适用于复杂非线性关系建模

* :robot: **[strategy](./vnpy/alpha/strategy)**：策略投研开发

    * 基于ML信号预测模型快速构建量化交易策略
    * 支持截面多标的和时序单标的两种策略类型

* :microscope: **[lab](./vnpy/alpha/lab.py)**：投研流程管理

    * 集成数据管理、模型训练、信号生成和策略回测等完整工作流程
    * 简洁API设计，内置可视化分析工具，直观评估策略表现和模型效果

* :book: **[notebook](./examples/alpha_research)**：量化投研Demo

    * [download_data_rq](./examples/alpha_research/download_data_rq.ipynb)：基于RQData下载A股指数成分股数据，包含指数成分变化跟踪及历史行情获取
    * [download_data_xt](./examples/alpha_research/download_data_xt.ipynb)：基于迅投研数据服务，下载获取A股指数成分历史变化和股票K线数据
    * [research_workflow_lasso](./examples/alpha_research/research_workflow_lasso.ipynb)：基于Lasso回归模型的量化投研工作流，展示线性模型特征选择与预测能力
    * [research_workflow_lgb](./examples/alpha_research/research_workflow_lgb.ipynb)：基于LightGBM梯度提升树的量化投研工作流，利用高效集成学习方法进行预测
    * [research_workflow_mlp](./examples/alpha_research/research_workflow_mlp.ipynb)：基于多层感知机神经网络的量化投研工作流，展示深度学习在量化交易中的应用

vnpy.alpha模块的设计理念受到[Qlib](https://github.com/microsoft/qlib)项目的启发，在保持易用性的同时提供强大的AI量化能力，特此向Qlib开发团队致以诚挚感谢！


## 功能特点

带有 :arrow_up: 的模块代表已经完成4.0版本的升级适配测试，同时4.0核心框架采用了优先保证兼容性的升级方式，因此大多数模块也都可以直接使用（涉及到C++ API封装的接口必须升级后才能使用）。 

1. :arrow_up: 多功能量化交易平台（trader），整合了多种交易接口，并针对具体策略算法和功能开发提供了简洁易用的API，用于快速构建交易员所需的量化交易应用。

2. 覆盖国内外所拥有的下述交易品种的交易接口（gateway）：

    * 国内市场

        * :arrow_up: CTP（[ctp](https://www.github.com/vnpy/vnpy_ctp)）：国内期货、期权

        * :arrow_up: CTP Mini（[mini](https://www.github.com/vnpy/vnpy_mini)）：国内期货、期权

        * :arrow_up: CTP证券（[sopt](https://www.github.com/vnpy/vnpy_sopt)）：ETF期权

        * :arrow_up: 飞马（[femas](https://www.github.com/vnpy/vnpy_femas)）：国内期货

        * :arrow_up: 恒生UFT（[uft](https://www.github.com/vnpy/vnpy_uft)）：国内期货、ETF期权

        * :arrow_up: 易盛（[esunny](https://www.github.com/vnpy/vnpy_esunny)）：国内期货、黄金TD

        * :arrow_up: 顶点HTS（[hts](https://www.github.com/vnpy/vnpy_hts)）：ETF期权

        * :arrow_up: 顶点飞创（[sec](https://www.github.com/vnpy/vnpy_sec)）：ETF期权

        * :arrow_up: 中泰XTP（[xtp](https://www.github.com/vnpy/vnpy_xtp)）：国内证券（A股）、ETF期权

        * :arrow_up: 华鑫奇点（[tora](https://www.github.com/vnpy/vnpy_tora)）：国内证券（A股）、ETF期权

        * 东证OST（[ost](https://www.github.com/vnpy/vnpy_ost)）：国内证券（A股）

        * 东方财富EMT（[emt](https://www.github.com/vnpy/vnpy_emt)）：国内证券（A股）

        * 飞鼠（[sgit](https://www.github.com/vnpy/vnpy_sgit)）：黄金TD、国内期货

        * :arrow_up: 金仕达黄金（[ksgold](https://www.github.com/vnpy/vnpy_ksgold)）：黄金TD

        * :arrow_up: 利星资管（[lstar](https://www.github.com/vnpy/vnpy_lstar)）：期货资管

        * :arrow_up: 融航（[rohon](https://www.github.com/vnpy/vnpy_rohon)）：期货资管

        * :arrow_up: 杰宜斯（[jees](https://www.github.com/vnpy/vnpy_jees)）：期货资管

        * 中汇亿达（[comstar](https://www.github.com/vnpy/vnpy_comstar)）：银行间市场

        * :arrow_up: TTS（[tts](https://www.github.com/vnpy/vnpy_tts)）：国内期货（仿真）

    * 海外市场

        * :arrow_up: Interactive Brokers（[ib](https://www.github.com/vnpy/vnpy_ib)）：海外证券、期货、期权、贵金属等

        * :arrow_up: 易盛9.0外盘（[tap](https://www.github.com/vnpy/vnpy_tap)）：海外期货

        * :arrow_up: 直达期货（[da](https://www.github.com/vnpy/vnpy_da)）：海外期货

    * 特殊应用

        * :arrow_up: RQData行情（[rqdata](https://www.github.com/vnpy/vnpy_rqdata)）：跨市场（股票、指数、ETF、期货）实时行情

        * :arrow_up: 迅投研行情（[xt](https://www.github.com/vnpy/vnpy_xt)）：跨市场（股票、指数、可转债、ETF、期货、期权）实时行情

        * :arrow_up: RPC服务（[rpc](https://www.github.com/vnpy/vnpy_rpcservice)）：跨进程通讯接口，用于分布式架构

3. 覆盖下述各类量化策略的交易应用（app）：

    * :arrow_up: [cta_strategy](https://www.github.com/vnpy/vnpy_ctastrategy)：CTA策略引擎模块，在保持易用性的同时，允许用户针对CTA类策略运行过程中委托的报撤行为进行细粒度控制（降低交易滑点、实现高频策略）

    * :arrow_up: [cta_backtester](https://www.github.com/vnpy/vnpy_ctabacktester)：CTA策略回测模块，无需使用Jupyter Notebook，直接使用图形界面进行策略回测分析、参数优化等相关工作

    * :arrow_up: [spread_trading](https://www.github.com/vnpy/vnpy_spreadtrading)：价差交易模块，支持自定义价差，实时计算价差行情和持仓，支持价差算法交易以及自动价差策略两种模式

    * :arrow_up: [option_master](https://www.github.com/vnpy/vnpy_optionmaster)：期权交易模块，针对国内期权市场设计，支持多种期权定价模型、隐含波动率曲面计算、希腊值风险跟踪等功能

    * :arrow_up: [portfolio_strategy](https://www.github.com/vnpy/vn


# FILE: docs/community/install/windows_install.md

# Windows安装指南

本文档中安装步骤适用的Windows系统包括：

- Windows 10/11
- Windows Server 2019

> 其他版本的Windows系统安装时可能遇到各种依赖库问题，不推荐使用。

在Windows系统上安装VeighNa，推荐使用官方推出的【VeighNa Studio Python发行版】，**尤其是初次接触Python的编程新手**。

作为一站式的量化投研交易Python环境，VeighNa Studio整合了：

- Python 3.10 64位（Python官网版本）
- VeighNa和其他相关依赖库
- VeighNa Station（VeighNa框架的图形化管理工具）

对于已经有比较丰富的编程经验或者需要用到特定Python发行版（如Anaconda）的用户，也可以采用手动安装的方案。


## VeighNa Studio方案

### 下载安装

在[VeighNa官网](https://www.vnpy.com/)可以下载VeighNa Studio安装包。

下载完成后，双击安装包进入VeighNa Studio安装向导（推荐点击右键，选择【使用管理员身份运行】进行安装），使用默认设置点击【快速安装】按钮即可进行VeighNa Studio安装，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/21.png)

> 推荐将VeighNa Studio安装在默认路径的C:\veighna_studio，其他VeighNa文档和教程中均使用该目录作为VeighNa安装目录进行讲解。

如果想进行个性化安装，可点击【自定义安装】进入高级选项页面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/24.png)

安装完成后，会转换到安装成功页面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/26.png)

此时桌面会出现VeighNa Station的图标，双击图标即可运行VeighNa Station。

### 使用

安装成功后，启动命令行工具即可直接使用VeighNa Studio Python发行版。

输入python即可进入python的交互式环境，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/29.png)

此时在命令行中输入python代码就会立即执行。如果想运行pyqtgraph的自带的例子，可以依次输入以下代码：

```python3
from pyqtgraph import examples
examples.run()
```

此时则会弹出Examples的运行窗口，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/30.png)

点击左侧的Basic Plotting则会弹出示例的图形界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/31.png)

如果想打开jupyter lab进行投资研究工作，可以打开cmd，输入jupyter lab，即可成功启动，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/32.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/38.png)

### 修改

如果安装之后，想要添加或者移除某项功能，可以双击VeighNa Studio的安装包，进入VeighNa Studio安装界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/33.png)

点击【修改】，进入修改页面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/35.png)

选择完可选功能后，点击【下一步】，进入高级选项页面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/37.png)

选择完毕，即可重新安装。

### 修复

如果安装之后，出现安装不完整或者其他需要修复的情况，可以双击VeighNa Studio的安装包，进入VeighNa Studio安装界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/33.png)

点击【修复】，进入修复界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/34.png)

修复完成后，会转换到修复成功页面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/15.png)

### 卸载

如果想卸载VeighNa Studio， 可以双击VeighNa Studio的安装包，进入VeighNa Studio安装界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/33.png)

点击【卸载】，进入卸载界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/27.png)

卸载完成后，会转换到卸载成功页面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/28.png)


## 手动安装方案

### 准备Python环境

首先请在电脑上准备好Python 3.10 64位环境（**注意必须是64位版本**），推荐使用Python官网的发行版，也可以使用Anaconda、Miniconda、Canopy等发行版。

这里我们以Python官网的发行版为例，首先在[Python官网](https://www.python.org/downloads/windows/)下载安装文件，选择【Windows installer (64-bit)】，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/22.png)

下载完毕后，双击文件进入Python安装向导，勾选【Add Python3.10 to PATH】选项后，点击【Install Now】进行安装，推荐使用默认设置一路点击【下一步】直到安装完成即可：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/23.png)


### 下载安装VeighNa  

下载VeighNa源代码（Windows系统请选择zip格式）：

- [VeighNa Github下载地址](https://github.com/vnpy/vnpy/releases)
- [VeighNa Gitee下载地址](https://gitee.com/mirrors/vn-py/releases)

下载完成后解压，然后启动命令行工具（CMD或者PowerShell），进入源代码所在的目录后（即install.bat文件所在的目录），输入下列命令运行脚本执行一键安装：

```
install.bat
```

一键安装过程整体分为3步：

1. 下载安装ta-lib库；
2. 安装VeighNa本身。

如果某一步安装过程中发生错误，请截取保存命令行中的报错信息（**注意优先保存底部的报错内容**），前往VeighNa社区论坛发帖提问寻求帮助。

### 启动VeighNa Trader

启动命令行工具，进入解压VeighNa源代码的目录下，在文件夹examples/veighna_trader中找到run.py文件。

输入如下命令即可启动VeighNa Trader：

```
python run.py 
```

请注意run.py中包含了较多的启动加载项（交易接口和应用模块），请根据自己所用的操作系统以及实际的交易需求修改调整使用（若需加载接口，取消接口前注释符号即可）。

连接接口介绍详见交易接口篇。

> 如果启动时出现一些库版本不兼容的情况，可根据提示对这些库重新pip安装。



# FILE: docs/community/install/mac_install.md

# Mac安装指南

## Mac系统的CTP接口支持

得益于Python语言本身的跨平台优势（Windows、Linux、Mac三大系统），VeighNa量化交易平台的核心框架部分很早就可以在Mac系统上运行。

但由于C++类交易API对于Mac系统支持的普遍不足，导致之前只有vnpy_ib等少数【纯Python实现】的交易接口可以在Mac系统上运行，对于大部分用户来说没什么实际价值。

从6.6.7版本的CTP API开始，上期技术官方推出了对Mac系统支持，包括Intel（x86_64）和苹果M系（arm64）芯片。终于，VeighNa平台可以在Mac系统上为期货量化用户提供从投研回测到实盘交易的一体化解决方案。


## Mac系统的VeighNa安装流程

目前Mac系统上还没有类似VeighNa Studio的开箱即用发行版，需要手动完成安装流程：

1. 前往Python官网下载3.10版本的安装包（或者使用brew安装），安装完成后在终端（Terminal）中运行命令：

```python3
python3
```
检查确认打开的Python解释器为3.10版本。

2. 使用brew安装TA-Lib的C++开发包：

```python3
brew install ta-lib
```

3. 安装NumPy和TA-Lib（Python），这里推荐使用豆瓣PyPI镜像解决官方源访问困难的问题：

```python3
python3 -m pip install numpy==1.26.4 --index=https://pypi.doubanio.com/simple
python3 -m pip install ta-lib --index=https://pypi.doubanio.com/simple
```

4. 安装米筐RQData客户端，注意这里使用的是米筐PyPI源：

```python3
python3 -m pip install rqdatac --index=https://pypi2.ricequant.com/simple
```

5. 安装VeighNa核心框架，以及需要使用的功能插件模块：


```python3
python3 -m pip install vnpy --index=https://pypi.doubanio.com/simple
python3 -m pip install vnpy_ctastrategy vnpy_ctabacktester vnpy_datamanager vnpy_sqlite vnpy_rqdata --index=https://pypi.doubanio.com/simple
```
这里的例子中包括（具体可以根据自己的需求调整）：

 - CTA策略实盘和回测模块：vnpy_ctastrategy、vnpy_ctabacktester
 - 历史数据管理模块：vnpy_datamanager
 - SQLite数据库驱动：vnpy_sqlite
 - RQData数据服务适配器：vnpy_rqdata

pip安装过程中如果出现报错某些依赖库的缺失，可以尝试先pip install该依赖库，然后再次执行上述安装命令。

6. 安装CTP交易接口模块：

由于6.7.2版本CTP的Mac系统API项目结构发生了较大变化，改为了使用framework目录的结构，因此无法再直接从PyPI下载预编译好的wheel二进制包进行安装。

用户需要克隆（或下载）本仓库的源代码到本地后（注意；克隆的源代码文件夹vnpy_ctp不要直接放在用户文件夹下，需要放在一个其的子文件下，否则会出现安装完成后无法识别该模块的情况，如下以在用户文件夹下新建一个名为github的文件夹为例）自行编译安装，具体命令如下：

```python3
mkdir github

cd github

git clone https://github.com/vnpy/vnpy_ctp.git

cd vnpy_ctp

pip3 install -e .
```

相关注意事项如下：

源码编译需要依赖XCode开发工具中的C++编译器，请务必先安装好。

编译过程中，会指定克隆到本地的源码目录中的framework文件夹路径，为API运行时动态库的加载路径。因此后续运行时，该源码目录不能删除，也不能移动位置，否则会导致动态库加载找不到的报错。

由于当前新版本Mac系统的安全机制，编译完成后需要在【访达】中找到下述两个动态库文件，分别手动打开一次后添加到操作系统信任名单，才能在启动Python时成功加载：

* vnpy_ctp/api/libs/thostmduserapi_se.framework/Versions/A/thostmduserapi_se
* vnpy_ctp/api/libs/thosttraderapi_se.framework/Versions/A/thosttraderapi_se

以上两个文件由于本身是二进制格式，并不能正常打开，但不影响添加到系统信任名单。

完成后即可使用run.py脚本启动VeighNa Trader，代码如下：

```python3
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy_ctp import CtpGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp
from vnpy_datamanager import DataManagerApp

def main():
    """Start VeighNa Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(DataManagerApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()

if __name__ == "__main__":
    main()
```



# FILE: docs/community/install/ubuntu_install.md

# Ubuntu安装指南

## 检查Python

检查本地Python版本，需要需要3.7版本以上的版本，可在命令行运行python命令查看。

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/40.png)


## 安装VeighNa

### 下载源代码

下载VeighNa源代码（Ubuntu系统请选择tar.gz格式）：

- [VeighNa Github下载地址](https://github.com/vnpy/vnpy/releases)
- [VeighNa Gitee下载地址](https://gitee.com/mirrors/vn-py/releases)

下载完成后用tar命令解压文件，如下图所示。

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/41.png)

### 执行一键安装

安装VeighNa前需要先安装gcc编译器，用于编译C++类接口文件。在终端中运行以下命令：

```
sudo apt-get update
sudo apt-get install build-essential
```

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/39.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/43.png)

然后进入之前解压出来的VeighNa源代码目录（包含install.sh文件）

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/42.png)

打开终端运行如下命令执行一键安装：

```
sudo bash install.sh
```

请注意，如果python软连接名不为python，比如python3或python3.10，请执行如下命令：

```
sudo bash install.sh 你的python软连接
```

一键安装过程整体分为3步：

1. 下载安装ta-lib库和numpy；
2. 安装VeighNa本身。

> 若是在虚拟机上运行，请把内存调至4G以上，否则会报错内存不足。


## 启动VeighNa Trader

进入解压VeighNa源代码的目录下，在文件夹examples/veighna_trader中找到run.py文件。

点击鼠标右键打开终端，输入如下命令即可启动VeighNa Trader：

```
python run.py 
```

请注意run.py中包含了较多的启动加载项（交易接口和应用模块），请根据自己所用的操作系统以及实际的交易需求修改调整使用（若需加载接口，取消接口前注释符号即可）。

请注意部分接口不支持Ubuntu系统，请不要加载。连接接口介绍详见交易接口篇（可查看接口支持的操作系统）。

> 如果启动时出现一些库版本不兼容的情况，可根据提示对这些库重新pip安装。


## 常见问题

### Python开发环境问题处理

如果安装时出现由于找不到头文件导致的报错“command ‘gcc’ failed with exit status 1”，可能是没有正确安装Python开发环境造成的。可以在终端中运行下述命令尝试解决：

```
sudo apt-get install 你的python软连接-dev
```

### 图形驱动问题处理

在有图形界面的Ubuntu系统上启动，如果出现qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found的报错，可以在终端中运行下述命令来安装libxcb-xinerama0，尝试解决图形驱动的依赖问题：

```
sudo apt-get install libxcb-xinerama0
```

### 中文编码问题处理

如果Ubuntu系统语言是英文，在连接CTP接口这类使用中文语言的接口时，可能会出现下述报错：

terminate called after throwing an instance of 'std::runtime_error'
what(): locale::facet::_S_create_c_locale name not valid

可以使用local-gen安装中文编码尝试解决：

```
sudo locale-gen zh_CN.GB18030
```

如果还没有解决，可能是因为系统缺少中文字体支持。解决方法如下：

```
sudo apt-get update
sudo apt-get install -y fonts-noto-cjk fonts-wqy-zenhei fonts-wqy-microhei
fc-cache -f -v
fc-list :lang=zh | wc -l
sudo locale-gen zh_CN.UTF-8 zh_CN.GB18030
```

### 安装依赖与路径分隔符

在Linux系统中安装C++接口时，如果使用`--no-build-isolation`参数，需要提前安装以下依赖库：

```bash
uv pip install meson-python meson pybind11
sudo apt-get update && sudo apt-get install -y ninja-build
```

此外，建议在Linux系统中使用正斜杠`/`作为路径分隔符，以避免路径解析问题。因此，推荐的安装命令如下：

```bash
uv pip install -e . --no-build-isolation --config-settings=build-dir=./{包的名字}/api
```

此命令将确保API文件夹被正确指定为构建目录，避免路径格式问题导致的安装失败。



# FILE: docs/community/app/portfolio_strategy.md

# PortfolioStrategy - 多合约组合策略模块

## 功能简介

PortfolioStrategy是用于**多合约组合策略实盘**的功能模块，用户可以通过其UI界面操作来便捷完成策略初始化、策略启动、策略停止、策略参数编辑以及策略移除等任务。

## 加载启动

### VeighNa Station加载

启动登录VeighNa Station后，点击【交易】按钮，在配置对话框中的【应用模块】栏勾选【PortfolioStrategy】。

### 脚本加载

在启动脚本中添加如下代码：

```python3
# 写在顶部
from vnpy_portfoliostrategy import PortfolioStrategyApp

# 写在创建main_engine对象后
main_engine.add_app(PortfolioStrategyApp)
```


## 启动模块

<span id="jump">

对于用户自行开发的策略，需要放到VeighNa Trader运行时目录下的**strategies**目录中，才能被识别加载。具体的运行时目录路径，可以在VeighNa Trader主界面顶部的标题栏查看。

对于在Windows上默认安装的用户来说，放置策略的strategies目录路径通常为：

```
    C:\Users\Administrator\strategies
```

其中Administrator为当前登录Windows的系统用户名。

</span>

在启动模块之前，请先连接交易接口（连接方法详见基本使用篇的连接接口部分）。看到VeighNa Trader主界面【日志】栏输出“合约信息查询成功”之后再启动模块，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

请注意，IB接口因为登录时无法自动获取所有的合约信息，只有在用户手动订阅行情时才能获取。因此需要在主界面上先行手动订阅合约行情，再启动模块。

成功连接交易接口后，在菜单栏中点击【功能】-> 【组合策略】，或者点击左侧按钮栏的图标：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/0.png)

即可进入多合约组合策略模块的UI界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/1.png)

如果配置了数据服务（配置方法详见基本使用篇的全局配置部分），打开多合约组合策略模块时会自动执行数据服务登录初始化。若成功登录，则会输出“数据服务初始化成功”的日志，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/2.png)


## 添加策略

用户可以基于编写好的组合策略模板（类）来创建不同的策略实例（对象）。

在左上角的下拉框中选择要交易的策略名称，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/3.png)

请注意，显示的策略名称是**策略类**（驼峰式命名）的名字，而不是策略文件（下划线模式命名）的名字。

选择好策略类之后，点击【添加策略】，会弹出添加策略对话框，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/4.png)

在创建策略实例时，需要配置相关参数，各参数要求如下：

- 实例名称
  - 实例名称不能重名；
- 合约品种
  - 格式为vt_symbol（合约代码 + 交易所名称）；
  - 一定要是实盘交易系统中可以查到的合约名称；
  - 合约名用“,”隔开，中间不加空格；
- 参数设置
  - 显示的参数名是策略里写在parameters列表中的参数名；
  - 默认数值为策略里的参数的默认值；
  - 由上图可观察到，参数名后面<>括号中显示的是该参数的数据类型，在填写参数时应遵循相应的数据类型。其中，<class 'str'>是字符串、<class 'int'>是整数、<class 'float'>是浮点数；
  - 请注意，如果某个参数可能会调整至有小数位的数值，而默认参数值是整数（比如1）。请在编写策略时，把默认参数值设为浮点数（比如1.0）。否则策略会默认该项参数为整数，在后续【编辑】策略实例参数时，会只允许填进整数。

参数配置完成后，点击【添加】按钮，则开始创建策略实例。创建成功后可在左侧的策略监控组件中看到该策略实例，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/5.png)

策略监控组件顶部显示的是策略实例名、策略类名以及策略作者名（在策略里定义的author）。顶部按钮用于控制和管理策略实例，第一行表格显示了策略内部的参数信息（参数名需要写在策略的parameters列表中图形界面才会显示），第二行表格则显示了策略运行过程中的变量信息（变量名需要写在策略的variables列表中图形界面才会显示）。【inited】字段表示当前策略的初始化状态（是否已经完成了历史数据回放），【trading】字段表示策略当前是否能够开始交易。

从上图可观察到，此时该策略实例的【inited】和【trading】状态都为【False】。说明该策略实例还没有初始化，也还不能发出交易信号。

策略实例创建成功后，该策略实例的配置信息会被保存到.vntrader文件夹下的portfolio_strategy_setting.json文件中。

请注意，如果添加了同名的策略实例，则会创建失败，图形界面输出“创建策略失败，存在重名”的日志信息，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/8.png)


## 管理策略

### 初始化

策略实例创建成功后，就可以对该实例进行初始化了。点击该策略实例下的【初始化】按钮，若初始化成功，则如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/6.png)

初始化完成后，可观察到此时该策略实例的【inited】状态已经为【True】。说明该策略实例已经加载过历史数据并完成初始化了。【trading】状态还是为【False】，说明此时该策略实例还不能开始自动交易。

请注意，与CTA策略不同，如果创建实例时输入错误的vt_symbol，多合约组合策略模块会在初始化时报错，而不是在创建策略实例时报错，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/7.png)

### 启动

策略实例初始化成功，【inited】状态为【True】时，才能启动该策略的自动交易功能。点击该策略实例下的【启动】按钮，即可启动该策略实例。成功后如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/10.png)

可观察到此时该策略实例的【inited】和【trading】状态都为【True】。说明此时该策略实例已经完成了历史数据回放，而且此时策略内部的交易请求类函数（buy/sell/short/cover/cancel_order等），以及信息输出类函数（send_email/put_event等），才会真正执行并发出对应的请求指令到底层接口中（真正执行交易）。

在上一步策略初始化的过程中，尽管策略同样在接收（历史）数据，并调用对应的功能函数，但因为【trading】状态为【False】，所以并不会有任何真正的委托下单操作或者交易相关的日志信息输出。

如果启动之后，策略发出了委托，可以去VeighNa Trader主界面【委托】栏查看委托订单细节，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/9.png)

请注意，与CTA策略模块不同，多合约组合策略**不提供本地停止单功能**，所以UI界面上不会有停止单的显示区域了。


### 停止

如果启动策略之后，由于某些情况（如到了市场收盘时间，或盘中遇到紧急情况）想要停止、编辑或者移除策略，可以点击策略实例下的【停止】按钮，即可停止该策略实例的自动交易。成功后如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/11.png)

组合策略引擎会自动将该策略之前发出的所有活动委托全部撤销，以保证在策略停止后不会有失去控制的委托存在。同时该策略实例最新的变量信息会被保存到.vntrader文件夹下的portfolio_strategy_data.json文件中。

此时可观察到该策略实例的【trading】状态已变为【False】，说明此时该策略实例已经停止自动交易了。

在多合约组合策略的实盘交易过程中，正常情况应该让策略在整个交易时段中都自动运行，尽量不要有额外的暂停重启类操作。对于国内期货市场来说，应该在交易时段开始前，启动策略的自动交易，然后直到收盘后，再关闭自动交易。因为现在CTP夜盘收盘后也会关闭系统，早上开盘前重启，所以夜盘收盘后也需要停止策略，关闭VeighNa Trader了。

### 编辑

如果创建策略实例之后，想要编辑某个策略实例的参数（若已启动策略，需要先点击策略实例下的【停止】按钮，停止策略），可以点击该策略实例下的【编辑】按钮，会弹出参数编辑对话框，以供修改策略参数。如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/12.png)

编辑完策略参数之后，点击下方的【确定】按钮，相应的修改会立即更新在参数表格中。

但是策略实例的交易合约代码无法修改，同时修改完后也不会重新执行初始化操作。也请注意，此时修改的只是.vntrader文件夹下porfolio_strategy_setting.json文件中该策略实例的参数值，并没有修改原策略文件下的参数。

修改前，json文件如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/18.png)


修改后，json文件如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/17.png)

若盘中编辑后想要再次启动策略，点击策略实例下的【启动】按钮即可再次启动该策略实例。

### 移除

如果创建策略实例之后，想要移除某个策略实例（若已启动策略，需要先点击策略实例下的【停止】按钮，停止策略），可以点击该策略实例下的【移除】按钮。移除成功后，图形界面左侧的策略监控组件中将不会再显示该策略实例的信息。如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/13.png)

此时.vntrader文件夹下的portfolio_strategy_setting.json文件也移除了该策略实例的配置信息。

### 状态跟踪

如果想要通过图形界面跟踪策略的状态，有两种方式：

1. 调用put_event函数

   策略实例中所有的的变量信息，都需要把变量名写在策略的variables列表中，才能在图形界面显示。如果想跟踪变量的状态变化，则需要在策略中调用put_event函数，界面上才会进行数据刷新。

   有时用户会发现自己写的策略无论跑多久，变量信息都不发生变化，这种情况请检查策略中是否漏掉了对put_event函数的调用。

2. 调用write_log函数

   如果不仅想观察到变量信息的状态变化，还想根据策略的状态输出基于自己需求的个性化的日志，可以在策略中调用write_log函数，进行日志输出。

## 运行日志

### 日志内容

多合约组合策略模块UI界面上输出的日志有两个来源，分别是策略引擎和策略实例。

**引擎日志**

策略引擎一般输出的是全局信息。下图中除了策略实例名后加冒号的内容之外，都是策略引擎输出的日志。

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/15.png)

**策略日志**

如果在策略中调用了write_log函数，那么日志内容就会通过策略日志输出。下图红框里的内容是策略实例输出的策略日志。冒号前是策略实例的名称，冒号后是write_log函数输出的内容。

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/16.png)

### 清空操作

如果想要清空多合约组合策略UI界面上的日志输出，可以点击右上角的【清空日志】按钮，则可一键清空该界面上已输出的日志。

点击【清空日志】后，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/14.png)

## 批量操作

在策略经过充分测试，实盘运行较为稳定，不需要经常


# FILE: docs/community/app/excel_rtd.md

# ExcelRtd - EXCEL RTD模块

## 功能简介

ExcelRtd是用于**在Excel中访问VeighNa程序内任意数据信息**的功能模块，
RTD全称是RealTimeData，是微软提供的主要面向金融行业中实时数据需求设计的Excel数据对接方案。ExcelRtd依赖于PyXLLC模块（www.pyxll.com），该模块属于商业软件，需要购买才能使用（提供30天免费使用）。

## 安装PyXLL
为了使用ExcelRtd模块，需要安装PyXLL插件。步骤如下：

首先进入[PyXLL官网](https://www.pyxll.com/)，点击DownloadPyXLL，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_0.png)

接着跳转到下载界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/13.png)

这时需要填写相应字段，其中**Python Version**选择Python3.10，而**Excel Version**则根据自己安装的Excel版本选择，一般为64bit(x64)。

填写完之后点击【Download PyXLL】，就会跳转到下载页面。将文件下载好之后，进入放置该文件的文件夹，按住shift键并且点击鼠标右键，选择【在此处打开PowerShell窗口】，运行以下命令：
```bash
pip install pyxll
pyxll install
```

接着按照软件要求就能成功安装了。

请注意，在执行到下图这一步时：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_9.png)

如果没有具体指定路径，会安装到图中的默认位置（因为后面还需要进入这个文件夹，所以请记住这个路径）。

接着进入该目录下的examples目录，并把路径~/veighna_studio/Lib/site-packages/vnpy_excelrtd/下的vnpy_rtd.py放入该目录，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_5.png)

如此就算正式安装完成了。

## 加载启动

### VeighNa Station加载

启动登录VeighNa Station后，点击【交易】按钮，在配置对话框中的【应用模块】栏勾选【ExcelRtd】。

### 脚本加载

在启动脚本中添加如下代码：

```python3
# 写在顶部
from vnpy_excelrtd import ExcelRtdApp

# 写在创建main_engine对象后
main_engine.add_app(ExcelRtdApp)
```

## 启动模块

在启动模块之前，请先连接交易接口（连接方法详见基本使用篇的连接接口部分）。看到VeighNa Trader主界面【日志】栏输出“合约信息查询成功”之后再启动模块，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

请注意，IB接口因为登录时无法自动获取所有的合约信息，只有在用户手动订阅行情时才能获取。因此需要在主界面上先行手动订阅合约行情，再启动模块。

成功连接交易接口后，在菜单栏中点击【功能】 -> 【Excel RTD】，或者点击左侧按钮栏的图表：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_6.png)

即可进入Excel RTD模块的UI界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/15.png)


## 功能和配置

### 基础应用

在启动Excel RTD模块后，即可在Excel表格中通过PyXll调用该模块提供的功能（主要是通过rtd_tick_data函数获取实时数据）。

首先打开一个excel表格，并且在每个单元格中调用rtd_tick_data函数并传入相应参数则可获取对应的数据，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/14.png)

上图是获取豆油2205四个字段实时数据（分别是bid_price_1、high_price、low_price以及last_price）的例子。

从图中可以看出rtd_tick_data函数需要两个参数：一个是vt_symbol，另一个是VeighNa中定义的TickData的属性（具体属性可参考源代码vnpy.trader.object.TickData）。这两个参数都是字符串，第一个参数可以通过单元格的具体位置指定，比如“A1”表示A列第1行的数据。

与此同时，在Excel RTD模块的图形界面中也能看到相应输出，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/16.png)

### 进阶应用
当然，上面只是简单的展示了ExcelRtd模块的功能。至于具体获取哪些数据，以什么样的方式展示在excel上，则由用户根据自己的实际需求编写。这里提供几个进阶的案例，包括期货市场报价跟踪、市场深度行情跟踪以及价差监控：

#### 期货市场报价跟踪
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_10.png)

#### 市场深度行情跟踪

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_11.png)
#### 价差监控

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_12.png)


# FILE: docs/community/app/paper_account.md

# PaperAccount - 本地仿真交易模块


## 功能简介

PaperAccount是用于**本地仿真交易**的功能模块，用户可以通过其UI界面基于实盘行情进行本地化的模拟交易。

## 加载启动

### VeighNa Station加载

启动登录VeighNa Station后，点击【交易】按钮，在配置对话框中的【应用模块】栏勾选【PaperAccount】。

### 脚本加载

在启动脚本中添加如下代码：

```python3
# 写在顶部
from vnpy_paperaccount import PaperAccountApp

# 写在创建main_engine对象后
main_engine.add_app(PaperAccountApp)
```


## 启动模块

在启动模块之前，请先连接要进行模拟交易的接口（连接方法详见基本使用篇的连接接口部分）。看到VeighNa Trader主界面【日志】栏输出“合约信息查询成功”之后再启动模块，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

请注意，IB接口因为登录时无法自动获取所有的合约信息，只有在用户手动订阅行情时才能获取。因此需要在主界面上先行手动订阅合约行情，再启动模块。

交易接口连接后，本地模拟交易模块自动启动。此时所有合约的交易委托和撤单请求均**被本地模拟交易模块接管**，不会再发往实盘服务器。


## 功能配置

在菜单栏中点击【功能】-> 【模拟交易】，或者点击左侧按钮栏的图标：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/4.png)

即可进入本地模拟交易模块的UI界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/5.png)

用户可以通过UI界面对以下功能进行配置：

- 市价委托和停止委托的成交滑点
  - 用于影响市价单和停止单成交时，成交价格相对于盘口价格的**滑点跳数**；

- 模拟交易持仓盈亏的计算频率
  - 多少秒执行一次持仓盈亏计算更新，如果持仓较多时发现程序卡顿，建议尝试调低频率；

- 下单后立即使用当前盘口撮合
  - 默认情况下，用户发出的委托需要**等到下一个TICK盘口推送才会撮合**（模拟实盘情景），对于TICK推送频率较低的不活跃合约可以勾选该选项，委托后会**立即基于当前的最新TICK盘口撮合**；

- 清空所有持仓
  - 一键清空本地所有持仓数据。

本地模拟交易模块同样可以和其他策略应用模块（如CtaStrategy模块、SpreadTrading模块等）一起使用，从而实现本地化的量化策略仿真交易测试。


## 数据监控

用户可以通过【查询合约】来查询确认合约的交易接口状态：

点击菜单栏的【帮助】->【合约查询】，在弹出的对话框中直接点击右上角的【查询】按钮，发现所有合约的【交易接口】列均显示为PAPER，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/2.png)

在对某一合约进行下单和撤单操作前，用户必须先**订阅**该合约的行情。

下图中【委托】、【成交】、【持仓】三个监控组件中显示的信息，其接口列均为PAPER（本地模拟数据)：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/3.png)

请注意，本地模拟交易模块**没有提供资金计算功能**，所以【资金】组件显示的是实盘账号的资金，并不会因为在本地模拟交易模块产生的委托而改变。


## 业务逻辑

本地模拟交易模块的业务逻辑如下所示：

- 支持的委托类型（不支持的类型会被拒单）：

  - 限价单；
  - 市价单；
  - 停止单；

- 委托撮合规则采用**到价成交**模式，以买入委托为例：

  - 限价单：当盘口卖1价ask_price_1小于等于委托价格，则成交；
  - 停止单：当盘口卖1价ask_price_1大于等于委托价格，则成交；

- 委托成交时**不考虑盘口挂单量**，一次性全部成交；

- 委托成交后，先推送委托状态更新OrderData，再推送成交信息TradeData，**和实盘交易中的顺序一致**；

- 委托成交后，模块会自动记录相应的持仓信息PositionData：

  - 根据合约本身的持仓模式（多空仓 vs 净仓位）信息，维护对应的持仓信息；
  - **开仓成交时，采用加权平均计算更新持仓成本价；**
  - **平仓成交时，持仓成本价不变；**
  - 多空仓模式下，挂出平仓委托后会冻结相应的持仓数量，可用数量不足时会拒单；
  - 持仓的盈亏会基于持仓成本价和最新成交价定时计算（默认频率1秒）；

- 数据的持久化保存：

  - 成交数据和委托数据不保存，关闭VeighNa Trader后即消失；
  - 持仓数据会在有变化时**立即写入硬盘文件**，重启VeighNa Trader登录交易接口后即可看到（要收到相应的合约信息）。



# FILE: docs/community/app/web_trader.md

# WebTrader - Web服务器模块

## 功能简介

WebTrader是用于**Web应用后端服务**的功能模块，用户可以通过浏览器（而非PyQt桌面端）来运行管理VeighNa量化策略交易。

## 架构设计

WebTrader采用了FastAPI作为后端服务器，支持REST主动请求调用和WebSocket被动数据推送，运行时整体框架图如下：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_1.png)

后端服务包括两个独立的进程：
- 策略交易进程
  - 运行VeighNa Trader的进程，负责所有策略交易功能的运行；
  - 启动了RpcServer用于对Web服务进程功能调用；
- Web服务进程
  - 运行了FastAPI的进程，负责对外提供Web访问的服务；
  - 启动了RpcClient用于调用策略交易进程的相关功能。

从网页端到策略交易进程的双向通讯模式包括：
- 主动请求调用（订阅行情、挂撤单、查询数据）
  - 浏览器发起REST API调用（访问某个URL地址提交数据）到Web服务进程；
  - Web服务进程收到后，转换为RPC请求（Req-Rep通讯模式）发送给策略交易进程；
  - 策略交易进程执行请求处理后，返回结果给Web服务进程；
  - Web服务进程返回数据给浏览器。
- 被动数据推送（行情推送、委托推送）
  - 浏览器发起Websocket连接到Web服务进程；
  - 策略交易进程通过RPC推送（Pub-Sub通讯），将数据推送给Web服务进程；
  - Web服务进程收到后，将数据通过Websocket API实时推送给浏览器（JSON格式）。

## 加载启动

### VeighNa Station加载

启动登录VeighNa Station后，点击【交易】按钮，在配置对话框中的【应用模块】栏勾选【WebTrader】。

### 脚本加载

在启动脚本中添加如下代码：

```python3
# 写在顶部
from vnpy_webtrader import WebTraderApp

# 写在创建main_engine对象后
main_engine.add_app(WebTraderApp)
```

### 启动模块

在启动模块之前，请先连接登录交易接口（连接方法详见基本使用篇的连接接口部分）。看到VeighNa Trader主界面【日志】栏输出“合约信息查询成功”之后再启动模块，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/market_radar/1.png)

成功连接交易接口后，在菜单栏中点击【功能】-> 【Web服务】，或者点击左侧按钮栏的图标：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_0.png)

即可进入RPC服务模块的UI界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_3.png)

此时系统中运行的只包括策略交易进程，左上角区域的服务器配置选项包括：
- 用户名和密码：从网页端登录Web应用时所用的用户名和密码，使用时请修改为自己想用的用户名和密码（通过启动目录.vntrader下的web_trader_setting.json修改），请注意这里的用户名和密码与底层交易接口无关；
- 请求和订阅地址：架构图中Web服务进程和策略交易进程之间，进行RPC通讯的地址，注意端口不要和其他程序冲突即可。

点击启动按钮后，会根据用户输入的配置信息在系统后台启动Web服务进程，同时在右侧区域输出Fast API运行过程中的相关日志信息。


## 接口演示
在启动Web服务后，在浏览器打开网址<http://127.0.0.1:8000/docs>，即可看到如下图所示的接口文档网页：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_2.png)

这里包含了目前WebTrader支持的相关接口信息，下面结合vnpy_webtrader项目下提供的[Jupyter Notebook](https://github.com/vnpy/vnpy_webtrader/blob/main/script/test.ipynb)进行相关的接口演示。

### 获得令牌（token）
```python3
import requests
import json

url = "http://127.0.0.1:8000/"
username = "vnpy"
password = "vnpy"

r = requests.post(
    url + "token",
    data={"username": username, "password": password},
    headers={"accept": "application/json"}
)
token = r.json()["access_token"]
```
首先导入相应的模块requests和json，接着定义url和用户名和密码，通过requests的post方法传入相应参数就能够获得令牌（token），后续访问使用各种接口直接传入token即可。

### 行情订阅
```
r = requests.post(url + "tick/" + "cu2112.SHFE", headers={"Authorization":"Bearer " + token})
```
通过上述命令可实现对合约cu2112.SHFE的订阅，同时可以在图形界面收到该合约的行情数据推送，入下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_4.png)

###  批量查询
```python3
# 查询函数
def query_test(name):
    """查询对应类型的数据"""
    r = requests.get(
        url + name,
        headers={"Authorization": "Bearer " + token}
    )
    return r.json()

# 批量查询
for name in ["tick", "contract", "account", "position", "order", "trade"]:
    data = query_test(name)
    print(name + "-" * 20)
    if data:
        print(data[0])
```
如有需要，同样可以通过发出主动请求查询相关的数据，比如tick数据、合约数据、账户数据、 持仓数据、委托数据以及成交数据。

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_5.png)

### 委托测试
```python3
# 委托测试
req = {
    "symbol": "cu2112",
    "exchange": "SHFE",
    "direction": "多",
    "type": "限价",
    "volume": 1,
    "price": 71030,
    "offset": "开",
    "reference": "WebTrader"
}

r = requests.post(
    url + "order",
    json=req,
    headers={"Authorization": "Bearer " + token}
)
vt_orderid = r.json()

print(vt_orderid)
```
下单后同样能在图形化界面看到委托信息，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_6.png)

### 撤单测试
```python3
# 撤单测试
r = requests.delete(
    url + "order/" + vt_orderid,
    headers={"Authorization": "Bearer " + token}
)
```
如果想将之前下的委托撤销，可以发送主动请求，结果同样会在图形化界面更新，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_7.png)

### Websocket测试

```python3
# Weboscket测试
from websocket import create_connection

ws = create_connection("ws://127.0.0.1:8000/ws/?token=" + token)

while True:
    result =  ws.recv()
    print("Received '%s'" % result)

ws.close()
```
通过Websocket可以被动接收策略交易进程推送过来的行情数据和委托数据等，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_8.png)

## 后续计划
WebTrader仅实现了Web应用的后端（提供了浏览器访问数据的接口），而前端页面（也就是浏览器中看到的网页）则按照之前的计划交给社区用户来实现，欢迎大家贡献代码。

同时WebTrader目前只支持基础的手动交易功能，后续将会逐渐加上策略交易应用相关的管理功能（比如CtaStrategy的相关调用）。



# FILE: docs/community/app/script_trader.md

# ScriptTrader - 脚本策略交易模块

## 功能简介

ScriptTrader是用于**脚本策略交易**的功能模块，提供了交互式的量化分析和程序化交易功能，又提供以整个策略连续运行的脚本策略功能。

故其可视为直接利用Python对交易客户端进行操作。它与CTA策略模块的区别在于：

- 突破了单交易所，单标的的限制；
- 可以较方便的实现如股指期货和一篮子股票之间的对冲策略、跨品种套利、股票市场扫描自动化选股等功能。

## 加载启动

### VeighNa Station加载

启动登录VeighNa Station后，点击【交易】按钮，在配置对话框中的【应用模块】栏勾选【ScriptTrader】。

### 脚本加载

在启动脚本中添加如下代码：

```python3
# 写在顶部
from vnpy_scripttrader import ScriptTraderApp

# 写在创建main_engine对象后
main_engine.add_app(ScriptTraderApp)
```

## 启动模块

在启动模块之前，请先连接交易接口（连接方法详见基本使用篇的连接接口部分）。看到VeighNa Trader主界面【日志】栏输出“合约信息查询成功”之后再启动模块，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

请注意，IB接口因为登录时无法自动获取所有的合约信息，只有在用户手动订阅行情时才能获取。因此需要在主界面上先行手动订阅合约行情，再启动模块。

成功连接交易接口后，在菜单栏中点击【功能】-> 【脚本策略】，或者点击左侧按钮栏的图标：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/0.png)

即可进入脚本交易模块的UI界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/1.png)

如果配置了数据服务（配置方法详见基本使用篇的全局配置部分），打开脚本交易模块时会自动执行数据服务登录初始化。若成功登录，则会输出“数据服务初始化成功”的日志，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/20.png)

用户可以通过UI界面使用以下功能：

### 启动

脚本策略需要事先编写好脚本策略文件，如test_strategy.py（脚本策略模板可参考[**脚本策略**](#jump)部分），因此点击【打开】按钮后需要用户指定该脚本策略文件的路径，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/21.png)

打开脚本策略之后，点击【启动】按钮则会启动脚本策略，并在下方界面输出相关信息，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/8.png)

### 停止

如果想停止脚本策略，直接点击【停止】按钮，之后策略会停止，通知会在下方界面输出“策略交易脚本停止”的日志，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/11.png)

### 清空

如果觉得下方显示界面的信息太多，或者想开启新的脚本策略，可以点击【清空】按钮，这时下方的所有信息就会被清空，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/10.png)


## 脚本策略模板

<span id="jump">

脚本策略文件编写需要遵循一定格式，下面提供使用模板，其作用为：

- 订阅两个品种的行情；
- 打印合约信息；
- 每隔3秒获取最新行情。

```python3
from time import sleep
from vnpy_scripttrader import ScriptEngine

def run(engine: ScriptEngine):
    """"""
    vt_symbols = ["sc2209.INE", "sc2203.INE"]

    # 订阅行情
    engine.subscribe(vt_symbols)

    # 获取合约信息
    for vt_symbol in vt_symbols:
        contract = engine.get_contract(vt_symbol)
        msg = f"合约信息，{contract}"
        engine.write_log(msg)

    # 持续运行，使用strategy_active来判断是否要退出程序
    while engine.strategy_active:
        # 轮询获取行情
        for vt_symbol in vt_symbols:
            tick = engine.get_tick(vt_symbol)
            msg = f"最新行情, {tick}"
            engine.write_log(msg)

        # 等待3秒进入下一轮
        sleep(3)
```

其中engine.strategy_active用于控制While循环，可视作是脚本策略的开关：

- 点击【启动】按钮，启动While循环，执行脚本策略；
- 点击【停止】按钮，退出While循环，停止脚本策略。


## 功能函数

Jupyter模式是基于脚本引擎（ScriptEngine）驱动的，下面通过jupyter notebook来说明ScriptEngine引擎的各功能函数。

首先打开Jupyter notebook，然后加载组件、初始化脚本引擎：

```python3
from vnpy_scripttrader import init_cli_trading
from vnpy_ctp import CtpGateway
engine = init_cli_trading([CtpGateway])
```

其中：

- 脚本引擎可以支持同时连接多个接口；
- init_cli_trading(gateways: Sequence[BaseGateway])可以将多个接口类，以列表的形式传递给init_cli_trading；
- init_cli_trading可视为vnpy封好的初始化启动函数，对主引擎、脚本引擎等各种对象进行了封装。

### 连接接口

**connect_gateway**

* 入参：setting: dict, gateway_name: str

* 出参：无

不同接口需要不同的配置参数，SimNow的配置如下：
```json
setting = {
    "用户名": "xxxx",
    "密码": "xxxx",
    "经纪商代码": "9999",
    "交易服务器":"180.168.146.187:10202",
    "行情服务器":"180.168.146.187:10212",
    "产品名称":"simnow_client_test",
    "授权编码":"0000000000000000"
}
engine.connect_gateway(setting,"CTP")
```

其他接口配置可以参考site-packages目录下不同接口模块类（如vnpy_ctp.gateway.ctp_gateway）中的default_setting来填写。

### 订阅行情

**subscribe**

* 入参：vt_symbols: Sequence[str]

* 出参：无

subscribe()函数用于订阅行情信息，若需要订阅一篮子合约的行情，可以使用列表格式。
```python3
engine.subscribe(vt_symbols = ["rb2209.SHFE","rb2210.SHFE"])
```

### 查询数据
这里介绍一下连接上交易接口并成功订阅数据后的数据存储：

- 底层接口不停向主引擎推送新的数据；
- 主引擎里维护着一个ticks字典用于缓存不同标的的最新tick数据（仅能缓存最新数据）；
- use_df的作用是转换成DataFrame格式，便于数据分析。

#### 单条查询

**get_tick**

* 入参：vt_symbol: str, use_df: bool = False

* 出参：TickData

查询单个标的最新tick，use_df为可选参数，用于把返回的类对象转化成DataFrame格式，便于数据分析。

```python3
tick = engine.get_tick(vt_symbol="rb2210.SHFE",use_df=False)
```

其中：

- vt_symbol：为本地合约代码，格式是合约品种+交易所，如rb2210.SHFE；
- use_df：为bool变量，默认False，返回TickData类对象，否则返回相应DataFrame，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/13.png)

**get_order**

* 入参：vt_orderid: str, use_df: bool = False

* 出参：OrderData

根据vt_orderid查询委托单的详细信息。

```python3
order = engine.get_order(vt_orderid="CTP.3_-1795780178_1",use_df=False)
```

其中，vt_orderid为本地委托号（在委托下单时，会自动返回该委托的vt_orderid）。
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/14.png)

**get_contract**

* 入参：vt_symbol, use_df: bool = False

* 出参：ContractData

根据本地vt_symbol来查询对应合约对象的详细信息。

```python3
contract = engine.get_contract(vt_symbol="rb2210.SHFE",use_df=False)
```
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/15.png)

**get_account**

* 入参：vt_accountid: str, use_df: bool = False

* 出参：AccountData

根据本地vt_accountid来查询对应资金信息。

```python3
account = engine.get_account(vt_accountid="CTP.189672",use_df=False)
```
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/16.png)

**get_position**

* 入参：vt_positionid: str, use_df: bool = False

* 出参：PositionData

根据vt_positionid来查询持仓情况，返回对象包含接口名称、交易所、合约代码、数量、冻结数量等。

```python3
position = engine.get_position(vt_positionid='CTP.hc2305.SHFE.多')
```
注意，vt_positionid为vnpy内部对于一笔特定持仓的唯一持仓编号，格式为"gateway_name.vt_symbol.Direction.value"，其中持仓方向可选“多”、“空”和“净”，如下图所示：
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/17.png)

#### 多条查询

**get_ticks**

* 入参：vt_symbols: Sequence[str], use_df: bool = False

* 出参：Sequence[TickData]

查询多个合约最新tick。

```python3
ticks = engine.get_ticks(vt_symbols=['rb2209.SHFE','rb2210.SHFE'],use_df=True)
```

vt_symbols是列表格式，里面包含多个vt_symbol，如图。
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/18.png)


**get_orders**

* 入参：vt_orderids: Sequence[str], use_df: bool = False

* 出参：Sequence[OrderData]

根据查询多个vt_orderid查询其详细信息。vt_orderids为列表，里面包含多个vt_orderid。

```python3
orders = engine.get_orders([orderid_one,orderid_two],use_df=True)
```

**get_trades**

* 入参：


# FILE: docs/community/app/risk_manager.md

# RiskManager - 事前风控管理模块

## 功能简介

RiskManager模块是用于**事前风控管理**的功能模块，用户可以通过其UI界面操作来便捷完成启动风控，参数修改和停止风控等任务。

## 加载启动

### VeighNa Station加载

启动登录VeighNa Station后，点击【交易】按钮，在配置对话框中的【应用模块】栏勾选【RiskManager】。

### 脚本加载

在启动脚本中添加如下代码：

```python3
# 写在顶部
from vnpy_riskmanager import RiskManagerApp

# 写在创建main_engine对象后
main_engine.add_app(RiskManagerApp)
```

## 启动模块

在菜单栏中点击【功能】-> 【交易风控】，或者点击左侧按钮栏的图标：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-1.png)

即可进入事前风控模块的UI界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-2.png)


## 启动风控

事前风控模块负责在委托通过交易API接口发出前，检查其状态是否符合各种风控规则。风控规则包括交易流控、下单数量、活动委托、撤单总数等，具体如下：

 - 委托流控相关：
   - 委托流控上限：给定时间窗口内最多允许发出的委托笔数
   - 委托流控清空：每隔多少秒清零上述统计的委托笔数
 - 单笔委托上限：每一笔委托允许的最大下单量
 - 总成交上限：今天日内允许的最大总成交笔数（注意不是委托笔数）
 - 活动委托上限：允许的处于活动状态（提交中、未成交、部分成交）最大委托数量
 - 合约撤单上限：今天日内允许的单合约撤单次数上限（每个合约独立统计）

推荐每天在运行自动交易前启动事前风控，以检查每一笔发出的委托是否符合风控要求：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-3.png)

1. 在【风控运行状态】一栏的下拉框中选择【启动】；
2. 设定各种风控规则的参数后，点击下方的【保存】按钮，即可开始运行风控；
3. 此时系统内的每一笔委托，都需要满足全部风控要求（不超过限制）后，才能通过底层接口发出。


## 参数修改

事前风控模块允许用户自定义风控参数：

* 用户可以点击输入框右侧的上下箭头来修改参数，也可以直接输入数字来修改，如下图所示。
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-4.png)
* 修改后请点击【保存】按钮生效。

## 停止风控

不需要运行风控时，用户可以停止风控：

* 在【风控运行状态】的下拉框中选择【停止】，如下图所示：
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-5.png)
* 点击下方的【保存】按钮即可停止对委托的风控检查。



# FILE: docs/community/app/data_manager.md

# DataManager - 历史数据管理模块

## 功能简介

DataManager是用于**历史数据管理**的功能模块，用户可以通过其UI界面操作来便捷完成数据下载、数据查看、数据导入和数据导出等任务。

## 加载启动

### VeighNa Station加载

启动登录VeighNa Station后，点击【交易】按钮，在配置对话框中的【应用模块】栏勾选【DataManager】。

### 脚本加载

在启动脚本中添加如下代码：

```python3
# 写在顶部
from vnpy_datamanager import DataManagerApp

# 写在创建main_engine对象后
main_engine.add_app(DataManagerApp)
```


## 启动模块

启动VeighNa Trader后，在菜单栏中点击【功能】-> 【数据管理】，或者点击左侧按钮栏的图标：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/00.png)

即可进入历史数据管理UI界面，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/1.png)


## 下载数据

DataManager模块提供了一键下载历史数据的功能，点击右上角【下载数据】按钮，会弹出下载历史数据窗口，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/2.png)

需要填写代码、交易所、周期以及开始日期四个字段信息：

<span id="jump">

- 代码
  - 代码格式为合约品种
  - 如IF888、rb2105
- 交易所
  - 合约交易的交易所（点击窗口右侧箭头按钮可选择VeighNa支持的交易所列表）
- 周期
  - MINUTE（1分钟K线）
  - HOUR（1小时K线）
  - DAILY（日K线）
  - WEEKLY（周K线）
  - TICK（一个Tick）
- 开始日期
  - 格式为yy/mm/dd
  - 如2018/2/25

</span>

填写完成后，点击下方【下载】按钮启动下载程序，下载成功如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/3.png)

注意下载完成后的历史数据会保存在本地数据库中，后续回测或实盘时可以直接使用，无需每次都重复下载。

### 数据来源：数据服务（期货、股票、期权）

以RQData为例，[RQData](https://www.ricequant.com/welcome/purchase?utm_source=vnpy)提供国内期货、股票以及期权的历史数据。在使用前需要保证数据服务已经正确配置（配置方法详见基本使用篇的全局配置部分）。

### 数据来源：IB（外盘期货、股票、现货等）

Interactive Brokers盈透证券（IB）提供丰富的外盘市场历史数据下载（包括股票、期货、期权、现货等），注意下载前需要先启动IB TWS交易软件，并在VeighNa Trader主界面连接好IB接口，并订阅所需合约行情。


## 导入数据

如果已经从其他渠道获取到了CSV格式的数据文件，可以通过DataManager的数据导入功能，将其快速导入VeighNa数据库。点击右上角的【导入数据】按钮，会弹出从如下图所示的对话框：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/21.png)

点击顶部的【选择文件】按钮，会弹出窗口选择要导入的CSV文件路径，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/5.png)

然后配置数据导入的相关细节：

- 合约信息
  - 格式详见本章[下载数据](#jump)部分的介绍；
  - 请注意，导入的合约代码（symbol）和交易所（exchange）两个字段组合起来，才能构成在CTA回测等模块中使用的本地代码（vt_symbol）；
  - 若合约代码为**IF2003**，交易所选择**CFFEX**（中金所），则在CtaBacktester中回测要用到的本地代码应为**IF2003.CFFEX**；
  - 可以对时间戳时区进行选择；
- 表头信息
  - 可查看CSV文件的表头信息，并将对应的表头字符串输入在表头信息中；
  - 对于CSV文件中不存在的字段（如股票数据没有【持仓量】字段），请留空即可；
- 格式信息
  - 采用Python内置库datetime模块的时间格式定义，来解析时间戳字符串；
  - 默认时间格式为"%Y-%m-%d %H:%M:%S"，对应的是"2017-1-3 0:00:00"；
  - 如果时间戳是"2017-1-3  0:00"，那么时间格式应该是"%Y-%m-%d %H:%M"。

填写完毕，则如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/22.png)

点击【确定】按钮，开始从CSV文件导入数据到数据库中。导入过程中界面会处于半卡住的情况，CSV文件越大（数据量越多），卡住的时间也会越长。成功载入之后，会弹出窗口显示载入成功，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/20.png)


## 查看数据

目前VeighNa Trader中获取数据的方式一共有三种：

- 通过数据服务或者交易接口下载

- 从CSV文件导入

- 使用DataRecorder模块录制

不管采用何种方法获取数据，点击左上角的【刷新】按钮，即可看到当前数据库中已有数据的统计情况（Tick数据除外）。刷新过程中界面可能会有偶尔的卡顿，通常对于越多的数据，卡顿的时间也会越长。刷新成功之后，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/7.png)

点击【查看】按钮，则会弹出选择数据要查看数据区间的对话框，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/10.png)

选择好要显示的数据范围后，点击【确定】按钮即可在右侧表格中看到每个时间点上具体的数据字段：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/11.png)

在数据库已有数据的前提下，点击表格最左侧【数据】列下的数据频率前的小箭头，则可展开或收起该数据频率下的合约信息显示。

若表格的右侧区域显示不完整，可拖动界面底端的横向滚动条进行调整。


## 导出数据

如果想导出数据库中的数据到本地CSV文件，则可选择要导出的合约，点击该合约所在行右侧的【导出】按钮后，会弹出选择数据区间对话框，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/8.png)

选择要导出的数据区间范围，点击【确定】后，会再次弹出对话框选择输出文件的位置，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/9.png)

选择好导出文件要放置的目录，填写完CSV文件名之后，点击【保存】按钮即可完成CSV文件的导出。


## 删除数据

若想删除特定合约数据，则可选择要删除的合约，点击该合约行数据右侧的【删除】按钮后，会弹出对话框，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/12.png)

点击【OK】按钮即可删除该合约数据，并弹出删除成功窗口，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/13.png)

此时再点击【刷新】按钮，图形界面上已经没有该合约的信息了，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/14.png)


## 更新数据

在用户**配置了数据服务**或者**交易接口（已连接）提供充足的历史数据**的情况下，点击右上角的【更新数据】按钮，即可基于图形界面上显示的所有合约数据，执行一键自动下载更新。

更新前图形界面显示如下图：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/17.png)

点击【更新数据】按钮，会弹出更新进度的信息提示对话框，如下图所示：

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/19.png)

此时DataManager会自动**从数据库中已有数据的结束日期开始，下载截止到当前最新日期**的数据，并更新到数据库中。

如果需要更新的数据较少，则可能瞬间完成更新任务，此时没有观察到更新对话框也是正常的。

更新完成后，点击左上角【刷新】按钮，即可看到该合约数据已更新至当前最新日期。

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/18.png)

## 数据范围

请注意，虽然界面上显示了数据库中已有数据的开始和结束时间，**但并不代表数据库中储存了从开始时间到结束时间之间所有的数据**。

如果依赖于交易接口提供的历史数据，一但开始时间和结束时间之间的时间跨度超过接口所能提供的数据范围，就可能导致数据之间出现缺失的情况。因此建议更新数据之后，点击【查看】按钮检查一下该合约数据是否连续。
