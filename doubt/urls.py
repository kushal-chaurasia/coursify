from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('doubt/' , views.doubt , name="doubt"),
    path('doubtpost/<int:id>' , views.doubtpost , name="doubtpost"),
    path('contactus/' , views.contactus , name="contactus"),
    path('liveclass/' , views.liveclass , name="liveclass"),
    path('board/' , views.board , name="board"),
]
