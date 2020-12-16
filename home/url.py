from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("beds",views.beds,name="beds"),
    path("chestofdrawer",views.chest,name="chest"),
    path("diningtable",views.dining,name="dining"),
    path("dressingtable",views.dressing,name="dressing"),
    path("sofa",views.sofa,name="sofa"),
    path("wardrobs",views.wardrobs,name="wardrobs")
        
]
