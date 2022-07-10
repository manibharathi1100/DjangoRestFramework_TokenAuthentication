from msilib.schema import CustomAction
from django.urls import path, include
# from .views import AccountViewSet
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .auth import CustomAuthToken

router=DefaultRouter()
router.register('', views.AccountViewSet, basename='account')

urlpatterns = [
    path('AccountViewSet/', include(router.urls)),
    path('server/incoming_data/', views.account_view, name="account_view"),
    path('api_urls/', views.api_urls, name="api_urls"),
    path('create/', views.create, name="create"),
    path('read/<str:pk>/', views.read, name="read"),
    path('edit/<str:pk>/', views.edit, name="edit"),
    path('delete/<str:pk>/', views.delete, name="delete"),

    path('login/', obtain_auth_token, name="login"),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view()),
]

