from django.contrib import admin
from django.urls import path

import fiemapp.views

urlpatterns = [
    path("",fiemapp.views.home),
    path("dashboard/",fiemapp.views.dashboard),
    path("addproducts/",fiemapp.views.addproducts),
    path("insproducts/",fiemapp.views.insproducts),
    path("listproduct/",fiemapp.views.listproduct),
    path("delproduct/",fiemapp.views.delproduct),
    path("login/",fiemapp.views.login),
    path("loginck/",fiemapp.views.loginck),
    path("logout/",fiemapp.views.logout),
    path("about/",fiemapp.views.about),
    path("contact/",fiemapp.views.contact),
    path("catalogue/",fiemapp.views.catalogue)




]
