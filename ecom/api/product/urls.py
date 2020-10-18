from rest_framework import routers
from django.urls import path, include

from . import views


# router = routers.SimpleRouter()  # SimpleRouter is the bare minimum
# we use the DefaultRouter to be able to use urlpatterns with path and include
router = routers.DefaultRouter()
router.register(r'', views.ProductViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),  # understand that there is no '' enclosing router.urls
]
