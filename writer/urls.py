from django.urls import path
from . import views

urlpatterns = [
    path("writer-dashboard",views.writer_dashboard, name="writer-dashboard"),
    path("create-article",views.create_article, name="create-article"),
    path("my-articles", views.my_articles, name="my-articles"),
    path("update-articles/<str:pk>", views.update_articles, name="update-articles"),
    path("delete-articles/<str:pk>", views.delete_articles, name="delete-articles"),
    path("account-management", views.account_management, name="account-management"),
    path("delete-account", views.delete_account, name="delete-account"),
]
