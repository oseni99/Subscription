from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from writer.models import Article
from .models import Subscription
from .forms import UpdateUserForm
from account.models import CustomUser
from decimal import Decimal


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


@login_required(login_url="login")
def subscription_plans(request):
    return render(request, "client/subscription_plans.html")


@login_required(login_url="login")
def account_management(request):
    form = UpdateUserForm(instance=request.user)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect ("client-dashboard")
    return render(request,"client/account_management.html", {
        "update_user":form
        })        



@login_required(login_url="login")
def account_deletion(request):
    if request.method == "POST":
        my_profile = CustomUser.objects.get(email=request.user)
        my_profile.delete()
        return redirect("login")
    return render(request, "client/delete_account.html")


@login_required(login_url="login")
def create_sub(request,subID,plan):
    custom_user = get_object_or_404(CustomUser, email=request.user)
    first_name = custom_user.first_name
    last_name = custom_user.last_name
    full_name = first_name + " " + last_name

    select_sub_plan = plan 
    if select_sub_plan == "basic":
        sub_cost = Decimal("4.99")
    elif select_sub_plan == "premium":
        sub_cost = Decimal("9.99")
    else:
        return HttpResponseBadRequest("Invalid Susbscription Plan")

#after paypal saves it to its own db its best to be able to get it to link to django also 
#whenever you try to create to the db try and alwsys use a try and except to be able to ctach errors related 
    try:
        subscription = Subscription.objects.create(
            subscriber_name = full_name,
            subscriber_plan = select_sub_plan,
            subscriber_cost = sub_cost,
            paypal_sub_id  = subID,
            is_active = True,
            user = request.user
            )
    except Exception as e:
        return HttpResponseBadRequest(f"An error has occured at: {e}")
        
    return render(request,"client/create_sub.html",{
            "sub_plan":select_sub_plan
            })

        