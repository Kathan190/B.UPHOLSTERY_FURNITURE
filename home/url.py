from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("beds",views.beds,name="beds"),
    path("chestofdrawer",views.chestofdrawer,name="chestofdrawer"),
    path("diningtable",views.diningtable,name="diningtable"),
    path("dressingtable",views.dressingtable,name="dressingtable"),
    path("sofa",views.sofa,name="sofa"),
    path("wardrobs",views.wardrobs,name="wardrobs")
        
]
