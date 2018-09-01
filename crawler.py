import requests
from bs4 import BeautifulSoup
from os.path import exists

def searchUrl( index, url, searchStr ): 

    searchStrList = searchStr.split(' ')
    img = ""
    
    try :
      htmlContent = requests.get(index +url ,headers={'Connection':'close'} ).text
    except:
      return 0
    #soup = BeautifulSoup(htmlContent,'html.parser')
    #list = soup.find('div','pl post-list')
    
    #print( htmlContent )
    

    for str1 in searchStrList:
      if str1 not in htmlContent:
        return 0
    writehHtml( index +url ) # write torrent link
    #createfile( "test.html", list.text )
"""
    if len( searchStrList) == 1 :
       keywordindex = htmlContent.find( searchStr )
       print( "keywordindex:" + str(keywordindex))
       torrentIndex = htmlContent.lower().find( ".torrent" , keywordindex )
       a1 = htmlContent.find( "<a href=" , torrentIndex-200 )
       com1 = htmlContent.find( "\"" , a1 )
       com2 = htmlContent.find( "\"" , com1+1 )
       print( "com1:" + str(com1))
       url = htmlContent[com1+1:com2]
       imgIndex1 = htmlContent.lower().find( "<ignore_js_op>" , keywordindex )
       imgIndex2 = htmlContent.lower().find( "</ignore_js_op>" , keywordindex )
       img = htmlContent[imgIndex1:imgIndex2+len("</ignore_js_op>")]
       print(str(imgIndex1) + "." + str(imgIndex2))
       print(img)
"""
    #writehHtmlimg( img ) # write jpg
    #writehHtml( index +url ) # write torrent link

def writehHtml( url ):
    print( url + '\n' )
    file = open(fileName, 'a')
    file.write( '<a target=\"_blank\" href=\"' + url + '\">' + url + '</a><BR>\r\n' )
    file.close()

def writehHtmlimg( img ):
    print( img + '\n' )
    file = open(fileName, 'a')
    file.write( img + '<BR>\r\n'  )
    file.close()

def createfile( name, context ):
    file = open(name, 'w')
    file.write( context  )
    file.close()


fileName = 'link.html'
fileCount = 0 
"""
while exists(fileName):
  print( fileName )
  fileCount += 1 
  fileName = fileName[:4] + str(fileCount) + fileName[ len(fileName)-5:len(fileName)]
"""

#searchStr = input("Enter key word:")
searchStr = "高杉麻里"

fileName = searchStr + '.html'

file = open(fileName, 'wb' )
file.write( searchStr.encode('utf-8')  )
file.close() 
file = open(fileName, 'a' )
file.write( '<BR>'  )
file.close() 

JKFindex = "https://www.jkforum.net/"

for i in range(1,100):
  JKFstr = JKFindex + 'home.php?mod=space&uid=430045&do=thread&view=me&order=dateline&from=space&page='

  try :
    res = requests.get(JKFstr+str(i)+".html",headers={'Connection':'close'})
  except :
    print( "skip: page" + str(i) )
  #print( res.text )
  soup = BeautifulSoup(res.text,'html.parser')
  aList = soup.find_all('a')
  temp = ''
 
  for link in aList:
   
   if link.get('href') != None and 'thread-' in link.get('href') and ( "日本" in link.text or "中文" in link.text ):
       searchUrl( JKFindex, link.get('href'), searchStr )


  print( '找完第' + str(i) + '頁')
       
    
 



