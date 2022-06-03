from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import Profile, Post, Block
from datetime import datetime

# Create your views here.

def view_profile(request):
    context={"profile": Profile.objects.filter(user=request.user).first(), "posts": Post.objects.filter(author__user=request.user).all()}
    return render(request, "profile.html", context=context)


def view_blocked_users(request):
    if request.method == 'GET':
        blocked_users = Block.objects.filter(blocker__user=request.user)
        all_users = Profile.objects.exclude(user__in=blocked_users.values('blocked__user').all()).all()
        context = {"blocked_users": blocked_users, "not_blocked_users": all_users}
        return render(request, "blockedUsers.html", context=context)
    elif request.method == 'POST':
        toBlockUsername=request.POST['toBlock']
        profileToBlock=Profile.objects.filter(user__username=toBlockUsername).first()
        profile=Profile.objects.filter(user=request.user).first()
        Block.objects.create(blocker=profile, blocked=profileToBlock)
        return redirect(view_blocked_users)

def view_posts(request):
    # se izvlekuvaat site korisnici koi go blokirale tekovniot korisnik
    blocked_by=Block.objects.filter(blocked__user=request.user).values_list('blocker__user').all()
    # se zemaat samo onie postovi koi se od korisnici koi ne go blokirale tekovniot korisnik
    posts=Post.objects.exclude(author__user__in=blocked_by).exclude(author__user=request.user)
    context = {"posts":posts}
    return render(request, "posts.html", context=context)

def add_post(request):
    if request.method == "GET":
        return render(request, "addPost.html")
    if request.method == "POST":
        title=request.POST['title']
        content=request.POST['content']
        author=Profile.objects.filter(user=request.user).first()
        datetime_now=datetime.now()

        # zacuvuvanje na postot
        Post.objects.create(title=title, content=content, author=author, date_created=datetime_now, last_modified=datetime_now, file=request.FILES['file'])

        return redirect(view_profile)

