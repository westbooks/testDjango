from django.db import models

# Create your models here.

"""
class Author(models.Model):
    
    name = models.CharField(max_length=20)
    email = models.EmailField()
    descript = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name


class Tag(models.Model):
    
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.tag_name


class Blog(models.Model):

    caption = models.TextField(max_length=50)
    author = models.ForeignKey(Author.name)  # 一对一外键，关联作者模型
    tags = models.ManyToManyField(Tag, blank=True)  # 多对多，绑定tag模型
    content = models.TextField()

    publish_time = models.DateTimeField(auto_now_add=True)  # 日期，新增自动写入
    update_time = models.DateTimeField(auto_now=True)  # 日期，修改自动更新
    recommend = models.BooleanField(default=False)  # 是否为推荐博文

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)

    class Meta:
        # 排序
        ordering = ['-publish_time']
"""


class BlogsPost(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField()
    create_time = models.DateTimeField()


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


"""
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']


class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = models.TextField('内容', blank=True, default='')

    published = models.BooleanField('正式发布', default=True)

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'

"""


