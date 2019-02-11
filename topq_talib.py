# -*- coding: utf-8 -*- 
'''
TopQ极宽魔改版talib金融函数库v1.0
文件名:topq_talib.py
默认缩写：tqta,示例：import topq_talib.py tqta
by Top极宽·量化开源团队 2017.8.8 首发 
	2019.01.01 升级

Top极宽量化(原zw量化)，Python量化第一品牌 
网站:www.TopQuant.vip   www.ziwang.com
QQ群: Top极宽量化总群，124134140
      
TopQuant.vip ToolBox 2016
Top极宽·量化开源工具箱 系列软件 
by Top极宽·量化开源团队 2016.12.25 首发
  

【简介】
		TopQ极宽魔改版talib金融函数库v1.0
		文件名:topq_talib.py
		默认缩写：tqta,示例：import topq_talib.py tqta

    Top极宽版talib金融函数库 ,也称 zw版talib函数库
    采用全新的pandas软件，对talib函数进行二次封装，
    提供了数十个常用的金融指标函数，与pandas无缝集成，可以直接调用。
    0.5版以pandas_talib.py的29个函数为蓝本。
    tq_talib.py1.0版，所有33个函数，均已测试通过，
    运行平台：python3.x，zwPython2016m2 以上版本   
     
     
    pandas_talib.py参见：
    https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code
    https://github.com/panpanpandas/ultrafinance/blob/master/ultrafinance/pyTaLib/pandasImpl.py
    默认数据格式，采用zwDat标准，全部小写
    ohlcv:open,high,low,close,volumns

---------zpd_talib 首批函数名称

:: ACCDIST,集散指标(A/D),Accumulation/Distribution,是由价格和成交量的变化而决定的.
:: ADX,平均趋向指数,反映趋向变动的程度,而不是方向的本身.
:: ATR均幅指标,Average True Ranger,周期内股价波动幅度的移动平均值，主要用于研判买卖时机.
:: BBANDS,布林带.Bollinger Bands.是根据统计学标准差原理设计的技术指标。它由三条轨道线组成，其中上下两条线分别可以看成是价格的压力线和支撑线,中间一条是价格平均线，
:: BBANDS_UpLow,极宽改进版的布林带talib函数。
:: CCI,顺势指标,Commodity Channel Index,是一种重点研判股价偏离度的股市分析工具。
:: COPP,估波指标,Coppock Curve,又称“估波曲线”,通过计算月度价格变化速率的加权平均值,来测量市场的动量,属于长线指标.
:: Chaikin,佳庆指标,Chaikin Oscillator,是由Marc Chaikin提出的,是A/D聚散指标的改良版本。
:: DONCH，奇安通道指标,Donchian Channel,该指标是由3条曲线组成,该指标用周期内的最高/低价,来显示市场的波动性;当其通道窄时,表示市场波动较小,反之通道宽则表示市场波动比较大。
:: EMA,指数平均数指标,Exponential Moving Average,也称EXPMA,是一种趋向类指标,对收盘价进行指数平均,用于判断价格变动趋势.
:: EOM,简易波动指标,Ease of Movement Value,又称EMV指标;它是根据等量图和压缩图的原理设计而成,是一个量价合成指标,将价格与成交量的变化,结合成一个波动指标,来反映股价或指数的变动状况.
:: FORCE,劲道指数,是一种摆荡指标,结合了三项主要数据:价格变动方向,幅度与成交量,用于衡量涨/跌势中的多/空头劲道.
:: KELCH,KC肯特纳通道,Keltner Channel,是一个移动平均通道,由上中下叁条线组成.一般以上下通道线,作为买卖机会点.
:: KST,确然指标,又称为完定指标,该指标参考长中短期的变速率ROC,以了解不同时间循环对市场的影响.该指标将数个周期的价格变动率函数作加权,以及再平滑绘制长短曲线,通过修正的价格变动组合来判断趋势,精准掌握转折买卖点。
:: KST4,极宽修订版，KST确然指标。
:: MA,移动平均线,Moving Average，即最常用的均线指标.
:: MACD,异同移动平均线,是从双指数均线发展来的,由快线减去慢线,得到快线DIF.
:: MFI,资金流量指标和比率,Money Flow Index and Ratio,又称为量相对强弱指标,Volume Relative Strength Index，VRSI,根据成交量来计测市场供需关系和买卖力道,属于量能反趋向指标.	
:: MOM,动量线,MOmentum,动量可以视为周期内,股价涨跌变动的比率.
:: MassI,梅斯线,Mass Index,是累积股价波幅宽度后,所设计的震荡曲线.在于寻找强/弱势股的反转点,是风险系数最小的震荡指标.
:: OBV,能量潮指标,On Balance Volume,通过成交量分析股价的走势。
:: PPSR,支点,又称支撑线和阻力线.Pivot Points, Supports and Resistances.该指标只是一个分析反转点的方法,常与布林带数据一起分析.
:: ROC,变动率,Rate of change,也叫做变动速度指标,变动率指标或变化速率指标,是由当前股价,与n天前的股价比较,计算其变动速度的大小.
:: RSI,相对强弱指标,Relative Strength Index,也称相对强弱指数,相对力度指数. 是通过比较平均收盘涨数,和平均收盘跌数,来分析市场的走势.
:: RSI100,极宽版RSI相对强弱指数,取0..100之间的数值.
:: STDDEV,标准偏差,Standard Deviation.
:: STOD,随机指标D值,Stochastic oscillator %D,随机指标,又称KD指标,KDJ指标综合了动量,强弱指标,及均线的优点,用来度量股价脱离价格正常范围的变异程度.
:: STOK,随机指标K值,Stochastic oscillator %K. 
:: TRIX,三重指数平滑移动平均指标，Triple Exponentially Smoothed Average.
:: TSI,真实强度指数,True Strength Index，是RSI相对强弱指数的变体,使用价格动量的双重平滑指数均线,剔除价格的震荡变化并发现趋势的变化。
:: ULTOSC,UOS终极指标,Ultimate Oscillator,依照加权的方式,将多个周期不同的振荡指标综合处理,比一般振荡指标,更能够顺应各种不同的市况.
:: Vortex,螺旋指标,Vortex Indicator，参见http://www.vortexindicator.com/VFX_VORTEX.PDF
#
#
#==================


#
mul_talib(xfun,df,ksgn='close',vlst=[5,10,15,30,50,100]):
mul_talib2x(xfun,df,ksgn='close',vlst=[5,10,15,30,50,100]):
#
:: MA(df, n):移动平均线,Moving Average，即最常用的均线指标

#
'''

import sys,os
import numpy as np
import pandas as pd


#--------------------------new.misc

def tax_mul(xfun,df,ksgn='close',vlst=[5,10,30]):
    #vlst=[5,10,15,30,50,100]
    for xd in vlst:
        #print('@mul_talib',xd,vlst)
        df=xfun(df,xd,ksgn)
        #print(df.head())
    return df

def tax_shift(df,xlst,n):
    if n>0:psgn='p'+str(n)
    elif n<0:psgn='n'+str(abs(n))
    #
    for xsgn in xlst:
        df[xsgn+psgn]=df[xsgn].shift(n)
    #
    return df

#--------------------------



#--------------------------old
    

