from django.conf.urls import patterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^icons', TemplateView.as_view(template_name="homepage/icons.html")),
    (r'^', TemplateView.as_view(template_name="homepage/home.html")),
)