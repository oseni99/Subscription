from django.urls import path
from . import views

urlpatterns = [
    path("client-dashboard",views.client_dashboard, name="client-dashboard"),
    path("browse-articles",views.browse_articles, name="browse-articles"),
    path("locked-subscription",views.locked_sub, name="locked-subscription"),
    path("subscription-plans",views.subscription_plans, name="subscription-plans"),
    path("account-management",views.account_management, name="client-management"),
    path("delete-account",views.account_deletion, name="client-delete"),
    path("create-sub/<int:subID>/<str:plan>",views.create_sub, name="create-sub"),
]
