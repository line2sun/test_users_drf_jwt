from users.views import ExampleUserView
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^auth-token-verify/$', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^example/', ExampleUserView.as_view()),

]
