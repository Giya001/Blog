from django.urls import path

from blog import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:blog_id>/detail',views.detail,name='detail'),
    path('<int:blog_id>/update',views.update,name='update'),

]