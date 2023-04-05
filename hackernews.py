from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://news.ycombinator.com/"
r = requests.get(url)
#use "print(r)" to check the response status code of the website 200 or 404
if(r.status_code==200):
    doc = BeautifulSoup(r.text, "html.parser")
    #use "print(type(doc).__name__)" to check if the return value is BeutifulSoup
    doc2 = BeautifulSoup(doc.decode('utf8'), "html.parser")
    #use "print(doc2.prettify())" to see HTML document printed in readable style
    titles = doc2.find_all(attrs={'class':'titleline'})
    a = [titles[i].parent.find('a').text.replace('a',"").replace('\n'," ") for i in range(10)]
    b = [titles[i].parent.find('a', href=True)['href'] for i in range(10)]
    #print(b)
    #parent = titles[0].parent 
    #for link in parent.find_all('a', href=True):
        #print(link['href'])
else:
    print('URL Not Found ')
data = {"Today's 10 latest news": a, "Links": b}
df = pd.DataFrame(data)
df.to_csv('10news.csv')
print(df)
