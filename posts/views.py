from .models import Post, Credit
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CreditForm
from django.db.models import F, Sum, Count

#from django.http import HttpResponseRedirect
#from django.urls import reverse

# Create your views here.
def postlist(request):
    posts = Post.objects.all()
    return render(request, 'postlist.html', {'posts': posts})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postlist')
        else:
            return redirect('postlist')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    credits = Credit.objects.filter(time=post.time)

    form = CreditForm(request.POST)

    score = 0

    if form.is_valid():
        form.save()
        total = (Credit.objects.filter(time=post.time).aggregate(
                total=Sum(F('credit') * F('grade'))
                    )['total']
                )
        credit_sum = (Credit.objects.filter(time=post.time).aggregate(
                credit_sum=Sum('credit')
                    )['credit_sum']
                )
        score = round(total / credit_sum,2)
        return render(request,'posts/detail.html', {'post': post, 'credits': credits, 'score': score})
    else:
        return render(request,'posts/detail.html', {'post': post, 'credits': credits, 'score': score})

