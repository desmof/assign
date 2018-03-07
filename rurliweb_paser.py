# -*- coding: utf-8 -*-
from __future__ import print_function
import requests
from bs4 import BeautifulSoup as Soup #html parser
from requests.compat import urljoin

# selector = '#board_list > dev > div.board_main.theme_defalut > table > tbody'



def turn_url(url,chk,table_hd):
    res = requests.get(url)
    soup= Soup(res.content, "html.parser")
    #soup = BeautifulSoup(res.content,"html.parser")
    rows = soup.find_all(chk, class_= table_hd)
    return rows
    ## url과 리스트 헤더 받아사 rows를 리턴
    
def turn_url_2(url,chk,table_hd):
    res = requests.get(url)
    soup= Soup(res.content, "html.parser")
    #soup = BeautifulSoup(res.content,"html.parser")
    rows = soup.find(chk, class_=table_hd)
    return rows
    ## url과 리스트 헤더 받아사 rows를 리턴

def passing(row,table_hd,ck):
    res = row.find(table_hd,{"class" : ck } )
    return res

    ##받은 줄을 아규먼트를 출력해줌
    



url = "http://bbs.ruliweb.com/market/board/1020"
rows = turn_url(url,"tr","table_body")

for row in rows :
    aid = passing(row,"td","id").get_text().strip()
    divsn = passing(row,"td","divsn").get_text().strip()
    subject = passing(row,"td","subject").a.get_text().strip()
    link = passing(row,"td","subject").a.get("href")
    href = urljoin(url,link)
    

    recomd = passing(row,"td","recomd").get_text().strip()
    hit = passing(row,"td","hit").get_text().strip()
    time = passing(row,"td","time").get_text().strip()
    try :
        print (u"{0}|{1}|{2}|{3}|{4}|{5}".format(aid,divsn,subject,recomd,hit,time) )
    except SyntaxError :
        pass
    except UnicodeEncodeError:
        pass
    except IOError:
            pass
    

    conts=turn_url_2(href,"div","view_content")
    conts_3 = conts.find_all("p")
    for row_3 in conts_3:
        break
        contex = row_3.get_text().strip()
        try :
            print (contex)
        except SyntaxError :
            pass
        except UnicodeEncodeError:
            pass
        except IOError:
            pass
        
    print (u"*"*60)
    rows_2=turn_url_2(href,"table","comment_table best")
    if rows_2 is not None :
        print (u"*"*60)
        rowss = rows_2.find_all("tr",{"class":"comment_element parent best"})
    
        for row_2 in rowss :
            user = row_2.find("div",{"class":"nick"}).get_text().strip()
#            user = passing(row,"div","nick").get_text().strip()
 #           user = row_2.find("div",{"class":"nick"}).get_text().strip()
            comment = row_2.find("span",{"class":"text"}).get_text().strip()
  #          comment = passing(row,"td","comment").get_text().strip()
            lik = row_2.find("button",{"class":"btn_like"}).span.get_text().strip()
            dik = row_2.find("button",{"class":"btn_dislike"}).span.get_text().strip()
            try :
                print (u"{0}|{1}|{2}|{3}".format(user,comment,lik,dik))
            except:
                pass
    try :
        print (u"*"*60)
    except:
        pass       
    





##r_classes = row.get('class')
##            recommand = row.find("td",{"class" : strict).get_text().strip()
##            recommand = int(recommand)
##            if recommand > 3 :
##                aid = 
##                dep = row.find("td",{"class" : "divsn"}).a.get_text()
##                title = row.find("td",{"class" : "subject"}).div.a.get_text()
##                count = row.find("td",{"class" : "hit"}).get_text().strip()
                




    
