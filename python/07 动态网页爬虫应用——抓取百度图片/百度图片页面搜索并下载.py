import os
import random
import re
import shutil
import time
import requests

COUNT_IMG_SUCCESSFUL = 0
COUNT_IMG_FAILED = 0

# 1. 获取网页源代码
def getHTMLText(pageIndex, key):
    try:
        # 指定请求url
        offset = 30 * pageIndex #设置每页偏移量
        hexOffset = hex(30 * pageIndex) #设置每页偏移量
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7075149555992023334&ipn=rj&ct=201326592&is=&fp=result&fr=&word={2}&queryWord={2}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={0}&rn=30&gsm={1}'.format(offset, hexOffset[2:],key)
        # 构造请求头，进行UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)  # 发送请求
        response.raise_for_status()
        jsonStr = response.json()
        return jsonStr #返回请求json格式
    except Exception as err:
        return {}  # 返回请求json格式
# 2. 解析网页源代码获取图片url列表
def parsePage(content): # 通过json获取当前页面的图片地址数组
    try:
        # print(content)
        imgList = [] #存储图片链接的列表
        for imgData in content['data']:
            if imgData['thumbURL']:
                # print(i['thumbURL'])
                imgList.append(imgData['thumbURL'])
        return imgList
    except Exception as err:
        return imgList
content = {
    "queryExt": "汽车",
    "data": [
        {
            "thumbURL": "https://img2.baidu.com/it/u=2063845288,771987642&fm=253&fmt=auto&app=138&f=JPEG?w=667&h=500",
            "fromPageTitle": "比亚迪唐dm-p开启预售 29.28万-33.28万_汽车前线",
        },
        {
            "thumbURL": "https://img2.baidu.com/it/u=3213417508,276827173&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500",
            "fromPageTitle": "长城汽车携豪华阵容闪耀曼谷国际车展,one gwm品牌战略再进击_搜狐汽",
        },
        {
            "thumbURL": "https://img0.baidu.com/it/u=4246844714,1826372471&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500",
            "fromPageTitle": "高清麦克拉伦12c蜘蛛汽车图片电脑桌面壁纸_汽车壁纸_壁纸下载_美桌网",
        },
        {}
    ]
}
# 3. 保存下载的图片到文件夹中
def saveImgsToDir(imgList, pageIndex, dirName):
    global COUNT_IMG_SUCCESSFUL
    global COUNT_IMG_FAILED
    print("Current page:" + str(pageIndex+1) + "**********************************")
    for i in range(len(imgList)):
        # print(imgList[i])
        try:
            # 下载图片并设置超时时间,如果图片地址错误就不继续等待了
            picture = requests.get(imgList[i], timeout=10)
            picture.raise_for_status()
            time.sleep(random.randint(1, 2))
            COUNT_IMG_SUCCESSFUL = COUNT_IMG_SUCCESSFUL + 1
            print('正在下载：{0}'.format(imgList[i]))
        except:
            COUNT_IMG_FAILED = COUNT_IMG_FAILED + 1
            print("Download image error! errorUrl:" + imgList[i])
            continue
        # 创建图片保存的路径
        pictureSavePath = dirName + '/' + str(i + pageIndex * 30) + '.jpg'
        # print(pictureSavePath)
        with open(pictureSavePath, 'wb') as fp:  # 以写入二进制的方式打开文件
            fp.write(picture.content)

# 创建所需文件夹
def creadDir(key):
    saveDir = '百度搜索页面图片-{0}'.format(key)
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    else:
        shutil.rmtree(saveDir)
        os.mkdir(saveDir)
    return saveDir

def main():
    MaxSearchPage = 3 #搜索页数
    key = input("请输入搜索词：")
    # 创建用于存放下载图片的文件夹
    dirName = creadDir(key)
    for pageIndex in range(MaxSearchPage): #多页下载
        responseText = getHTMLText(pageIndex, key)  #获取网页源代码（json格式）
        imgList = parsePage(responseText) #从获取的json结构中获取图片url列表
        saveImgsToDir(imgList, pageIndex, dirName) #保存下载的图片到文件夹中
    print('下载完毕，下次成功图片总数：{0}，下载失败图片总数：{1}'.format(COUNT_IMG_SUCCESSFUL, COUNT_IMG_FAILED))
main()