def ACCDIST(df, n,ksgn='close'): 
    '''
    def ACCDIST(df, n,ksgn='close'): 
    #集散指标(A/D)——Accumulation/Distribution
        也称离散指标，是由价格和成交量的变化而决定的
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ad_{n}，输出数据
        若A/D指标下降，而价格上升，为卖出信号；
        若A/D指标上升，而价格下降时，为买进信号。
    '''
    #xnam='ad_{d}'.format(d=n)
    xnam='ad'
    ad = (2 * df[ksgn] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']  
    M = ad.diff(n - 1)  
    N = ad.shift(n - 1)  
    ROC = M / N  
    AD = pd.Series(ROC, name = xnam)  #'Acc/Dist_ROC_' + str(n)
    df = df.join(AD)  
    return df


def ADX(df, n, n_ADX,ksgn='close'):
    '''
    def ADX(df, n, n_ADX):
    adx，中文全称：平均趋向指数，ADX指数是反映趋向变动的程度，而不是方向的本身
    英文全称：Average Directional Index 或者Average Directional Movement Index
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        n_ADX,adx周期
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：adx_{n}_{n2}，输出数据
    '''
    i = 0
    UpI = []
    DoI = []
    #xnam='adx_{n}_{n2}'.format(n=n,n2=n_ADX)
    xnam='adx'
    while i + 1 <= len(df) - 1:  # df.index[-1]:
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        #..UpMove=df['high'].iloc[i+1]-df['high'].iloc[i]
        UpMove = df['high'].iloc[i+1] - df['high'].iloc[i]
        DoMove = df['low'].iloc[i] - df['low'].iloc[i+1]
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    i = 0
    TR_l = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #TR = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))
        TR = max(df['high'].iloc[i+1], df[ksgn].iloc[i]) - min(df['low'].iloc[i+1], df[ksgn].iloc[i])
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l)
    #ATR = pd.Series(pd.ewma(TR_s, span=n, min_periods=n))
    ATR = TR_s.ewm(span=n,min_periods=n-1,adjust=True,ignore_na=False).mean() 
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI =UpI.ewm(span=n,min_periods=n-1,adjust=True,ignore_na=False).mean()/ ATR
    NegDI =DoI.ewm(span=n,min_periods=n-1,adjust=True,ignore_na=False).mean()/ ATR
    #PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1) / ATR)
    #NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1) / ATR)
    xp=abs(PosDI - NegDI) / (PosDI + NegDI)*100
    xp5=xp.ewm(span=n_ADX,min_periods=n_ADX-1,adjust=True,ignore_na=False).mean()
    #ds = pd.Series(pd.ewma(abs(PosDI - NegDI) / (PosDI + NegDI), span=n_ADX, min_periods=n_ADX - 1), name=xnam)
    ds = pd.Series(xp5,name=xnam)
    ds.index=df.index
    df[xnam]=ds
    #df = df.join(ds)  
    return df


def ATR(df, n,ksgn='close'):  
    '''
    def ATR(df, n,ksgn='close'):  
    #ATR,均幅指标（Average True Ranger）,取一定时间周期内的股价波动幅度的移动平均值，主要用于研判买卖时机
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：atr_{n}，输出数据
     该指标价值越高，趋势改变的可能性就越高；该指标的价值越低，趋势的移动性就越弱。   
    [14,14,100,100]
    '''    
    #xnam='atr_{n}'.format(n=n)
    xnam='atr'
    i = 0
    TR_l = [0]
    while i < len(df) - 1:  # df.index[-1]:
    # for i, idx in enumerate(df.index)
        # TR=max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        #TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
        TR = max(df['high'].iloc[i + 1], df[ksgn].iloc[i] - min(df['low'].iloc[i + 1], df[ksgn].iloc[i]))
        TR_l.append(TR)
        i = i + 1;#print('#',i,TR)
    TR_s = pd.Series(TR_l)
    #ds = pd.Series(pd.ewma(TR_s, span=n, min_periods=n), name=xnam)
    ds = TR_s.ewm(span=n,min_periods=n,adjust=True,ignore_na=False).mean()
    #df = df.join(ds)  
    ds.index=df.index;df[xnam]=ds
    #print('ds',ds.head())
    return df
    


def BBANDS(df, n,ksgn='close'):  
    '''
    def BBANDS(df, n,ksgn='close'):  
    布林带.Bollinger Bands  
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：_{n}，_{n}b，输出数据
    '''    
    #xnam='boll_{n}'.format(n=n)
    xnam='boll'
    MA = df[ksgn].rolling(window=n,center=False).mean()
    MSD = df[ksgn].rolling(window=n,center=False).std()
    b1 = 4 * MSD / MA  
    B1 = pd.Series(b1, name = xnam+'b')  
    df = df.join(B1)  
    b2 = (df[ksgn] - MA + 2 * MSD) / (4 * MSD)  
    B2 = pd.Series(b2, name = xnam)  
    df = df.join(B2)  
    return df    


def BBANDS_UpLow(df, n,ksgn='close'):  
    '''
    BBANDS_UpLow(df, n,ksgn='close'):  
    zw改进版的布林带talib函数.Bollinger Bands  
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了4栏：
            boll_ma，布林带均线数据
            boll_std，布林带方差据
            boll_up，布林带上轨带差据
            boll_low，布林带下轨带差据
    '''        
    #df['boll_ma']=pd.Series(pd.rolling_mean(df[ksgn], n))  
    #df['boll_std']= pd.Series(pd.rolling_std(df[ksgn], n))  
    df['boll_ma']=df[ksgn].rolling(window=n,center=False).mean()
    df['boll_std']=df[ksgn].rolling(window=n,center=False).std()
    #df[#MSD = pd.Series(pd.rolling_std(df[ksgn], n))  
    MA=df['boll_ma']
    MSD=df['boll_std']
    #
    knum=2
    df['boll_up']= MA + MSD * knum    #knum=numStdDev
    df['boll_low']= MA - MSD * knum

    return df 


def CCI(df, n,ksgn='close'):  
    '''
    def CCI(df, n,ksgn='close'):  
    CCI顺势指标(Commodity Channel Index)
    CCI指标，是由美国股市分析家唐纳德·蓝伯特（Donald Lambert）所创造的，是一种重点研判股价偏离度的股市分析工具。

    
    MA是简单平均线，也就是平常说的均线
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：cci_{n}，输出数据
    '''
    #xnam='cci_{d}'.format(d=n)
    xnam='cci'
    PP = (df['high'] + df['low'] + df[ksgn]) / 3  
    #CCI = pd.Series((PP - pd.rolling_mean(PP, n)) / pd.rolling_std(PP, n), name = xnam)  
    MA = PP.rolling(window=n,center=False).mean()
    MSD = PP.rolling(window=n,center=False).std()
    CCI= pd.Series((PP - MA) / MSD, name = xnam)
    df = df.join(CCI)  
    
    return df
    

