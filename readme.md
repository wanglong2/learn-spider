## 安装selenium环境

> 安装selenium
>
> ​	pip install selenium
>
> 安装webdriver (chrome 版本)
>
> > > 1、查看自己的chrome版本
> > >
> > > ​	在chrome的搜索栏中输入 chrome://version/  Google Chrome：131.0.6778.86 (正式版本) （64 位） (cohort: Stable) 
> > >
> > > 2、找到对应的版本
> > >
> > > ​		130及以后的版本
> > >
> > > > > https://googlechromelabs.github.io/chrome-for-testing/   

> > > 3、下载后放入chrome所在目录
> > >
> > > > 并且放入虚拟环境中 

## xpath的一些芝士

* 从根目录开始

  > /html/body ...............

* 通过属性锁定

  > 如div的属性   
  >
  > > > div[@class='typing']
  > >
  > > 如果想要同时拥有两个属性的标签
  > >
  > > ​	div[@class='typing' and @class='1']
  > >
  > > 或者关系的 and 改为or 即可
  >
  > div[1] 数数 使用1开始的

  

  

  # selenium

  * 添加一些反扒手段

    > 包含头文件 from selenium.webdriver.chrome.options import Options
    >
    > chrome_options = Options()
    >
    >  
    >
    > * 添加user-agent
    > * 使用ip



* 等待子页面加载

  > 包含头文件
  >
  > ​	from selenium.webdriver.support.ui import WebDriverWait
  > ​	from selenium.webdriver.support import expected_conditions as EC
  >
  > 