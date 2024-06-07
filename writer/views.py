from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ArticleForm
from .models import Article

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

    article = Article.objects.get(id=pk)

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