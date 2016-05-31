# TingClass
批量下载TingClass的MP3文件，简化手动下载模式。

用户手册
Note: TingClass采用了Python3的标准库urllib，引用了BeautifulSoup4，需要提前安装。
Windows下可以直接用pip install bs4指令进行安装；
mp3_spider函数的参数说明：
  参数1： 本地目录，请自行创建；
  参数2： 节目目录地址，请去掉最后的"1.html"；
  参数3： 节目目录页码，下图中就下载第1页；
  参数4： 节目目录页码超出值，小于该值的会搜索；
  参数5： 节目名称；

import TingClass;
TingClass.mp3_spider("H:\\english\\9695-科学一刻", "http://www.tingclass.net/list-9695-", 3, 5, "科学一刻");
TingClass.mp3_spider("H:\\english\\201605-VOA慢速英语", "http://www.tingclass.net/list-8335-", 1, 2, "VOA慢速英语");
TingClass.mp3_spider("H:\\english\\201604-VOA常速英语", "http://www.tingclass.net/list-9768-", 1, 3, "VOA常速英语");
