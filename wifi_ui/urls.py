from django.urls import path


from wifi_ui import views

urlpatterns =[
    path('', views.index, name='index'),
    path('wifi_ui/', views.connect, name='connect')
]