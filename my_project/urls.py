from django.contrib import admin
from django.urls import path
import content.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content.views.homepage),
    path('article/<int:id>/', content.views.article),
    path('category/<int:id>/', content.views.categories),
    path('type/<int:id>/', content.views.types),
]