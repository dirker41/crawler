import requests
from bs4 import BeautifulSoup

def searchUrl( url,searchStr ):	
    if ( searchStr in requests.get(url ,headers={'Connection':'close'} ).text ):
       writehHtml( url )

def writehHtml( url ):
    file = open('link.html', 'a')
    file.write( '<a href=\"' + url + '\">' + url + '</a><BR>' )
    file.close()

file = open('link.html', 'w')
file.close() 

searchStr = input("Enter key word:")

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
	   
    
 



