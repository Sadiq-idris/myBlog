from django.urls import path
from . import views

urlpatterns = [
    path("", views.Posts.as_view(), name="post"),
    path("<int:pk>", views.DetailPost.as_view(), name="post_detail"),
    path("send", views.sendComment, name="send"),
    path("getComment/<int:pk>", views.getComment, name="getComment"),
    path("update-post/<int:pk>", views.UpdatePost.as_view(), name="update_post"),
    path("delete-post/<int:pk>", views.DeletePost.as_view(), name="delete_post"),
]