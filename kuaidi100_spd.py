# 1��HTTP����
import urllib.request  #����
import urllib.parse  #URL����
import time  #������ʱ
from multiprocessing.dummy import Pool  #���߳�
import random
# 2��ģ�������
from selenium import webdriver
from selenium.webdriver.common.by import By
# 3�����ݽ���
import json  #json��ʽ����
from lxml import etree  #����ΪXML��HTML
import re  #����ƥ��
# 4�����ݴ洢
import MySQLdb
             
#################################
###1�������ȡHTTP_User_Agent
#################################
def getUserAgent():
    '''
    ���ܣ������ȡHTTP_User_Agent
    '''
    user_agents=[
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    user_agent = random.choice(user_agents)
    return user_agent
    
#################################
###2����������IP��
#################################
  
def getProxies(pages):
    '''
    ���ܣ���ȡ���̸���IP����ԭʼ����IP��
	@pages����ȡ����ҳԭʼ����IP
    '''
    init_proxies = []
    ##��ȡǰʮҳ
    for i in range(1,pages+1):
        print("####")
        print("####��ȡ��"+str(i)+"ҳ####")
        print("####")        
        print("IP��ַ\t\t\t�˿�\t���ʱ��\t\t��֤ʱ��")
        url = "http://www.xicidaili.com/nn/"+str(i)
        user_agent = getUserAgent()
        headers=("User-Agent",user_agent)
        opener = urllib.request.build_opener() 
        opener.addheaders = [headers] 
        try:
            data = opener.open(url,timeout=5).read()
        except Exception as er:
            print("��ȡ��ʱ�������󣬾������£�")
            print(er)
        selector=etree.HTML(data) 
        ip_addrs = selector.xpath('//tr[@class="odd"]/td[2]/text()')  #IP��ַ
        port = selector.xpath('//tr[@class="odd"]/td[3]/text()')  #�˿�
        sur_time = selector.xpath('//tr[@class="odd"]/td[9]/text()')  #���ʱ��
        ver_time = selector.xpath('//tr[@class="odd"]/td[10]/text()')  #��֤ʱ��
        for j in range(len(ip_addrs)):
            ip = ip_addrs[j]+":"+port[j] 
            init_proxies.append(ip)
            print(ip_addrs[j]+"\t\t"+port[j]+"\t\t"+sur_time[j]+"\t"+ver_time[j])#�����ȡ���� 
    return init_proxies

	
def testProxy(curr_ip):
    '''
    ���ܣ���֤IP��Ч��
    @curr_ip����ǰ����֤��IP
    '''
    tmp_proxies = []
    tarURL = "http://www.baidu.com/" 
    user_agent = getUserAgent()
    proxy_support = urllib.request.ProxyHandler({"http":curr_ip})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders=[("User-Agent",user_agent)]
    urllib.request.install_opener(opener)
    try:
        res = urllib.request.urlopen(tarURL,timeout=5).read()
        if len(res)!=0:
            tmp_proxies.append(curr_ip)
    except urllib.error.URLError as er2: 
        if hasattr(er2,"code"):
            print("��֤����IP��"+curr_ip+"��ʱ�������󣨴�����룩��"+str(er2.code))
        if hasattr(er2,"reason"):
            print("��֤����IP��"+curr_ip+"��ʱ�������󣨴���ԭ�򣩣�"+str(er2.reason))
    except Exception as er:
        print("��֤����IP��"+curr_ip+"��ʱ�������´��󣩣�")
        print(er)
    return tmp_proxies
		
##2.3 ���߳���֤ 	
def mulTestProxies(unchecked_proxies):
    '''
    ���ܣ����߳���֤IP��Ч��
    @tmp_proxies��ԭʼ����IP��
    '''
    pool = Pool(processes=3)
    fl_proxies = pool.map(testProxy,unchecked_proxies)
    pool.close()
    pool.join()  #�ȴ����̳��е�worker����ִ�����
    return fl_proxies

#################################
###3����ȡ�㶫��У��Ϣ���ڹؼ�������
################################# 
def getSchoolInfo():
    '''
    ���ܣ���ȡ�㶫��У��Ϣ
    '''
    url = "http://www.gx211.com/gxmd/gx-gd.html"
    user_agent = getUserAgent()
    headers=("User-Agent",user_agent)
    opener = urllib.request.build_opener() 
    opener.addheaders = [headers] 
    try:
        data = opener.open(url,timeout=5).read()
    except Exception as er:
        print("��ȡ��ʱ�������󣬾������£�")
        print(er)
	####�������ݣ��ǹ�����html�ļ���
    selector = etree.HTML(data)
    school_name_list1 = selector.xpath('//div[@id!="Div0"]/table/tbody/tr/td[1]')
    school_name_list2 = selector.xpath('//div[@id="Div3"]/table/tr/td[1]')
        
    school_zhuguan_list1 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tbody/tr/td[2]/text()')
    school_zhuguan_list2 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tr/td[2]/text()')
    
    school_loc_list1 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tbody/tr/td[3]/text()')
    school_loc_list2 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tr/td[3]/text()')

    school_cengci_list1 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tbody/tr/td[4]/text()')
    school_cengci_list2 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tr/td[4]/text()')
    
    school_leixing_list1 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tbody/tr/td[5]/text()')
    school_leixing_list2 = selector.xpath('//div[@class="WrapContent"]/div[@id!="Div0"]/table/tr/td[5]/text()') 
    
    school_name_list = school_name_list1+school_name_list2
    school_zhuguan_list = school_zhuguan_list1+school_zhuguan_list2
    school_loc_list = school_loc_list1+school_loc_list2
    school_cengci_list = school_cengci_list1+school_cengci_list2
    school_leixing_list = school_leixing_list1+school_leixing_list2
	####�洢����
    school_info = [['ѧУ����','���ܲ���','���ڵ�','���','����']]
    for j in range(len(school_name_list)):
        school_name = "/".join(school_name_list[j].xpath('descendant-or-self::text()'))#ѡȡ��ǰ�ڵ�����к��Ԫ�أ��ӡ���ȣ��Լ���ǰ�ڵ㱾�� 
        school_name.replace('��','')
        school_name = re.search(u'[\u4e00-\u9fa5]+',school_name).group()#����ƥ������
        school_zhuguan = (school_zhuguan_list[j]).strip()
        school_loc = school_loc_list[j].strip()
        school_cengci = school_cengci_list[j].strip()
        school_leixing = school_leixing_list[j].strip()
        if school_name!='ѧУ����' or school_zhuguan!='���ܲ���' or school_loc!='���ڵ�' or school_cengci!='���' or school_leixing!='����':
            school_info.append([school_name,
                                school_zhuguan,
                                school_loc,
                                school_cengci,
                                school_leixing                  
                                ])
    return school_info
	
#################################
###4��Ŀ�����ݻ�ȡ
################################# 
def getGuids(keywords):
    '''
    ���ܣ���ȡ����
    @keywords�������ؼ���
    '''
    guids = []
    pat = "\(\'(.*?)\'\)\;"  #IDƥ��ģʽ
    chromedriver = "C:/Users/whenif/AppData/Local/Google/Chrome/Application/chromedriver"
    i = 0
    j = 0
    for keyword in keywords:
        i += 1
        browser = webdriver.Chrome(chromedriver)  #ģ�������
        keyword = urllib.parse.quote(keyword) #URL����
        browser.get("https://www.kuaidi100.com/courier/?searchText="+keyword)
        ids = browser.find_elements(by=By.XPATH,value="//div[@id='queryResult']/dl/dd[2]/span/a")  #����XHR��ID
        print("������ȡ��"+str(i)+"���ؼ���...")
        if i==80:
            time.sleep(180)#ÿ��ȡ80����Ϣ3����
        else:
            seconds =  random.randint(8, 12)
            time.sleep(seconds)
        for id in ids:
            j += 1  #����
            print("����ȡ��"+str(j)+"��guid...")
            id = id.get_attribute('onclick')
            id = re.compile(pat).findall(id)
            guids.append([urllib.parse.unquote(keyword),id[0]])
        browser.quit()
    return guids


def getInfos(guids,proxy_pool):
    '''
    ���ܣ���ȡ����
    @guids�����Աȫ��Ψһ��ʶ�б�
    @proxy_pool������IP��
    '''
    global data 
    infos = []#�洢����������Ϣ
    i = 0  #����IPѭ�������ۼ���
    j = 1  #��ȡ�����ۼ���
    for guid in guids:
        URL = 'https://www.kuaidi100.com/courier/searchapi.do?method=courierdetail&json={"guid":"'+guid[1]+'"}'  #��������URL
        user_agent = getUserAgent()
        my_user_agent = ("User-Agent",user_agent)
        print("������ȡ��"+str(j)+"�����Ա��Ϣ...")
        j += 1 
        i += 1
        if len(proxy_pool)!=0 and i < len(proxy_pool):
            i=i
        elif len(proxy_pool)!=0 and i >= len(proxy_pool):
            i=0
        else:
            print("����IP����Դ�ѿݽߣ����ڸ��´���IP��...")
            unchecked_proxies = getProxies(5)  #��ȡԭʼ����IP
            checked_proxies = mulTestProxies(unchecked_proxies)#���̲߳���ԭʼ����IP   
            proxy_pool = []
            for tmp_proxy in checked_proxies:
                if len(tmp_proxy)!=0:
                    proxy_pool.append(tmp_proxy)
            print("����IP�ظ�����ϣ�����ȡ"+str(len(proxy_pool))+"������IP")
            i=0	
        proxy_addr = proxy_pool[i]
        proxy = urllib.request.ProxyHandler({"http":proxy_addr[0]})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        opener.addheaders=[my_user_agent]
        urllib.request.install_opener(opener)
        try:
            data = opener.open(URL).read() 
        except urllib.error.URLError as er2: 
            proxy_pool.remove(proxy_addr) #�������Ƴ���IP
            if hasattr(er2,"code"):
                print("������룺"+str(er2.code))
            if hasattr(er2,"reason"):
                print("����ԭ��"+str(er2.reason))
        if type(data)==str:
            data = data
        else:
            data = data.decode()
        data_json = json.loads(data)
        company_name = data_json['courier']['companyName']  #��˾����
        courier_name = data_json['courier']['courierName']  #���Ա����
        courier_tel = data_json['courier']['courierTel']  #�ֻ�����
        work_time = data_json['courier']['workTime']  #����ʱ��
        score = data_json['courier']['score']  #�÷�
        xzq_full_name = data_json['courier']['xzqFullName']  #����
        infos.append([guid[0],guid[1],company_name,courier_name,courier_tel,work_time,score,xzq_full_name])
        # ������ȡƵ�ʣ�ÿ100����ȡ��Ϣ1���ӵģ�������ÿ����ȡ��Ϣ3��
        if i%100==0:
            time.sleep(60)
        else:
            time.sleep(3)
    return infos

#################################
###5��������ȡ��洢
################################# 
def dbCon():
    '''
    ���ܣ�����MySQL���ݿ�
    '''
    con = MySQLdb.connect(
        host='localhost',  # port
        user='****',       # usr_name
        passwd='****',     # passname
        db='****',  # db_name
        charset='utf8',
        local_infile = 1
        )
    return con  
 
def exeSQL(sql):
    '''
    ���ܣ����ݿ��ѯ���� 
    @sql������SQL���
    '''
    global res
    print("exeSQL: " + sql)
    #�������ݿ�
    con = dbCon()  #�������ݿ������
    cur = con.cursor()  #ͨ����ȡ�������ݿ�����conn�µ�cursor()�����������α�
    try:
        tmp = cur.execute(sql) #ͨ���α�cur ����execute()��������д�봿sql���
        res = cur.fetchmany(tmp)#cur.fetchone()ֻ��ʹ�α겻�ϵ������ƶ�
    except Exception as er:
        print('ִ��MySQL��䡾' + str(sql) + '��ʱ�����´���')        
        print(er)
    finally:
        cur.close()  #�ر��α�
        con.commit()  #�������ύ����������ݿ����һ������ʱ����Ҫ������������������ݲ��ᱻ�����Ĳ��롣
        con.close()  #�ر����ݿ�����
    return res
	
def exeInsertSQL(sql,data_list):
    '''
    ���ܣ����ݿ���뺯�� 
    @sql���������SQL���
    @data_list�����������б�
    ''' 
    con = dbCon()  #�������ݿ������
    cur = con.cursor()
    try:
        n = cur.executemany(sql,data_list)
    except Exception as er:
        print('ִ��MySQL��䡾' + str(sql) + '��ʱ�����´���')        
        print(er)
    finally:
        cur.close()  #�ر��α�
        con.commit()  #�������ύ����������ݿ����һ������ʱ����Ҫ������������������ݲ��ᱻ�����Ĳ��롣
        con.close()  #�ر����ݿ�����

def dataStore(school_info,xhr_guids,courier_info):
    '''
    ���ܣ����ݿ�洢 
    @school_info��ѧУ��Ϣ
    @xhr_guids������XHR�ļ���ȫ��Ψһ��ʶ��
    @courier_info�����Ա����
    ''' 
    #�洢ѧУ��Ϣ
    table_name1 = 'school_info'
    exeSQL("drop table if exists " + table_name1)
    exeSQL("create table " + table_name1 + "(ѧУ���� varchar(100), ���ܲ��� varchar(50), ���ڵ� varchar(50), ��� varchar(50), ���� varchar(50));")
    insert_sql1 = "insert into " + table_name1 + " values(%s,%s,%s,%s,%s);"
    exeInsertSQL(insert_sql1,school_info)		
    #�洢����XHR�ļ���ȫ��Ψһ��ʶ��
    table_name2 = 'xhr_guids'
    exeSQL("drop table if exists " + table_name2)
    exeSQL("create table " + table_name2 + "(�����ؼ��� varchar(100),ȫ�ֱ�ʶ�� varchar(50));")   
    insert_sql2 = "insert into " + table_name2 + " values(%s,%s);"
    exeInsertSQL(insert_sql2,xhr_guids)
    #�洢���Ա����
    table_name3 = 'courier_info'
    exeSQL("drop table if exists " + table_name3)
    exeSQL("create table " + table_name3 + "(`�����ؼ���` varchar(100),`ȫ�ֱ�ʶ��` varchar(50),`������˾` varchar(50),`���Ա����` varchar(20),`�ֻ�����` varchar(20),`����ʱ��` varchar(100),`�÷�` varchar(30),`��������` varchar(50));")   
    insert_sql3 = "insert into " + table_name3 + " values(%s,%s,%s,%s,%s,%s,%s,%s);"
    exeInsertSQL(insert_sql3,courier_info)
    
#################################
###6������main()����
#################################
def main():
    '''
    ���ܣ���������������غ���    
    '''
    #---��1����ȡ��ʼ����IP��
    unchecked_proxies = getProxies(10)  #��ȡԭʼ����IP
    checked_proxies = mulTestProxies(unchecked_proxies)  #���̲߳���ԭʼ����IP   
    proxy_pool = []
    for tmp_proxy in checked_proxies:
        if len(tmp_proxy)!=0:
            proxy_pool.append(tmp_proxy)
            print("����IP�ػ�ȡ��ϣ�����ȡ"+str(len(proxy_pool))+"������IP")
    #---��2����ȡ����λ�ã������ؼ��ʣ�
    school_info = getSchoolInfo()  #��ȡȫʡ��У��Ϣ
    final_loc = []  #��ȡ�����ؼ���
    for loc in school_info[1:]:
        final_loc.append(loc[0])
    '''Ԥ��ȫʡ�ֵ���Ϣ��ȡ�ӿ�
    sel_sql = 'select `province_name`\
                    ,`city_name`\
                    ,`county_name`\
                    ,`town_name`\
                    ,`village_name`\
            from    positionV1 ' +\
            'where  `province_name`="�㶫ʡ" \
               and  city_name="������";'
    location = exeSQL(sel_sql)
    final_loc = []
    for loc in location:
        loc = loc[1]+loc[2]+loc[3]+loc[4]
        final_loc.append(loc)'''
    #---��3����ȡ����
    xhr_guids = getGuids(final_loc)
    courier_info = getInfos(guids,proxy_pool) #��ȡ��ݺ�����Ϣ
    #---��4���洢����
    dataStore(school_info,xhr_guids,courier_info)
  
if __name__ == "__main__":
    main()

