"""crud2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

urlpatterns = [
    path('owners', include('owners.urls')), # http://127.0.0.1:8000/owners 주소를 요청하면 owners.url로 이동(owners 앱에 있는 url로 이동)
    #api에 없는 주소면 not found 예)http://127.0.0.1:8000/users
    # path('movies', include('movies.urls')),
]

