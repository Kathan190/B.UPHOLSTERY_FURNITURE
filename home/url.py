from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("beds",views.beds,name="beds"),
    path("chest",views.chest,name="chest"),
    path("dining",views.dining,name="dining"),
    path("dressing",views.dressing,name="dressing"),
    path("sofa",views.sofa,name="sofa"),
    path("wardrobs",views.wardrobs,name="wardrobs"),
    path("image", views.image, name="image")
        
]
