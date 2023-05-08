from django.urls import path
from . import views

app_name = 'blog-app'

urlpatterns = [
    path('',views.post_list, name='post-list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail, name="post-detail"),
    
]
