from django.urls import path

from . import views

app_name = 'funnymanga'
urlpatterns = [
    # ex: /funnymanga/
    path('', views.index, name='index'),
    # ex: /funnymanga/5/
    path('<int:picture_id>/', views.detail, name='detail'),
    # ex: /funnymanga/5/comment/
    path('<int:picture_id>/comment/', views.comment, name='comment'),
]