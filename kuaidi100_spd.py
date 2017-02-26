# 1、HTTP请求
import urllib.request  #请求
import urllib.parse  #URL编码
import time  #设置延时
from multiprocessing.dummy import Pool  #多线程
import random
# 2、模拟浏览器
from selenium import webdriver
from selenium.webdriver.common.by import By
# 3、数据解析
import json  #json格式解析
from lxml import etree  #解析为XML和HTML
import re  #正则匹配
# 4、数据存储
import MySQLdb
             
#################################
###1、随机抽取HTTP_User_Agent
#################################
def getUserAgent():
    '''
    功能：随机获取HTTP_User_Agent
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
###2、构建代理IP池
#################################
  
def getProxies(pages):
    '''
    功能：爬取西刺高匿IP构造原始代理IP池
	@pages：获取多少页原始代理IP
    '''
    init_proxies = []
    ##爬取前十页
    for i in range(1,pages+1):
        print("####")
        print("####爬取第"+str(i)+"页####")
        print("####")        
        print("IP地址\t\t\t端口\t存活时间\t\t验证时间")
        url = "http://www.xicidaili.com/nn/"+str(i)
        user_agent = getUserAgent()
        headers=("User-Agent",user_agent)
        opener = urllib.request.build_opener() 
        opener.addheaders = [headers] 
        try:
            data = opener.open(url,timeout=5).read()
        except Exception as er:
            print("爬取的时候发生错误，具体如下：")
            print(er)
        selector=etree.HTML(data) 
        ip_addrs = selector.xpath('//tr[@class="odd"]/td[2]/text()')  #IP地址
        port = selector.xpath('//tr[@class="odd"]/td[3]/text()')  #端口
        sur_time = selector.xpath('//tr[@class="odd"]/td[9]/text()')  #存活时间
        ver_time = selector.xpath('//tr[@class="odd"]/td[10]/text()')  #验证时间
        for j in range(len(ip_addrs)):
            ip = ip_addrs[j]+":"+port[j] 
            init_proxies.append(ip)
            print(ip_addrs[j]+"\t\t"+port[j]+"\t\t"+sur_time[j]+"\t"+ver_time[j])#输出爬取数据 
    return init_proxies

	
def testProxy(curr_ip):
    '''
    功能：验证IP有效性
    @curr_ip：当前被验证的IP
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
            print("验证代理IP（"+curr_ip+"）时发生错误（错误代码）："+str(er2.code))
        if hasattr(er2,"reason"):
            print("验证代理IP（"+curr_ip+"）时发生错误（错误原因）："+str(er2.reason))
    except Exception as er:
        print("验证代理IP（"+curr_ip+"）时发生如下错误）：")
        print(er)
    return tmp_proxies
		
##2.3 多线程验证 	
def mulTestProxies(unchecked_proxies):
    '''
    功能：多线程验证IP有效性
    @tmp_proxies：原始代理IP池
    '''
    pool = Pool(processes=3)
    fl_proxies = pool.map(testProxy,unchecked_proxies)
    pool.close()
    pool.join()  #等待进程池中的worker进程执行完毕
    return fl_proxies

#################################
###3、获取广东高校信息用于关键词搜索
################################# 
def getSchoolInfo():
    '''
    功能：获取广东高校信息
    '''
    url = "http://www.gx211.com/gxmd/gx-gd.html"
    user_agent = getUserAgent()
    headers=("User-Agent",user_agent)
    opener = urllib.request.build_opener() 
    opener.addheaders = [headers] 
    try:
        data = opener.open(url,timeout=5).read()
    except Exception as er:
        print("爬取的时候发生错误，具体如下：")
        print(er)
	####解析数据（非规整的html文件）
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
	####存储数据
    school_info = [['学校名称','主管部门','所在地','层次','类型']]
    for j in range(len(school_name_list)):
        school_name = "/".join(school_name_list[j].xpath('descendant-or-self::text()'))#选取当前节点的所有后代元素（子、孙等）以及当前节点本身 
        school_name.replace('－','')
        school_name = re.search(u'[\u4e00-\u9fa5]+',school_name).group()#正则匹配中文
        school_zhuguan = (school_zhuguan_list[j]).strip()
        school_loc = school_loc_list[j].strip()
        school_cengci = school_cengci_list[j].strip()
        school_leixing = school_leixing_list[j].strip()
        if school_name!='学校名称' or school_zhuguan!='主管部门' or school_loc!='所在地' or school_cengci!='层次' or school_leixing!='类型':
            school_info.append([school_name,
                                school_zhuguan,
                                school_loc,
                                school_cengci,
                                school_leixing                  
                                ])
    return school_info
	
