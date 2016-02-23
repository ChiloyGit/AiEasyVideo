# -*- coding: utf-8 -*-
# The code used download NetEasy Public Lesson video
import os, wget, bs4, requests, re, sys
def _sysexit():
    input("请按回车键退出: ")
    sys.exit()
'''
网页请求处理
'''
def _httpreq(url):
    try:
        req = requests.get(url)
        #req.encoding = 'utf-8'
        return req.text
    except:
        print ('请确保网络连接正常及网址正确！')
        _sysexit()
print ('#'.center(30, '#'))
print ('本程序适用于下载网易云公开课视频\n作者：chiloy@chiloy.com\n如有问题与建议，请与我联系！')
print ('#'.center(30, '#'))
inputurl = input('请输入或复制(ctrl+v)网易云课堂公开课专辑目录网址：')
reqcontent = bs4.BeautifulSoup(_httpreq(inputurl),"html5lib")
print ('开始抓取页面视频'.center(60, '#'))
print (('课程信息：%s ' % reqcontent.title.string).center(70, '*'))
splitname = reqcontent.title.string.split('：')
idlist2 = reqcontent.find_all(id ="list2")
urlarr = []
lesarr = []
downurlarr = []
for line in idlist2:
    for row in line.find_all(href=re.compile("open.163.com/movie")):
        urlarr.append (row.get('href'))
        lesarr.append (row.next_element)
for lesname in lesarr:
    print ('第%d集：%s' % (lesarr.index(lesname) + 1, lesname))
print ('成功抓取页面视频'.center(60, '#'))
print ('开始生成视频下载链接'.center(60, '#'))
for index in range(len(urlarr)):
    getdowncontent = _httpreq(urlarr[index])
    m3u8flag = getdowncontent.find('-list.m3u8')
    headappsrc = getdowncontent.find("appsrc : '")
    if (m3u8flag == -1):
        tailappsrc = getdowncontent.find('.m3u8') 
    else:
        tailappsrc = m3u8flag
    downurl = getdowncontent[headappsrc +10 :tailappsrc] + '.mp4'
    downurlarr.append(downurl)
    while (len(downurlarr) == len(urlarr)):
        print ('成功生成视频下载链接')
        break
print ('即将开始下载工作，请保证D盘有足够的硬盘空间！')


downmode= input ('如下载全部视频，请输入 Y，单集请输入集号数字：')
if (os.path.exists("D:\\AiEasyVideo") == False): 
    os.mkdir("D:\\AiEasyVideo")
if (os.path.exists("D:\\AiEasyVideo\\" + splitname[0]) == False):
        os.mkdir("D:\\AiEasyVideo\\" + splitname[0])
if(os.path.exists("D:\\AiEasyVideo\\" + splitname[0] + '\\' + splitname[1]) == False):
            os.mkdir("D:\\AiEasyVideo\\" + splitname[0] + '\\' + splitname[1])

if (downmode == 'Y'):
    for downstep in downurlarr:        # 第二个实例   
        print ('正在下载第%d集：%s，剩余下载%d集' % (downurlarr.index(downstep) + 1, lesarr[downurlarr.index(downstep)], len(downurlarr) - (downurlarr.index(downstep) + 1)))
        wget.download(downstep, "D:\\AiEasyVideo\\" + splitname[0] + '\\' + splitname[1] + '\\' + lesarr[downurlarr.index(downstep)] + '.mp4')
    print ('视频下载完成！好好学习！天天向上！')
elif(0 < int(downmode)< len(downurlarr)):
    downnumber = int(downmode) - 1
    print ('请稍后正在下载第%d集：%s' % (int(downmode), lesarr[downnumber]))
    wget.download(downurlarr[downnumber], "D:\\AiEasyVideo\\" + splitname[0] + '\\' + splitname[1] + '\\'  + lesarr[downnumber] +'.mp4')
    print ('视频下载完成！好好学习！天天向上！')
    inexit = input ('输入Q退出本程序')
    while inexit =='Y':
        print ('感谢使用本程序')
        sys.exit()
        
else:
    print ('输入值不合法')
    _sysexit()











