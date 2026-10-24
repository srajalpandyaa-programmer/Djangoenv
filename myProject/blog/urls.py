from django.urls import path, re_path
from . import views
urlpatterns = [
    
    #path('blog/', views.home, name='home'),
    #path('blog/about/', views.about, name='about'),
    #path('post/<int:post_id>/', views.post_details, name='post_detail'),
    #path('user/<str:username>/', views.user_profile, name='user_profile'),
    #path('article/<int:year>/<int:month>/<int:days>/', views.article_by_date,name='article_by_date'),

    #re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_date, name='article_by_date')
    
    #path('', views.post_list, name='post_list'),
    #path('',views.home, name="home"),
    #path('',views.blog_details,name="blog_details")
    #path('',views.blog_list,name="blog_list")
    #path('',views.home,name="home"),
    #path('about/',views.about,name="about"),
    path('home/',views.home,name="home"),
    path('',views.blog,name="blog"),

]