#################################
###4、目标数据获取
################################# 
def getGuids(keywords):
    '''
    功能：获取数据
    @keywords：搜索关键词
    '''
    guids = []
    pat = "\(\'(.*?)\'\)\;"  #ID匹配模式
    chromedriver = "C:/Users/whenif/AppData/Local/Google/Chrome/Application/chromedriver"
    i = 0
    j = 0
    for keyword in keywords:
        i += 1
        browser = webdriver.Chrome(chromedriver)  #模拟浏览器
        keyword = urllib.parse.quote(keyword) #URL编码
        browser.get("https://www.kuaidi100.com/courier/?searchText="+keyword)
        ids = browser.find_elements(by=By.XPATH,value="//div[@id='queryResult']/dl/dd[2]/span/a")  #构建XHR的ID
        print("正在爬取第"+str(i)+"个关键词...")
        if i==80:
            time.sleep(180)#每爬取80个休息3分钟
        else:
            seconds =  random.randint(8, 12)
            time.sleep(seconds)
        for id in ids:
            j += 1  #调试
            print("共爬取到"+str(j)+"个guid...")
            id = id.get_attribute('onclick')
            id = re.compile(pat).findall(id)
            guids.append([urllib.parse.unquote(keyword),id[0]])
        browser.quit()
    return guids


def getInfos(guids,proxy_pool):
    '''
    功能：获取数据
    @guids：快递员全局唯一标识列表
    @proxy_pool：代理IP池
    '''
    global data 
    infos = []#存储最终所有信息
    i = 0  #代理IP循环调度累加器
    j = 1  #爬取个数累加器
    for guid in guids:
        URL = 'https://www.kuaidi100.com/courier/searchapi.do?method=courierdetail&json={"guid":"'+guid[1]+'"}'  #数据所在URL
        user_agent = getUserAgent()
        my_user_agent = ("User-Agent",user_agent)
        print("正在爬取第"+str(j)+"个快递员信息...")
        j += 1 
        i += 1
        if len(proxy_pool)!=0 and i < len(proxy_pool):
            i=i
        elif len(proxy_pool)!=0 and i >= len(proxy_pool):
            i=0
        else:
            print("代理IP池资源已枯竭，正在更新代理IP池...")
            unchecked_proxies = getProxies(5)  #获取原始代理IP
            checked_proxies = mulTestProxies(unchecked_proxies)#多线程测试原始代理IP   
            proxy_pool = []
            for tmp_proxy in checked_proxies:
                if len(tmp_proxy)!=0:
                    proxy_pool.append(tmp_proxy)
            print("代理IP池更新完毕，共获取"+str(len(proxy_pool))+"个代理IP")
            i=0	
        proxy_addr = proxy_pool[i]
        proxy = urllib.request.ProxyHandler({"http":proxy_addr[0]})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        opener.addheaders=[my_user_agent]
        urllib.request.install_opener(opener)
        try:
            data = opener.open(URL).read() 
        except urllib.error.URLError as er2: 
            proxy_pool.remove(proxy_addr) #报错则移除改IP
            if hasattr(er2,"code"):
                print("错误代码："+str(er2.code))
            if hasattr(er2,"reason"):
                print("错误原因："+str(er2.reason))
        if type(data)==str:
            data = data
        else:
            data = data.decode()
        data_json = json.loads(data)
        company_name = data_json['courier']['companyName']  #公司名称
        courier_name = data_json['courier']['courierName']  #快递员姓名
        courier_tel = data_json['courier']['courierTel']  #手机号码
        work_time = data_json['courier']['workTime']  #工作时间
        score = data_json['courier']['score']  #得分
        xzq_full_name = data_json['courier']['xzqFullName']  #地区
        infos.append([guid[0],guid[1],company_name,courier_name,courier_tel,work_time,score,xzq_full_name])
        # 控制爬取频率，每100次爬取休息1分钟的，其他的每次爬取休息3秒
        if i%100==0:
            time.sleep(60)
        else:
            time.sleep(3)
    return infos

