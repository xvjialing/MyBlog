# django博客

## 注意点
1. Django按照INSTALLED_APPS中中模块的添加顺序查找Templates，如果不同APP下templates有同名.html文件，则会冲突。
解决方法：在APP的templates文件夹下创建创建以APP为名称的目录，将html文件放入新创建的文件夹下。

2. Models: Django中通常一个Model对应一张数据表,django中Model以类的形式表现,它包含了一些基本字段和数据的一些行为.ORM:对象关系映射,隐藏了数据访问细节,不需要编写SQL语句.

3. Admin:Admin是Django自带的一个自动化数据管理界面,被授权的用户可以直接在Admin中管理数据库,Django提供了许多正对Admin的定制功能.
* 配置Admin:

python manage.py createsuperuser 创建超级用户

http://localhost:8000/admin Admin入口

修改settings.py中LANGUAGE_CODE='zh_Hans'可使管理界面变为中文

配置应用:在应用下admin.py中引入自身的modles模块(或里面的模型类),编辑admin.py : admin.site.register(modles.Artical)

修改数据默认显示名称:在Atical类下添加一个方法,根据python版本选择_str_(slef)(Python3)或者_unicode_(slef)(python 2.7)
返回 return self.title