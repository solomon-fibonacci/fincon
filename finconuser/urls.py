from django.conf.urls import url
from finconuser import views
from django.contrib.auth.decorators import login_required


urlpatterns = [url(r'^signup/', views.SignUpView.as_view(), name='signup'),
               url(r'^signin/', views.SignInView.as_view(), name='signin'),
               url(r'^signout/', views.SignOutView.as_view(), name='signout'),
               url(
               r'^home/',
               login_required(views.UserHomeView.as_view(), login_url='/user/signin/'),
               name='home')]
