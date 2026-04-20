from django.urls import path
from blog import views

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update')
]