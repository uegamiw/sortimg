from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
   # path('', views.TopView.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'), # 追加
    path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'), # サインアップ
    path('signup_done/', views.SignupDone.as_view(), name='signup_done'), # サインアップ完了
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'), # 登録情報の更新
    path('password_change/', views.PasswordChange.as_view(), name='password_change'), # パスワード変更
    path('password_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
]