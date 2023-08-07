from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.urls import re_path
from elderlystore.settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/products/', include('products.urls')),
    path('api/quest/', include('quest.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
]
