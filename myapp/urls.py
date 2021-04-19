from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contact', views.ContactViewSet)
router.register(r'ourwork', views.OurworkViewSet)
router.register(r'testomonial', views.TestomonialViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
