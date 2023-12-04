from django.contrib import admin
from django.urls import path

from currency.views import (
    rate_list,
    contactus_list,
    source_list,
    source_create,
    source_update,
    source_delete,
    source_details
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('contactus/list/', contactus_list),
    path('source/list/', source_list),
    path('source/create/', source_create),
    path('source/update/<int:pk>/', source_update),
    path('source/delete/<int:pk>/', source_delete),
    path('source/details/<int:pk>/', source_details),
]
