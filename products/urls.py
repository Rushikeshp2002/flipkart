from django.urls import path

from . import views

urlpatterns = [
    path("data/<int:id>",views.getSingleProdct,name="getSingleProduct"),
    path("data/",views.getAll,name="getAll"),
    path("data/<slug:cat>",views.getCategoryProducts,name="getCategoryProducts"),
    path("data/<slug:keyword>",views.search,name="search"),
    path("increment/<int:pid>/<int:uid>",views.getIncrement,name="increment")
]
