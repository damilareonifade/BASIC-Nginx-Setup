from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('split-test/',TemplateView.as_view(template_name='index.html')),
    path('p1/',views.homepage,name='p1_html'),
    path('p2/',TemplateView.as_view(template_name='p2.html'),name='p2_html'),

]
