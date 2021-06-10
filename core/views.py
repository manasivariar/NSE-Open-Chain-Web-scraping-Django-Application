from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

def index(request):
    url = "https://www.nseindia.com/option-chain"
    chrome = "D:\chromedriver.exe"  #Put your Chromedriver path here.
    # useragent = {"User-Agent":'Mozilla/5.0 (Windows NT10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    # r = requests.get(url, headers=useragent)
    # soup = BeautifulSoup(r.content, 'html.parser')
    myStyles = '''
    body{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .dataframe{
        margin: auto;
        border-collapse: collapse;
        text-align: center;
    }
    tr:first-child{
        font-weight: bold;
    }
    td {
        padding: 10px;
    }
    '''
    chrome_driver = webdriver.Chrome(executable_path=chrome)
    chrome_driver.get(url)
    sleep(5)
    data = chrome_driver.find_element_by_xpath('/html/body/div[7]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div/table[1]').text
    ls = data.split("\n")
    data1 = ls[1:22]
    data2 = ls[22:]
    dataMain = [x.split(" ") for x in data2]
    dataMain.insert(0, data1)
    df = pd.DataFrame(dataMain, columns=data1)
    df = df.to_html(header=False, index=False, justify="center", border=1, index_names=False)
    return HttpResponse("<h1>Extracted Data</h1>"+df+"<style type='text/css'>" + myStyles + "</style>")