from django.urls import path
from ekart import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("categories",views.CategoryView,basename="cat"),
router.register("products",views.ProductView,basename="prdt"),




urlpatterns=[


]+router.urls