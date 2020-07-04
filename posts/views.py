from .models import Post, Credit
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CreditForm
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