#Coppock Curve  
def COPP(df, n,ksgn='close'):  
    '''
    def COPP(df, n):  				
　　估波指标（Coppock Curve）又称“估波曲线”，通过计算月度价格的变化速率的加权平均值来测量市场的动量，属于长线指标。
　　估波指标由Edwin·Sedgwick·Coppock于1962年提出，主要用于判断牛市的到来。
    该指标用于研判大盘指数较为可靠，一般较少用于个股；再有，该指标只能产生买进讯号。
    依估波指标买进股票后，应另外寻求其他指标来辅助卖出讯号。
    估波指标的周期参数一般设置为11、14，加权平均参数为10，也可以结合指标的平均线进行分析

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：copp_{n}，输出数据
    '''
    #xnam='copp_{d}'.format(d=n)
    xnam='copp'
    M = df[ksgn].diff(int(n * 11 / 10) - 1)  
    N = df[ksgn].shift(int(n * 11 / 10) - 1)  
    ROC1 = M / N  
    M = df[ksgn].diff(int(n * 14 / 10) - 1)  
    N = df[ksgn].shift(int(n * 14 / 10) - 1)  
    ROC2 = M / N  
    #MROC=pd.Series(ROC1+ROC2)
    #Copp = MROC(span = n, min_periods = n,adjust=True,ignore_na=False).mean()
    m1=ROC1.ewm(span=n,min_periods=n,adjust=True,ignore_na=False).mean()
    m2=ROC2.ewm(span=n,min_periods=n,adjust=True,ignore_na=False).mean()
    Copp = pd.Series(m1+m2, name = xnam)  
    #Copp = pd.Series(pd.ewma(ROC1 + ROC2, span = n, min_periods = n), name = xnam)  
    df = df.join(Copp)  
    return df
    
