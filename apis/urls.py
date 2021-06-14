from django.urls import path

from apis.views import UserCreateView, UserLoginView

urlpatterms = [
    path('v1/user/create/', UserCreateView.as_view(), name='apis_vi_user'),
    path('v1/users/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
]