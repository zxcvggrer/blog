from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown

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
    def save(self,*args,**kwargs):
        if not self.excerpt :
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            #self.excerpt = strip_tags(md.convert(self.body))[:54]
            self.excerpt = md.convert(self.body)[:54]
        super(Post, self).save(*args, **kwargs)
    category=models.ForeignKey(Category)#一对多
    tags=models.ManyToManyField(Tag,blank=True)#多对多

    author = models.ForeignKey(User)
    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-created_time']

    Num_views=models.PositiveIntegerField(default=0)
    #增加Num_views记录阅读量
    def increase_view(self):
        self.Num_views += 1
        self.save(update_fields=['Num_views'])


    