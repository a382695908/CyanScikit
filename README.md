# CyanScikit
CyanScikit是一个综合类的科技网站，完成于2016/03

# 2.0介绍
在之前的1.0版本中，开发追求的过于详细，于是在2.0版本中开始进行了优化和精简， 希望大家喜欢<br>

# 环境介绍
python 3.4<br>
django1.10.4<br>
mysql 5.6<br>

# 版本介绍
master分支是最原始的版本，即1.0<br>
2.0是目前开发维护的版本<br>

# 后台管理
url:127.0.0.1:8000/admin/ <br>
账号和密码都是 cyanscikit <br>

# 数据库文件备份
在data_sql 目录下 <br>
msyql数据库备份：/usr/bin/mysqldump -uusername -ppassword databasename  --default-character-set=utf8 --opt -Q -R >./backup.sql <br>
恢复：/usr/bin/mysql -uusername -ppassword databasename <./backup.sql <br>
如果出现中文乱码问题，在最后加上--default-character-set=utf8;

# 展示
<img src="https://github.com/Thinkgamer/CyanScikit/blob/2.0/docs/show/%E9%A6%96%E9%A1%B5.png" alt="首页" align=center />
<img src="https://github.com/Thinkgamer/CyanScikit/blob/2.0/docs/show/blog.png"  alt="博客" align=center />
<img src="https://github.com/Thinkgamer/CyanScikit/blob/2.0/docs/show/news.png"  alt="新闻" align=center />
<img src="https://github.com/Thinkgamer/CyanScikit/blob/2.0/docs/show/talks.png"  alt="留言板" align=center />
<img src="https://github.com/Thinkgamer/CyanScikit/blob/2.0/docs/show/marksts.png"  alt="外包中心" align=center />

