"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from quickstart.views import UserDetail, UserList, Customer, Account, Background
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.conf.urls import handler404

# from django.core.exceptions import PermissionDenied
# from django.http import HttpResponse

# def response_error_handler(request, exceptions=None):
#     return HttpResponse('Error handler content', status=404)

# def permission_denied_view(request):
#     raise PermissionDenied

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'deals-customers', views.Customer)
router.register(r'account', views.Account)
router.register(r'background', views.Background)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # path('403/', permission_denied_view),
    path('', include(router.urls)),
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += router.urls

handler404 = "quickstart.views.error_404_view"

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

# handler403 = response_error_handler