#################################
###5、数据提取与存储
################################# 
def dbCon():
    '''
    功能：连接MySQL数据库
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
    功能：数据库查询函数 
    @sql：定义SQL语句
    '''
    global res
    print("exeSQL: " + sql)
    #连接数据库
    con = dbCon()  #创建数据库的连接
    cur = con.cursor()  #通过获取到的数据库连接conn下的cursor()方法来创建游标
    try:
        tmp = cur.execute(sql) #通过游标cur 操作execute()方法可以写入纯sql语句
        res = cur.fetchmany(tmp)#cur.fetchone()只会使游标不断的向下移动
    except Exception as er:
        print('执行MySQL语句【' + str(sql) + '】时出如下错误：')        
        print(er)
    finally:
        cur.close()  #关闭游标
        con.commit()  #方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
        con.close()  #关闭数据库连接
    return res
	
def exeInsertSQL(sql,data_list):
    '''
    功能：数据库插入函数 
    @sql：定义插入SQL语句
    @data_list：插入数据列表
    ''' 
    con = dbCon()  #创建数据库的连接
    cur = con.cursor()
    try:
        n = cur.executemany(sql,data_list)
    except Exception as er:
        print('执行MySQL语句【' + str(sql) + '】时出如下错误：')        
        print(er)
    finally:
        cur.close()  #关闭游标
        con.commit()  #方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
        con.close()  #关闭数据库连接

def dataStore(school_info,xhr_guids,courier_info):
    '''
    功能：数据库存储 
    @school_info：学校信息
    @xhr_guids：数据XHR文件的全局唯一标识符
    @courier_info：快递员数据
    ''' 
    #存储学校信息
    table_name1 = 'school_info'
    exeSQL("drop table if exists " + table_name1)
    exeSQL("create table " + table_name1 + "(学校名称 varchar(100), 主管部门 varchar(50), 所在地 varchar(50), 层次 varchar(50), 类型 varchar(50));")
    insert_sql1 = "insert into " + table_name1 + " values(%s,%s,%s,%s,%s);"
    exeInsertSQL(insert_sql1,school_info)		
    #存储数据XHR文件的全局唯一标识符
    table_name2 = 'xhr_guids'
    exeSQL("drop table if exists " + table_name2)
    exeSQL("create table " + table_name2 + "(搜索关键词 varchar(100),全局标识符 varchar(50));")   
    insert_sql2 = "insert into " + table_name2 + " values(%s,%s);"
    exeInsertSQL(insert_sql2,xhr_guids)
    #存储快递员数据
    table_name3 = 'courier_info'
    exeSQL("drop table if exists " + table_name3)
    exeSQL("create table " + table_name3 + "(`搜索关键词` varchar(100),`全局标识符` varchar(50),`所属公司` varchar(50),`快递员姓名` varchar(20),`手机号码` varchar(20),`工作时间` varchar(100),`得分` varchar(30),`所属地区` varchar(50));")   
    insert_sql3 = "insert into " + table_name3 + " values(%s,%s,%s,%s,%s,%s,%s,%s);"
    exeInsertSQL(insert_sql3,courier_info)
    
#################################
###6、定义main()函数
#################################
def main():
    '''
    功能：主函数，调用相关函数    
    '''
    #---（1）获取初始代理IP池
    unchecked_proxies = getProxies(10)  #获取原始代理IP
    checked_proxies = mulTestProxies(unchecked_proxies)  #多线程测试原始代理IP   
    proxy_pool = []
    for tmp_proxy in checked_proxies:
        if len(tmp_proxy)!=0:
            proxy_pool.append(tmp_proxy)
            print("代理IP池获取完毕，共获取"+str(len(proxy_pool))+"个代理IP")
    #---（2）获取地理位置（搜索关键词）
    school_info = getSchoolInfo()  #获取全省高校信息
    final_loc = []  #提取搜索关键词
    for loc in school_info[1:]:
        final_loc.append(loc[0])
    '''预留全省街道信息获取接口
    sel_sql = 'select `province_name`\
                    ,`city_name`\
                    ,`county_name`\
                    ,`town_name`\
                    ,`village_name`\
            from    positionV1 ' +\
            'where  `province_name`="广东省" \
               and  city_name="广州市";'
    location = exeSQL(sel_sql)
    final_loc = []
    for loc in location:
        loc = loc[1]+loc[2]+loc[3]+loc[4]
        final_loc.append(loc)'''
    #---（3）获取数据
    xhr_guids = getGuids(final_loc)
    courier_info = getInfos(guids,proxy_pool) #爬取快递号码信息
    #---（4）存储数据
    dataStore(school_info,xhr_guids,courier_info)
  
if __name__ == "__main__":
    main()

