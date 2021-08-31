from django.urls import path
from .views import signup, signin, signout, list, detail, good, read, BoardCreate

urlpatterns = [
  path('signup/', signup, name='signup'),
  path('login/', signin, name='login'),
  path('logout', signout, name='logout'),
  path('list/', list, name='list'),
  path('detail/<int:pk>/', detail, name='detail'),
  path('good/<int:pk>', good, name='good'),
  path('read/<int:pk>', read, name='read'),
  path('create/', BoardCreate.as_view(), name='create')
]