from django.template.defaulttags import url
from django.urls import path, include
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



urlpatterns = [
    path('<str:s>', views.ReplacerView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name='schema.yml'),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name='schema.yml'
         ),
    name="swagger-ui"
    ),
]
