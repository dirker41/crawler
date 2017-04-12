import requests
from bs4 import BeautifulSoup
from os.path import exists

def searchUrl( url,searchStr ):	

    searchStrList = searchStr.split(' ')
    
    htmlContent = requests.get(url ,headers={'Connection':'close'} ).text
    
    flag = 0
	
    for str in searchStrList:
      if str not in htmlContent:
        flag = 1 
	
    if flag == 0 :
       writehHtml( url )

def writehHtml( url ):
    print( url + '\n' )
    file = open(fileName, 'a')
    file.write( '<a href=\"' + url + '\">' + url + '</a><BR>' )
    file.close()

fileName = 'link.html'
fileCount = 0 

while exists(fileName):
  print( fileName )
  fileCount += 1 
  fileName = fileName[:4] + str(fileCount) + fileName[ len(fileName)-5:len(fileName)]


searchStr = input("Enter key word:")

file = open(fileName, 'w')
file.write( searchStr + '<BR>' )
file.close() 




for i in range(1,500):
 JKFstr = 'https://www.jkforum.net/home.php?mod=space&uid=430045&do=thread&view=me&order=dateline&from=space&page='

 res = requests.get(JKFstr+str(i),headers={'Connection':'close'})
 soup = BeautifulSoup(res.text,'html.parser')
 aList = soup.find_all('a')
 temp = ''
 
 for link in aList:
   
   if link.get('href') != None and 'thread-' in link.get('href') and link.get('href')[0]=='t':
     if temp == '' :
       temp = link.get('href')
     elif temp != '' and link.get('href') == temp:
      
       searchUrl( 'https://www.jkforum.net/' + link.get('href'), searchStr )
	  
       
       temp = ''
     else:
       temp = ''

 print( '找完第' + str(i) + '頁')
	   
    
 



