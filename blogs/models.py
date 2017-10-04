from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
            return self.name
class Post(models.Model):
    #文章数据库
    #标题，正文，文章创作和修改时间，文章摘要，作者，分类和标签
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=100,blank=True)

    category=models.ForeignKey(Category)#一对多
    tags=models.ManyToManyField(Tag,blank=True)#多对多

    author = models.ForeignKey(User)
    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-created_time']