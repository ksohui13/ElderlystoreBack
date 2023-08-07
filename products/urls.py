from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from products.views import ProductViewSet,ReviewViewSet,CommentViewSet, ProQuestViewSet


router = DefaultRouter()
router.register('product', ProductViewSet) 
router.register('review', ReviewViewSet)
router.register('comment', CommentViewSet)
router.register('quest', ProQuestViewSet)

urlpatterns = [
    #라우터
    path('router/', include(router.urls)), 
]