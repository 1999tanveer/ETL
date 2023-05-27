#!/usr/bin/env python
# coding: utf-8

# In[163]:


#pip install supabase


# In[248]:


import requests
from datetime import date
import datetime
from supabase import create_client, Client


# In[249]:


url=""
key=""

supabase_conn= create_client(url, key)


# In[252]:


import logging
logger = logging.getLogger()
loghandler = logging.FileHandler(filename='StockAnalysis_log.log', mode='a')
logger.addHandler(loghandler)


# In[253]:


logging.info('Logs for Stock Analysis ETL Process')


# In[254]:


today = date.today()
today=today-datetime.timedelta(days=11)
print("Today's date:", today)


# In[204]:


url_day = "https://working-days.p.rapidapi.com/1.3/get_info_day"

querystring = {"country_code":"US","date":today-datetime.timedelta(days=1),"configuration":"Federal holidays"}

headers = {
	"X-RapidAPI-Key": "50033bb69cmshcdb1dfd03d87915p1bd957jsnd26aeee15a5c",
	"X-RapidAPI-Host": "working-days.p.rapidapi.com"
}

response = requests.request("GET", url_day, headers=headers, params=querystring)

print(response.text)


# In[257]:


today = date.today()
yesterday=today-datetime.timedelta(days=1)
print(d, "Yesterday's date:", yesterday)

if (response.json()['working_day']==1) :

    logging.info('Extract Operation for'+str(yesterday))

    url='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=ODSLP5A1Z79WG98U&outputsize=compact'
    r = requests.get(url)
    data = r.json()

    #print(data)

    SMA_nValue= 3
    LMA_nValue=10
    leaveDays=0
    SMA=0
    LMA=0
    Sum=0
    i=0;
    
    while(LMA_nValue+leaveDays>i):
        if ( (yesterday-datetime.timedelta(days=i)).strftime('%Y-%m-%d')) in data['Time Series (Daily)'] :
            #print( (yesterday-datetime.timedelta(days=i)).strftime('%Y-%m-%d') ," -- ",data['Time Series (Daily)'][ (yesterday-datetime.timedelta(days=i) ).strftime('%Y-%m-%d')]['4. close'],"--working")
            Sum+=float(data['Time Series (Daily)'][ (yesterday-datetime.timedelta(days=i) ).strftime('%Y-%m-%d')]['4. close'])
            if i == SMA_nValue+leaveDays-1:
                SMA='%.3f'% (Sum/SMA_nValue)

            if i == LMA_nValue+leaveDays-1:
                LMA='%.3f'% (Sum/LMA_nValue)
        else:
            #print(i,"-- Leave")
            leaveDays+=1;
        i+=1;

    print("SMA -:", SMA,"LMA -:", LMA)
    logging.info('Transformted Data:'+"SMA -"+str(SMA)+"LMA -"+str(LMA))

    value={'Date':(yesterday).strftime('%Y-%m-%d'),'SMA':SMA,'LMA':LMA}
    op=supabase_conn.table('StockAnalysis').insert([value]).execute()
    logging.info('Load operation output:'+str(op))
    print(op)

else:
    logging.info('Holiday -'+str(yesterday))