#Chaikin Oscillator  
def CHAIKIN(df,n,ksgn='close'):   
    '''
    def CHAIKIN(df):					
    #佳庆指标（Chaikin Oscillator）
　　佳庆指标（CHAIKIN）是由马可·蔡金（Marc Chaikin）提出的，聚散指标（A/D）的改良版本。
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
        n=27,
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ck，输出数据
    '''
    
    xnam='ck'
    n3=max(n/3,1)   #n>=3
    ad = (2 * df[ksgn] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']  
    #Chaikin = pd.Series(pd.ewma(ad, span = 3, min_periods = 2) - pd.ewma(ad, span = 10, min_periods = 9), name = xnam)  
    ad1=ad.ewm(span = n3, min_periods = n3-1,adjust=True,ignore_na=False).mean()
    ad9=ad.ewm(span =n , min_periods = n-1,adjust=True,ignore_na=False).mean()
    Chaikin = pd.Series(ad1-ad9, name = xnam)  
    df = df.join(Chaikin)  
    return df
    

#Donchian Channel  
def DONCH(df, n):  
    '''
    def DONCH(df, n):      
      #唐奇安通道指标,Donchian Channel  
	该指标是由Richard Donchian发明的，是有3条不同颜色的曲线组成的，该指标用周期（一般都是20）内的最高价和最低价来显示市场的波动性
	当其通道窄时表示市场波动较小，反之通道宽则表示市场波动比较大。
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：donchsr，中间输出数据
            donch，输出数据
    '''
    #xnam='donch_{d}'.format(d=n)
    xnam='donch'
    i = 0  
    DC_l = []  
    while i < n - 1:  
        DC_l.append(0)  
        i = i + 1  
    i = 0  
    while (i + n - 1) <=(len(df) - 1):  #df.index[-1]:  
        #DC = max(df['high'].ix[i:i + n - 1]) - min(df['low'].ix[i:i + n - 1])  
        DC = max(df['high'].iloc[i:i + n - 1]) - min(df['low'].iloc[i:i + n - 1])  
        DC_l.append(DC)  
        i = i + 1  
    #
    #DC_l.append(DC)  
    #
    DonCh = pd.Series(DC_l, name = xnam)   #'Donchian_' + str(n)
    
    #df = df.join(DonCh)  
    DonCh.index=df.index;
    df[xnam+'_sr']=DonCh
    df[xnam]=df[xnam+'_sr'].shift(n - 1)  
    #DonCh = DonCh.shift(n - 1)  
    return df
    
def DONCH_ext(df, n):  
    '''
    def DONCH(df, n):      
      #唐奇安通道指标,Donchian Channel  
	该指标是由Richard Donchian发明的，是有3条不同颜色的曲线组成的，该指标用周期（一般都是20）内的最高价和最低价来显示市场的波动性
	当其通道窄时表示市场波动较小，反之通道宽则表示市场波动比较大。
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：donchsr，中间输出数据
            donch，输出数据
    '''
    #xnam='donch_{d}'.format(d=n)
    xnam='donch'
    df['dc_up']=df['high'].rolling(window=n,center=False).max()
    df['dc_low']=df['low'].rolling(window=n,center=False).min()
    df['dc_mid']=(df['dc_up']+df['dc_low'])/2
    #
    return df
    


def EMA(df, n,ksgn='close'):  
    '''
    EMA(df, n,ksgn='close'):  
    #Exponential Moving Average  
    EMA是指数平滑移动平均线，也叫EXPMA指标，也称为：SMMA 
    是平均线的一个变种，EMA均线较MA更加专业一些。
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ema，输出数据
    '''
    #xnam='ema_{n}'.format(n=n)
    xnam='ema'
    ds=df[ksgn].ewm(span = n).mean()
    EMA = pd.Series(ds, name = xnam)  
    #EMA = pd.Series(pd.ewma(df[ksgn], span = n, min_periods = n - 1), name = xnam)  
    df = df.join(EMA)  
    return df    
   
    

def EMA_ext(df, n,ksgn='close'):  
    '''
    EMA(df, n,ksgn='close'):  
    #Exponential Moving Average  
    EMA是指数平滑移动平均线，也叫EXPMA指标，也称为：SMMA 
    是平均线的一个变种，EMA均线较MA更加专业一些。
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ema，输出数据
    '''
    #xnam='ema_{n}'.format(n=n)
    xnam='ema'
    n=max(n,2)
    #EMA = pd.Series(pd.ewma(df[ksgn], span = n, min_periods = n - 1), name = xnam)  
    dma=df[ksgn].ewm(span=n,min_periods=n-1,adjust=True,ignore_na=False).mean()
    #EMA = pd.Series(pd.ewma(df[ksgn], span = n, min_periods = n - 1), name = xnam)  
    EMA = pd.Series(dma, name = xnam)  
    df = df.join(EMA)  
    #
    df['xnum']=0  # =1:buy; =-1:sell
    df.loc[df.dprice>df.ema,'xnum']=1
    df.loc[df.dprice<df.ema,'xnum']=-1
    df['xsum']=df['xnum'].rolling(window=n,center=False).sum()
    df['kema']=df['xsum']/n*100
    #
    return df    


#Ease of Movement  
def EOM(df, n):   
    '''
    def EOM(df, n):  					
    简易波动指标(Ease of Movement Value)，又称EMV指标
   它是由RichardW．ArmJr．根据等量图和压缩图的原理设计而成,目的是将价格与成交量的变化结合成一个波动指标来反映股价或指数的变动状况。
   由于股价的变化和成交量的变化都可以引发该指标数值的变动,因此,EMV实际上也是一个量价合成指标。


    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：eom_{n}，输出数据
            eom_x，10e10倍的输出数据
    '''
    #xnam='eom_{d}'.format(d=n)
    xnam='eom'
    EoM = (df['high'].diff(1) + df['low'].diff(1)) * (df['high'] - df['low']) / (2 * df['volume'])  
    #Eom_ma = pd.Series(pd.rolling_mean(EoM, n), name = xnam)  
    Eom_ma = pd.Series(EoM.rolling(window=n,center=False).mean(), name = xnam)  
    df = df.join(Eom_ma)  
    df['eom_x']=df[xnam]*10e8  #10e10
    return df



def FibPR(df, price='close'):
    """
    Fibonacci Price Retracements 
    斐波纳契价格回调(黄金分割线)指数
    
    """
    #p0618 = np.pi - 1
    #p0381 = 1 - p0618
    p0618,p0381 =0.618,0.381
    #
    #p= pd.Series(df[price])
    df['fib']=df[price]
    df['fib618']=df[price]*(1+p0618)
    df['fib381']=df[price]*(1+p0381)
    df['fib-381']=df[price]*(1-p0381)
    df['fib-618']=df[price]*(1-p0618)
    #
    return df

def FORCE(df, n,ksgn='close'):   
    '''
    def FORCE(df, n):					
    #劲道指数(Force Index)
　　劲道指数是由亚历山大·埃尔德(Alexander Elder)博士设计的一种摆荡指标，藉以衡量每个涨势中的多头劲道与每个跌势中的空头劲道。
　　劲道指数结合三项主要的市场资讯：价格变动的方向、它的幅度与成交量。它是由一个崭新而实用的角度，把成交量纳入交易决策中。
   短线的交易，则在劲道指数翻为正值时卖出，在劲道指数翻为负值时回补
   
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：force__{n}，输出数据
          force_x，缩小10e7倍的输出数据
    '''
    #xnam='force_{d}'.format(d=n)
    xnam='force'
    F = pd.Series(df[ksgn].diff(n) * df['volume'].diff(n), name = xnam)  
    df = df.join(F)  
    df['force_x']=df[xnam]/10e7
    return df

  
def KDJ(df, n,n3,ksgn='close'):    
    '''
    def KDJ(df, n,ksgn='close'):     
       KDJ 随机指标D值,Stochastic oscillator %D  
	随机指标，又称KD指标，KDJ指标
    根据目前股价在近阶段股价分布中的相对位置来预测可能发生的趋势反转
　   随机指标综合了动量观念、强弱指标及移动平均线的优点，用来度量股价脱离价格正常范围的变异程度。
　   KD指标考虑的不仅是收盘价，而且有近期的最高价和最低价，这避免了仅考虑收盘价而忽视真正波动幅度的弱点。
　  随机指标一般是根据统计学的原理，通过一个特定的周期（常为9日、9周等）内出现过的最高价、最低价
  及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值RSV，
  然后根据平滑移动平均线的方法来计算K值、D值与J值，并绘成曲线图来研判股票走势。
  K与D值永远介于0到100之间。D大于80时，行情呈现超买现象。D小于20时，行情呈现超卖现象。
  上涨趋势中，K值小于D值，K线向上突破D线时，为买进信号。下跌趋势中，K值大于D值，K线向下跌破D线时，为卖出信号。
买进信号：K值在上涨趋势中﹤D值，K线向上突破D线时；
卖出信号：K值在下跌趋势中﹥D值，K线向下跌破D线。
    
算法
首先要计算周期的RSV值，然后再计算K值、D值、J值。以9日周期的KDJ为例：
对每一交易日求RSV（未成熟随机值）
RSVt=(Ct-L9)/(H9-L9)*100    （Ct=当日收盘价；L9=9天内最低价；H9=9天内最高价）
RSV=（收盘价-最近N日最低价）/（最近N日最高价-最近N日最低价）* 100
K线：RSV的M1日移动平均,K值为RSV值3日平滑移动平均线，公式为：Kt=RSVt/3+2*t-1/3
D线：K值得M2日移动平均,D值为K值的3日平滑移动平均线，公式为：Dt=Kt/3+2*Dt-1/3
J线：3D-2K。J值为三倍K值减两倍D值，公式为：Jt=3*Dt-2*Kt
参数
N，M1 。M2 天数，一般为9，3，3
用法
（1）D大于80 ，超买； D小于20，超卖；J大于100%，超买；J小于10%，超卖。
 （2）指标线K向上突破指标线D，买进信号；指标线K向下跌破指标线D，卖出信号。
 （3）指标线K与指标线D的交叉发生在70以上和30以下才有效。、
 （4）KDJ指标不适于发行量小，交易不活跃的股票。
 （%）KDJ指标对于大盘和热门大盘股有极高准确性。
 
       
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：stod，输出数据
    '''
    #xnam='stod'
    xnam='kdj'
    #m1,m2=round(n/3),round(n/3) n3=n/3
    cn=df[ksgn]
    ln=df['low'].rolling(window=n,center=False).min()
    hn=df['high'].rolling(window=n,center=False).max()
    df['rsv']=(cn-ln)/(hn-ln)*100
    #df['rsv1p']=df['rsv'].shift(1)
    #
    df['kdj_k']=MA01(df,n3,'rsv')
    df['kdj_d']=MA01(df,n3,'kdj_k')
    df['kdj_j']=df['kdj_k']*3-df['kdj_d']*2
    #df['k1p'],df['d1p']=50,50
    #df['kdj_k']=df['k1p']*2/3+df['rsv']/3
    #df['kdj_d']=df['d1p']*2/3+df['kdj_k']/3
    #df['kdj_j']=df['kdj_k']*3-df['kdj_d']*2
    
    
    #print('n df',len(df))
    return df

def KELCH(df, n,ksgn='close'):
    '''
    def KELCH(df, n):  				#肯特纳通道（Keltner Channel，KC）
　　肯特纳通道（KC）是一个移动平均通道，由叁条线组合而成(上通道、中通道及下通道)。
	KC通道，一般情况下是以上通道线及下通道线的分界作为买卖的最大可能性。
  	若股价於边界出现不沉常的波动，即表示买卖机会。    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了3栏：kc_m，中间数据
            kc_u，up上轨道数据
            kc_d，down下轨道数据
    '''
    xnam='kc_m'
    xnam2='kc_u'
    xnam3='kc_d'
    ds=(df['high'] + df['low'] + df[ksgn]) / 3
    KelChM =pd.Series(ds.rolling(window=n,center=False).mean(), name = xnam)  #'KelChM_' + str(n)
    ds=(4 * df['high'] - 2 * df['low'] + df[ksgn]) / 3
    KelChU = pd.Series(ds.rolling(window=n,center=False).mean(), name = xnam2)   #'KelChU_' + str(n)
    ds=(-2 * df['high'] + 4 * df['low'] + df[ksgn]) / 3
    KelChD = pd.Series(ds.rolling(window=n,center=False).mean(), name =xnam3)    #'KelChD_' + str(n)
    #KelChM = pd.Series(pd.rolling_mean((df['high'] + df['low'] + df[ksgn]) / 3, n), name = xnam)  #'KelChM_' + str(n)
    #KelChU = pd.Series(pd.rolling_mean((4 * df['high'] - 2 * df['low'] + df[ksgn]) / 3, n), name = xnam2)   #'KelChU_' + str(n)
    #KelChD = pd.Series(pd.rolling_mean((-2 * df['high'] + 4 * df['low'] + df[ksgn]) / 3, n), name =xnam3)    #'KelChD_' + str(n)
    #
    df = df.join(KelChM)  
    df = df.join(KelChU)  
    df = df.join(KelChD)  
    
    return df



def KST(df, vlst,ksgn='close'): 
#def KST(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    '''
    def KST(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    #KST Oscillator  
    确然指标（KST）又称为完定指标，该指标参考长、中、短期的变速率ROC，以了解不同时间循环对市场的影响。
    该指标将数个周期的价格变动率函数作加权以及再平滑绘制长短曲线，其特色在通过修正的价格变动组合来判断趋势，精准掌握转折买卖点。
    
    tst:
       (r1, r2, r3, r4, n1, n2, n3, n4) = (1, 2, 3, 4, 6, 7, 9, 9)
    '''
    '''
    
    【输入】
        df, pd.dataframe格式数据源
        r1..r4,n1..n4，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ksf，输出数据
    '''
    xnam='kst';
    [r1, r2, r3, r4, n1, n2, n3, n4] =vlst
    #
    M = df[ksgn].diff(r1 - 1)  
    N = df[ksgn].shift(r1 - 1)  
    ROC1 = M / N  
    M = df[ksgn].diff(r2 - 1)  
    N = df[ksgn].shift(r2 - 1)  
    ROC2 = M / N  
    M = df[ksgn].diff(r3 - 1)  
    N = df[ksgn].shift(r3 - 1)  
    ROC3 = M / N  
    M = df[ksgn].diff(r4 - 1)  
    N = df[ksgn].shift(r4 - 1)  
    ROC4 = M / N  
    #'KST_' + str(r1) + '_' + str(r2) + '_' + str(r3) + '_' + str(r4) + '_' + str(n1) + '_' + str(n2) + '_' + str(n3) + '_' + str(n4)
    roc1x=ROC1.rolling(window=n1,center=False).sum()
    roc2x=ROC2.rolling(window=n2,center=False).sum()
    roc3x=ROC3.rolling(window=n3,center=False).sum()
    roc4x=ROC4.rolling(window=n4,center=False).sum()
    #KST = pd.Series(pd.rolling_sum(ROC1, n1) + pd.rolling_sum(ROC2, n2) * 2 + pd.rolling_sum(ROC3, n3) * 3 + pd.rolling_sum(ROC4, n4) * 4, name = xnam)  
    KST = pd.Series(roc1x+roc2x *2+roc3x *3+roc4x *4, name = xnam)  
    df = df.join(KST)  
    return df


def KST4(df, vlst,ksgn='close'): 	
#def KST4(df, r1, r2, r3, r4,ksgn='close'): 
    '''
    def KST4(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    zw修订版，KST确然指标
    确然指标（KST）又称为完定指标，该指标参考长、中、短期的变速率ROC，以了解不同时间循环对市场的影响。
    该指标将数个周期的价格变动率函数作加权以及再平滑绘制长短曲线，其特色在通过修正的价格变动组合来判断趋势，精准掌握转折买卖点。
    
    tst:
       (r1, r2, r3, r4) = (9,13,18,24);(12,20,30,40)
    
    【输入】
        df, pd.dataframe格式数据源
        r1,r2,r3,r4，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ksf，输出数据
    
    '''
    [r1, r2, r3, r4] =vlst
    vlst8=[r1, r2, r3, r4]+[r1, r2, r3, r4]
    #df=KST(df,r1, r2, r3, r4,r1, r2, r3, r4,ksgn)
    df=KST(df,vlst8, ksgn)
    
    return df


       
def MA(df, n,ksgn='close'):  
    '''
    def MA(df, n,ksgn='close'):  
    #Moving Average  
    MA是简单平均线，也就是平常说的均线
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ma_{n}，均线数据
    '''
    #xnam='ma_{n}'.format(n=n)
    xnam='ma'
    #ds5 = pd.Series(pd.rolling_mean(df[ksgn], n), name =xnam)  
    ds2=pd.Series(df[ksgn], name =xnam,index=df.index);
    ds5 = ds2.rolling(center=False,window=n).mean() 
    #print(ds5.head()); 
    #print(df.head())
    #
    df = df.join(ds5)  
    #
    return df
   
def MA_n(df, n,ksgn='close'):  
    '''
    def MA(df, n,ksgn='close'):  
    #Moving Average  
    MA是简单平均线，也就是平常说的均线
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ma_{n}，均线数据
    '''
    xnam='ma_{n}'.format(n=n)
    #xnam='ma'
    #ds5 = pd.Series(pd.rolling_mean(df[ksgn], n), name =xnam)  
    ds2=pd.Series(df[ksgn], name =xnam,index=df.index);
    ds5 = ds2.rolling(center=False,window=n).mean() 
    #print(ds5.head()); 
    #print(df.head())
    #
    df = df.join(ds5)  
    #
    return df
       
   
def MA01(df, n,ksgn='close'):  
    '''
    def MA(df, n,ksgn='close'):  
    #Moving Average  
    MA是简单平均线，也就是平常说的均线
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ma_{n}，均线数据
    '''
    #xnam='ma_{n}'.format(n=n)
    #xnam='ma'
    #ds5 = pd.Series(pd.rolling_mean(df[ksgn], n), name =xnam)  
    #ds2=pd.Series(df[ksgn], name =xnam);
    ds5 = df[ksgn].rolling(center=False,window=n).mean() 
    #print(ds5.head()); print(df.head())
    #df = df.join(ds5)  
    
    return ds5



#MACD, MACD Signal and MACD difference  
def MACD010(df, n_fast, n_slow,ksgn='close'): 
    '''
    def MACD(df, n_fast, n_slow):           
      #MACD指标信号和MACD的区别, MACD Signal and MACD difference   
	MACD是查拉尔·阿佩尔(Geral Appel)于1979年提出的，由一快及一慢指数移动平均（EMA）之间的差计算出来。
	“快”指短时期的EMA，而“慢”则指长时期的EMA，最常用的是12及26日EMA：

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了3栏：macd,sign,mdiff
        sign=macd_9
        dif=macd-macd_9
        [12,26]
    '''
    #xnam='macd'.format(n=n_fast,n2=n_slow)
    #xnam2='msign'.format(n=n_fast,n2=n_slow)
    #xnam3='mdiff'.format(n=n_fast,n2=n_slow)
    xnam='macd'
    xnam2='msign'
    xnam3='mdiff'
    EMAfast = df[ksgn].ewm(span = n_fast, min_periods = n_fast - 1).mean()
    EMAslow = df[ksgn].ewm(span = n_slow, min_periods = n_slow - 1).mean()  
    MACD = pd.Series(EMAfast - EMAslow, name = xnam)  #dif
    xnum=max(int((n_fast+n_slow)/4),2)
    #MACDsign = MACD.ewm(span = 9, min_periods = 8).mean() #DEA or DEM   
    MACDsign = MACD.ewm(span = xnum, min_periods = xnum-1).mean() #DEA or DEM   
    MACDsign.name=xnam2
    MACDdiff = pd.Series(MACD - MACDsign, name =xnam3)  
    df = df.join(MACD)  
    df = df.join(MACDsign)  
    df = df.join(MACDdiff)  
    return df
    
def MACD020(df, n_fast, n_slow,ksgn='close'): 
    '''
    def MACD(df, n_fast, n_slow):           
      #MACD指标信号和MACD的区别, MACD Signal and MACD difference   
	MACD是查拉尔·阿佩尔(Geral Appel)于1979年提出的，由一快及一慢指数移动平均（EMA）之间的差计算出来。
	“快”指短时期的EMA，而“慢”则指长时期的EMA，最常用的是12及26日EMA：

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了3栏：macd,sign,mdiff
        sign=macd_9
        dif=macd-macd_9
        [12,26]
    '''
    #xnam='macd'.format(n=n_fast,n2=n_slow)
    #xnam2='msign'.format(n=n_fast,n2=n_slow)
    #xnam3='mdiff'.format(n=n_fast,n2=n_slow)
    xnam='mdiff' #'macd'
    xnam2='mdea' #'msign'
    xnam3='macd' #'mdiff'
    EMAfast = df[ksgn].ewm(span = n_fast, min_periods = n_fast - 1).mean()
    EMAslow = df[ksgn].ewm(span = n_slow, min_periods = n_slow - 1).mean()  
    mdiff = pd.Series(EMAfast - EMAslow, name = xnam)  #dif
    xnum=max(int((n_fast+n_slow)/4),2)
    #MACDsign = MACD.ewm(span = 9, min_periods = 8).mean() #DEA or DEM   
    mdea = mdiff.ewm(span = xnum, min_periods = xnum-1).mean() #DEA or DEM   
    mdea.name=xnam2
    macd = pd.Series(mdiff - mdea, name =xnam3)  
    df = df.join(macd)  
    df = df.join(mdea)  
    df = df.join(mdiff)  
    return df
    

#pd.ewm_mean is deprecated for Series and will be removed in a future version, replace with 
        #Series.ewm(span=12,min_periods=15,adjust=True,ignore_na=False).mean()

def MFI(df, n,ksgn='close'):   
    '''
    def MFI(df, n):					
    MFI,资金流量指标和比率,Money Flow Index and Ratio
　　资金流量指标又称为量相对强弱指标（Volume Relative Strength Index，VRSI），
	英文全名Money Flow Index，缩写为MFI，根据成交量来计测市场供需关系和买卖力道。
	该指标是通过反映股价变动的四个元素：上涨的天数、下跌的天数、成交量增加幅度、成交量减少幅度
	来研判量能的趋势，预测市场供求关系和买卖力道，属于量能反趋向指标。	    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：mfi，输出数据
    '''
    #xnam='mfi_{d}'.format(d=n)
    xnam='mfi'
    PP = (df['high'] + df['low'] + df[ksgn]) / 3  
    i = 0  
    PosMF = [0]  
    while i <(len(df) - 1): #df.index[-1]:  
        if PP.iloc[i + 1] > PP.iloc[i]:  
            #PosMF.append(PP[i + 1] * df.get_value(i + 1, 'volume'))  
            PosMF.append(PP.iloc[i + 1] * df['volume'].iloc[i + 1])  
        else:  
            PosMF.append(0)  
        i = i + 1  
    #    
    PosMF = pd.Series(PosMF)  
    TotMF = PP * df['volume']  
    #MFR = pd.Series(PosMF / TotMF)  
    PosMF.index=TotMF.index
    MFR =PosMF / TotMF
    
    #MFI = pd.Series(pd.rolling_mean(MFR, n), name = xnam)  
    MFI = pd.Series(MFR.rolling(window=n,center=False).mean(), name = xnam)  
    #df = df.join(MFI)  
    #MFI.index=df.index;
    df[xnam]=MFI
    return df
    
def MOM(df, n,ksgn='close'):  
    '''
    
    def MOM(df, n,ksgn='close'):  
　　动量线，英文全名MOmentum，简称MOM。“动量”这一名词，市场上的解释相当广泛。以Momentum命名的指标，种类更是繁多。
		综合而言，动量可以视为一段期间内，股价涨跌变动的比率。
    
    动量指标.Momentum  
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：mom，输出数据
    '''
    #xnam='mom_{n}'.format(n=n)
    xnam='mom'
    #M = pd.Series(df['close'].diff(n), name = 'Momentum_' + str(n))  
    M = pd.Series(df[ksgn].diff(n), name = xnam)  
    df = df.join(M)  
    return df
    

def MASS(df,n=25):  
    '''
    def MassI(df):					
    梅斯线（Mass Index）
　　梅斯线是Donald Dorsey累积股价波幅宽度之后，所设计的震荡曲线。
		本指标最主要的作用，在于寻找飙涨股或者极度弱势股的重要趋势反转点。
　　MASS指标是所有区间震荡指标中，风险系数最小的一个。		
    
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：mass，输出数据
    '''
    xnam='mass'
    Range = df['high'] - df['low']  
    EX1 =Range.ewm(span=9,min_periods=8,adjust=True,ignore_na=False).mean()
    EX2 =EX1.ewm(span=9,min_periods=8,adjust=True,ignore_na=False).mean()
    Mass = EX1 / EX2  
    MassI = pd.Series(Mass.rolling(window=n,center=False).sum(), name = xnam)  #'Mass Index'
    df = df.join(MassI)  
    return df    
    

def OBV(df, n,ksgn='close'):   
    '''
    def OBV(df, n,ksgn='close'):   
    #能量潮指标（On Balance Volume，OBV）
    OBV指标是葛兰维（Joe Granville）于本世纪60年代提出的，并被广泛使用。
    股市技术分析的四大要素：价、量、时、空。OBV指标就是从“量”这个要素作为突破口，来发现热门股票、分析股价运动趋势的一种技术指标。
    它是将股市的人气——成交量与股价的关系数字化、直观化，以股市的成交量变化来衡量股市的推动力，从而研判股价的走势。
    关于成交量方面的研究，OBV能量潮指标是一种相当重要的分析指标之一。    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：obv，输出数据
        obv_x，放大10e6倍的输出数据
    '''
    #xnam='obv_{d}'.format(d=n)
    xnam='obv'
    i = 0  
    OBV = [0]  
    while i <  len(df) - 1:  #df.index[-1]
        #if df.get_value(i + 1, ksgn) - df.get_value(i, ksgn) > 0:  
        if df[ksgn].iloc[i+1]-df[ksgn].iloc[i] > 0:  
            #OBV.append(df.get_value(i + 1, 'Volume'))  
            OBV.append(df['volume'].iloc[i + 1])  
        if (df[ksgn].iloc[i+1]-df[ksgn].iloc[i]) == 0:  
            OBV.append(0)  
        if (df[ksgn].iloc[i+1]-df[ksgn].iloc[i]) < 0:  
            OBV.append(-df['volume'].iloc[i + 1])  
        i = i + 1  
    OBV = pd.Series(OBV)  
    #OBV_ma = pd.Series(pd.rolling_mean(OBV, n), name = xnam)  
    OBV_ma = pd.Series(OBV.rolling(window=n,center=False).mean(), name = xnam)  
    
    #df = df.join(OBV_ma)  
    OBV_ma.index=df.index;
    df[xnam]=OBV_ma
    df['obv_x']=df[xnam]/10e6
    return df
    
    



def PPSR(df):  
    '''
    def PPSR(df):  					
     支点，支撑线和阻力线.Pivot Points, Supports and Resistances  
	PIVOT指标的观念很简单，不需要计算任何东西，它纯粹只是一个分析反转点的方法而已。
	PIVOT意思是指“轴心”，轴心是用来确认反转的基准，所以PIVOT指标其实就是找轴心的方法
     PIVOT指标，经常与布林带数据一起分析。

    【输入】
        df, pd.dataframe格式数据源
    【输出】    
        df, pd.dataframe格式数据源,
        增加了7栏：pp,s1,s2,s3,r1,r2,r3，输出数据
    '''
    PP = pd.Series((df['high'] + df['low'] + df['close']) / 3)  
    R1 = pd.Series(2 * PP - df['low'])  
    S1 = pd.Series(2 * PP - df['high'])  
    R2 = pd.Series(PP + df['high'] - df['low'])  
    S2 = pd.Series(PP - df['high'] + df['low'])  
    R3 = pd.Series(df['high'] + 2 * (PP - df['low']))  
    S3 = pd.Series(df['low'] - 2 * (df['high'] - PP))  
    psr = {'pp':PP, 'r1':R1, 's1':S1, 'r2':R2, 's2':S2, 'r3':R3, 's3':S3}  
    PSR = pd.DataFrame(psr)  
    df = df.join(PSR)  
    
    return df
    


def ROC(df, n,ksgn='close'):  

    '''
    def ROC(df, n,ksgn='close'):  
    变动率(Rate of change,ROC)
　　ROC是由当天的股价与一定的天数之前的某一天股价比较，其变动速度的大小,来反映股票市场变动的快慢程度。
		ROC，也叫做变动速度指标、变动率指标或变化速率指标。
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：roc，输出数据
    '''
    #xnam='roc_{n}'.format(n=n)
    xnam='roc'
    M = df[ksgn].diff(n - 1)  
    N = df[ksgn].shift(n - 1)  
    ROC = pd.Series(M / N, name = xnam) *1000 
    df = df.join(ROC)  
    return df




def RSI(df, n):
    '''
    def RSI(df, n):  					
      #RSI，相对强弱指标,Relative Strength Index
	也称相对强弱指数、相对力度指数
	RSI，是通过比较一段时期内的平均收盘涨数和平均收盘跌数来分析市场买沽盘的意向和实力，从而作出未来市场的走势。
	RSI通过特定时期内股价的变动情况计算市场买卖力量对比，来判断股票价格内部本质强弱、推测价格未来的变动方向的技术指标。

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度,一般为14
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：rsi，输出数据
    '''
    #xnam='rsi_{n}'.format(n=n)
    xnam='rsi'
    #print( xnam)
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        UpMove=df['high'].iloc[i+1]-df['high'].iloc[i]
        DoMove=df['low'].iloc[i]-df['low'].iloc[i+1]

        #Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    #PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1))
    #NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1))
    PosDI =UpI.ewm(span=n, min_periods=n - 1,adjust=True,ignore_na=False).mean()
    NegDI =DoI.ewm(span=n, min_periods=n - 1,adjust=True,ignore_na=False).mean()
    
    ds = pd.Series(PosDI / (PosDI + NegDI), name=xnam)
    #df = df.join(ds)
    #print('rsi')
    #print(len(ds),len(df))
    ds.index=df.index
    df[xnam]=ds*100
    return df



def RSI100(df, n):

    '''
    ???? def RSI100(df, n): ???//
        zw版RSI相对强弱指数，取0..100之间的数值
    
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：rsi，输出数据
          rsi_k，中间输出数据
    '''    
    #xnam='rsi_{n}'.format(n=n)
    xnam='rsi'
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        UpMove=df['high'].iloc[i+1]-df['high'].iloc[i];
        DoMove=df['low'].iloc[i]-df['low'].iloc[i+1];
        
        #Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    #PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1))
    #NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1))
    PosDI =UpI.ewm(span=n, min_periods=n - 1,adjust=True,ignore_na=False).mean()
    NegDI =DoI.ewm(span=n, min_periods=n - 1,adjust=True,ignore_na=False).mean()
    #ds = pd.Series(PosDI / (PosDI + NegDI))
    ds = pd.Series(PosDI / (PosDI + NegDI))
    ds.index=df.index
    #print(ds.tail())
    #df = df.join(ds)  
    #df[xnam]=ds;
    df['rsi_k']=ds;
    df[xnam]=100-100/(1+df['rsi_k']);
    
    return df
    


def STDDEV(df, n,ksgn='close'):
    '''
    def STDDEV(df, n,ksgn='close'):
    #标准偏差,#Standard Deviation
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：std_{n}，输出数据
    '''
    xnam='std_{d}'
    #
    ds=pd.Series(df[ksgn].rolling(window=n,center=False).mean(), name =xnam)
    df = df.join(ds)  
    #df = df.join(pd.Series(pd.rolling_std(df[ksgn], n), name =xnam))  
    
    return df      
    
  

def STOD(df, n,ksgn='close'):    
    '''
    def STO(df, n,ksgn='close'):     
       KDJ 随机指标D值,Stochastic oscillator %D  
	随机指标，又称KD指标，KDJ指标
　   随机指标综合了动量观念、强弱指标及移动平均线的优点，用来度量股价脱离价格正常范围的变异程度。
　   KD指标考虑的不仅是收盘价，而且有近期的最高价和最低价，这避免了仅考虑收盘价而忽视真正波动幅度的弱点。
　  随机指标一般是根据统计学的原理，通过一个特定的周期（常为9日、9周等）内出现过的最高价、最低价
  及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值RSV，
  然后根据平滑移动平均线的方法来计算K值、D值与J值，并绘成曲线图来研判股票走势。
  K与D值永远介于0到100之间。D大于80时，行情呈现超买现象。D小于20时，行情呈现超卖现象。
  上涨趋势中，K值小于D值，K线向上突破D线时，为买进信号。下跌趋势中，K值大于D值，K线向下跌破D线时，为卖出信号。
       
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：stod，输出数据
    '''
    #xnam='stod'
    xnam='stod'
    SOk = pd.Series((df[ksgn] - df['low']) / (df['high'] - df['low']), name = 'stok')
    #SOd = pd.Series(pd.ewma(SOk, span = n, min_periods = n - 1), name = xnam)
    SOd=pd.Series(SOk.ewm(span = n, min_periods = n - 1,adjust=True,ignore_na=False).mean(),name = xnam)
    df = df.join(SOk)  
    df = df.join(SOd) 
    df['stod']=df['stod']*100
    df['stok']=df['stok']*100
    #print('n df',len(df))
    return df


def STOK(df,ksgn='close'):  
    '''
    def STOK(df,ksgn='close'):  
    KDJ 随机指标K值,Stochastic oscillator %K
	随机指标，又称KD指标，KDJ指标
　   随机指标综合了动量观念、强弱指标及移动平均线的优点，用来度量股价脱离价格正常范围的变异程度。
　   KD指标考虑的不仅是收盘价，而且有近期的最高价和最低价，这避免了仅考虑收盘价而忽视真正波动幅度的弱点。
　  随机指标一般是根据统计学的原理，通过一个特定的周期（常为9日、9周等）内出现过的最高价、最低价
  及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值RSV，
  然后根据平滑移动平均线的方法来计算K值、D值与J值，并绘成曲线图来研判股票走势。
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：stok，输出数据
    '''
    xnam='stok'
    SOk = pd.Series((df[ksgn] - df['low']) / (df['high'] - df['low']), name =xnam)  
    df = df.join(SOk)  
    return df



def TRIX(df, n,ksgn='close'): 
    '''
    def TRIX(df, n,ksgn='close'): 
    三重指数平滑平均线（TRIX）属于中长线指标。它过滤掉许多不必要的波动来反映股价的长期波动趋势。在使用均线系统的交叉时，有时会出现骗线的情况，有时还会出现频繁交叉的情况，通常还有一个时间上的确认。为了解决这些问题，因而发明了TRIX这个指标把均线的数值再一次地算出平均数，并在此基础上算出第三重的平均数。这样就可以比较有效地避免频繁出现交叉信号。 TRIX指标又叫三重指数平滑移动平均指标，其英文全名为“Triple Exponentially Smoothed Average”，是一种研究股价趋势的长期技术分析工具。
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：trix，输出数据
    '''
    #xnam='trix_{n}'.format(n=n)
    xnam='trix'
    EX1=df[ksgn].ewm(span=n,min_periods=n-1,adjust=True,ignore_na=False).mean()
    EX2=EX1.ewm(span=n,min_periods=n-1,adjust=True,ignore_na=False).mean()
    EX3=EX2.ewm(span=n,min_periods=n-1,adjust=True,ignore_na=False).mean()
    #
    #EX1 = pd.ewma(df[ksgn], span=n, min_periods=n - 1)
    #EX2 = pd.ewma(EX1, span=n, min_periods=n - 1)
    #EX3 = pd.ewma(EX2, span=n, min_periods=n - 1)
    
    i = 0
    ROC_l = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]:
        ROC = (EX3[i + 1] - EX3[i]) / EX3[i]*10000
        ROC_l.append(ROC)
        i = i + 1
    trix  = pd.Series(ROC_l, name=xnam)
    #df = df.join(trix)     
    trix.index=df.index;
    df[xnam]=trix
    
    #df[xnam]=EX3
     
    #print(trix.tail())
    #print('n',len(df))
    return df
    


def TSI(df, r, s,ksgn='close'):   
    
    '''
    def TSI(df, r, s,ksgn='close'):   
    TSI，真实强度指数,True Strength Index
  TSI是相对强弱指数 (RSI) 的变体。
  TSI 使用价格动量的双重平滑指数移动平均线，剔除价格的震荡变化并发现趋势的变化。
  r一般取25，是一般取13
    【输入】
        df, pd.dataframe格式数据源
        r,s，时间长度;  r一般取25，s一般取13
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：tsi，输出数据
    '''
    #xnam='tsi'.format(d=r,d2=s)
    xnam='tsi'
    M = pd.Series(df[ksgn].diff(1))  
    aM = abs(M)  
    EMA1=M.ewm(span=r,min_periods=r-1,adjust=True,ignore_na=False).mean()
    aEMA1=aM.ewm(span=r,min_periods=r-1,adjust=True,ignore_na=False).mean()
    EMA2=EMA1.ewm(span=s,min_periods=s-1,adjust=True,ignore_na=False).mean()
    aEMA2=aEMA1.ewm(span=s,min_periods=s-1,adjust=True,ignore_na=False).mean()
    #EMA1 = pd.Series(pd.ewma(M, span = r, min_periods = r - 1))  
    #
    TSI = pd.Series(EMA2 / aEMA2, name = xnam)  
    df = df.join(TSI)  
    
    return df





#Ultimate Oscillator  
def ULTOSC(df,n=7,ksgn='close'):
    '''
    def ULTOSC(df,ksgn='close'):
    UOS，终极指标（Ultimate Oscillator，UOS）
　　终极指标，由拉瑞·威廉（Larry Williams）所创。他认为现行使用的各种振荡指标，对于周期参数的选择相当敏感。
   不同的市况，不同参数设定的振荡指标，产生的结果截然不同。因此，选择最佳的参数组含，成为使用振荡指标之前，最重要的一道手续。
　　为了将参数周期调和至最佳状况，拉瑞·威廉经过不断测试的结果，先找出三个周期不同的振荡指标，再将这些周期参数，按照反比例的方式，制作成常数因子。
   然后，依照加权的方式，将三个周期不同的振荡指标，分别乘以不同比例的常数，加以综合制作成UOS指标。
　　经过一连串参数顺化的过程后，UOS指标比一般单一参数的振荡指标，更能够顺应各种不同的市况。
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：uos，输出数据
    '''
    i = 0  
    TR1 = [0]  
    BP1 = [0]  
    xnam='uos'
    while i <  len(df) - 1:   #df.index[-1]:  
        #TR = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))  
        TR = max(df['high'].iloc[i+1],df[ksgn].iloc[i])-min(df['low'].iloc[i+1],df[ksgn].iloc[i])  
        TR1.append(TR)  
        #BP = df.get_value(i + 1, 'close') - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))  
        BP =df[ksgn].iloc[i+1]-min(df['low'].iloc[i+1], df[ksgn].iloc[i])  
        BP1.append(BP)  
        i = i + 1  
    
    #UltO = pd.Series((4 * pd.rolling_sum(pd.Series(BP_l), 7) / pd.rolling_sum(pd.Series(TR_l), 7)) + (2 * pd.rolling_sum(pd.Series(BP_l), 14) / pd.rolling_sum(pd.Series(TR_l), 14)) + (pd.rolling_sum(pd.Series(BP_l), 28) / pd.rolling_sum(pd.Series(TR_l), 28)), name =xnam)  # 'Ultimate_Osc'
    n2,n4=n*2,n*4
    BP1=pd.Series(BP1)
    TR1=pd.Series(TR1)
    mbp1=BP1.rolling(window=n,center=False).sum()
    mtr1=TR1.rolling(window=n,center=False).sum()
    mbp2=BP1.rolling(window=n2,center=False).sum()
    mtr2=TR1.rolling(window=n2,center=False).sum()
    mbp4=BP1.rolling(window=n4,center=False).sum()
    mtr4=TR1.rolling(window=n4,center=False).sum()
    
    UltO=pd.Series(4*mbp1/mtr1+2*mbp2/mtr2+mbp4/mtr4,name=xnam)
    #UltO=pd.Series((4*pd.rolling_sum(pd.Series(BP_l),n)/pd.rolling_sum(pd.Series(TR_l),n))+(2*pd.rolling_sum(pd.Series(BP_l),n2)/pd.rolling_sum(pd.Series(TR_l),n2))+(pd.rolling_sum(pd.Series(BP_l),n4)/pd.rolling_sum(pd.Series(TR_l),n4)),name=xnam)  # 'Ultimate_Osc'
    #df = df.join(UltO)      
    UltO.index=df.index;
    df[xnam]=UltO*10 *2
    return df


def VORTEX(df, n):
    '''
    def VORTEX(df, n):
    VI 螺旋指标,#Vortex Indicator  
    参见 http://www.vortexindicator.com/VFX_VORTEX.PDF


    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度

    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：vortex 输出数据
    '''
    #xnam='vortex_{n}'.format(n=n)
    xnam='vortex'
    i = 0
    TR = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #Range = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))
        Range=max(df['high'].iloc[i+1],df['close'].iloc[i])-min(df['low'].iloc[i+1],df['close'].iloc[i])
        #TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
        TR.append(Range)
        i = i + 1
    i = 0
    VM = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #Range = abs(df.get_value(i + 1, 'high') - df.get_value(i, 'low')) - abs(df.get_value(i + 1, 'low') - df.get_value(i, 'high'))
        Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        VM.append(Range)
        i = i + 1
    #ds = pd.Series(pd.rolling_sum(pd.Series(VM), n) / pd.rolling_sum(pd.Series(TR), n), name=xnam)
    VM,TR=pd.Series(VM),pd.Series(TR)
    vm2=VM.rolling(window=n,center=False).sum()
    tr2=TR.rolling(window=n,center=False).sum()
    ds = pd.Series(vm2/tr2, name=xnam)
    #df = df.join(ds)  
    ds.index=df.index;
    df[xnam]=ds*100
    
    return df




    
#=========================================
'''
indicators=["MA", "EMA", "MOM", "ROC", "ATR", "BBANDS", "PPSR", "STOK", "STO",
    "TRIX", "ADX", "MACD", "MassI", "Vortex", "KST", "RSI", "TSI", "ACCDIST",
    "Chaikin", "MFI", "OBV", "FORCE", "EOM", "CCI", "COPP", "KELCH", "ULTOSC",
    "DONCH", "STDDEV"]
'''