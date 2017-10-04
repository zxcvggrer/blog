from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blogs.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):

    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        #print(form)
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            comment.post = post
            #print(comment.post)
            #print('------------------')
            comment.save()
            return redirect(post)

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blogs/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    #return redirect(post)
    return redirect(post)