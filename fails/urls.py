from django.conf.urls import patterns

urlpatterns = patterns('fails.views',
    (r'^add', 'add'),
    (r'^', 'list'),
)