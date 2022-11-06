
import streamlit as st
import requests
def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	return response.json()
    # 將 response 轉換成 json 格式
	# 回傳值
def app():
    bookstorelist = getAllBookstore()
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstorelist))
    county = st.selectbox('請選擇縣市', getcountyoption(bookstorelist))
    SpecificBookstore = getSpecificBookstore(bookstorelist,county)
    num = len(SpecificBookstore)
    st.write(num)
def getcountyoption(items):
    #創一個空的 list 命名為 optionlist
    optionlist = []
    for item in items:
        #把 cityname 欄位中的縣市名節取出來 並給指定變數 name
        # hint: 想辦法去處理 items['cityname']的內容
        name = item['cityName'][0:3]
        # 如果 name 不再 optionlist 之中 把它放入 optionlist
        # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionlist
        if name not in item:
            optionlist.append(name)
    return optionlist       
def getSpecificBookstore(items,country):
    Specificbookstore = []
    for item in items:
        name = item['cityName']
        #如果 name 不是我們選擇的 country 則跳過
        # hint: 用 if-else 判斷 continue 跳過
        if country not in name :
            continue
        Specificbookstore.append(item)
    return Specificbookstore
if __name__ == '__main__':
    app()
