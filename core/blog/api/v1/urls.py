from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register('post',views.PostViewset,basename='post')
router.register('category',views.CategoryViewset,basename='category')
urlpatterns = router.urls

# urlpatterns = [
#     path('post/', views.PostViewset.as_view({'get':'list'}),name='post-list'),
#     path('post/<int:pk>', views.PostViewset.as_view({'get':'retrieve'}),name='post-detail')
# ]