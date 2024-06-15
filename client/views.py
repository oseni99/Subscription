from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from writer.models import Article
from .models import Subscription

@login_required(login_url="login")
def client_dashboard(request):
    try:
        sub_details = Subscription.objects.get(user=request.user, is_active=True)
        sub_plan = sub_details.subscriber_plan
        return render(request, "client/client_dashboard.html", {
        "subscription_plan":sub_plan
        })
    except Subscription.DoesNotExist:
        sub_plan = "None"
        return render(request, "client/client_dashboard.html", {
        "subscription_plan":sub_plan
        })
   


@login_required(login_url="login")
def browse_articles(request):
    try:
        sub_details = Subscription.objects.get(user=request.user, is_active=True)
        current_sub_plan = sub_details.subscriber_plan

        if current_sub_plan == "basic":
            articles = Article.objects.all().filter(is_premium=False)
        elif current_sub_plan == "premium":
            articles = Article.objects.all()
        return render(request,"client/browse_articles.html",{
            "client_articles": articles
            })
    except Subscription.DoesNotExist:
        return render(request, "client/locked_sub.html")


@login_required(login_url="login")
def locked_sub(request):
    return render(request, "client/locked_sub.html")