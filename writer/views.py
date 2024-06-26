from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ArticleForm, UpdateUserForm
from .models import Article
from account.models import CustomUser

@login_required(login_url="login")
def writer_dashboard(request):
    return render(request, "writer/writer_dashboard.html")


@login_required(login_url="create-article")
def create_article(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            # article.date_posted = timezone.now()
            article.user = request.user 
            article.save()
            return redirect("my-articles")
    else:
        form = ArticleForm()

    return render(request, "writer/create_article.html",{
        "article_forms":form
        })

@login_required(login_url="login")
def my_articles(request):
    current_user = request.user.id   # getting the user with the specific id in case of 

    article = Article.objects.all().filter(user=current_user)

    return render(request, "writer/my_articles.html",{
        "all_articles":article
        })
    


@login_required(login_url="login")
def update_articles(request, pk):
    try:
        article = Article.objects.get(id=pk, user=request.user)
    except:
        return redirect("my-articles")

    form = ArticleForm(instance=article)  # using that specific id to make sure its not blank and the forms we trying to update/receive wuth the url gets in that form straight up 
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)  # sending that form with that instance of that article with tat specific article in it 
        if form.is_valid():
            # article.date_edited = timezone.now()
            form.save()
            return redirect("my-articles")
    else:
         form = ArticleForm(instance=article)
    return render(request, "writer/update_article.html", {
            "update_articles":form
        })

@login_required(login_url="login")
def delete_articles(request, pk):
    try:
        article = Article.objects.get(id=pk, user=request.user)
    except:
        return redirect("my-articles")
    if request.method == "POST":
        article.delete()
        return redirect("my-articles")
    return render(request, "writer/delete_article.html")


@login_required(login_url="login")
def account_management(request):
    form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("writer-dashboard")
    return render(request, "writer/account_management.html",{
        "update_user":form
        })

@login_required(login_url="login")
def delete_account(request):
    if request.method == "POST":
        deleteUser = CustomUser.objects.get(email=request.user) #this gets the email of that particular user signed in 
        deleteUser.delete()
        return redirect("login")
    return render(request, "writer/delete_account.html")