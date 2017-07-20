# django博客

## 注意点
1. Django按照INSTALLED_APPS中中模块的添加顺序查找Templates，如果不同APP下templates有同名.html文件，则会冲突。
解决方法：在APP的templates文件夹下创建创建以APP为名称的目录，将html文件放入新创建的文件夹下。
