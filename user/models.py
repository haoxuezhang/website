from django.db import models
from django.contrib.auth.models import AbstractUser

from DjangoUeditor.models import UEditorField


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField('呢称', max_length=50, default='好学长')
    gender = models.CharField('性别', default='male', max_length=6, choices=(("male", "男"), ("female", "女")))
    mobile = models.CharField('手机号', max_length=11, null=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Important(models.Model):
    title = models.CharField(max_length=255,verbose_name='标题')
    image = models.ImageField(upload_to='img/%Y/%m',verbose_name='首页大图')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '首页大图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Solutions(models.Model):
    solutionCate = models.ForeignKey('SolutionCate', verbose_name='解决方案分类')
    title = models.CharField(max_length=255, verbose_name='标题')
    describe = models.CharField(max_length=255, verbose_name='描述')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='文章图示')
    context = UEditorField(verbose_name='文章内容', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/",
                           default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '解决方案'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SolutionCate(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name='分类ID')
    name = models.CharField(max_length=50, verbose_name='文章分类')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '解决方案分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Products(models.Model):
    productCate = models.ForeignKey('ProductCate', verbose_name='分类')
    title = models.CharField(max_length=255, verbose_name='标题')
    describe = models.CharField(max_length=255, verbose_name='描述')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='案例图片')
    context = UEditorField(verbose_name='文章内容', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/",
                           default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '产品展示'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ProductCate(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name='分类ID')
    name = models.CharField(max_length=50, verbose_name='文章分类')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '产品展示分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Example(models.Model):
    title = models.CharField(max_length=255, verbose_name='文章标题')
    describe = models.CharField(max_length=255, verbose_name='描述')
    logo = models.ImageField(upload_to='img/%Y/%m', verbose_name='服务对象logo')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='案例图片')
    context = UEditorField(verbose_name='文章内容', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/",
                           default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '客户案例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class News(models.Model):
    newsCate = models.ForeignKey('NewsCate', verbose_name='文章分类')
    title = models.CharField(max_length=255, verbose_name='文章标题')
    tag = models.CharField(max_length=10, verbose_name='标签')
    describe = models.CharField(max_length=255, verbose_name='描述')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='文章图示')
    context = UEditorField(verbose_name='文章内容', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/",
                           default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    click_count = models.IntegerField(default=0, verbose_name='点击数')

    class Meta:
        verbose_name = '新闻动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class NewsCate(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name='分类ID')
    name = models.CharField(max_length=50, verbose_name='分类')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '新闻动态分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Aboutus(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='地点截图', default='1')
    context = UEditorField(verbose_name='公司介绍', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/",
                           default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




