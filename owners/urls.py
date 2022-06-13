from django.urls import path

from owners.views import OwnersView, DogsView # form .views로 해도 돌아간다!

urlpatterns = [
    #path('', OwnersView.as_view()),  => 얘로하면 http://127.0.0.1:8000/owners 
    path('/owners', OwnersView.as_view()),  # http://127.0.0.1:8000/owners/owners
    path('/dogs', DogsView.as_view()), # http://127.0.0.1:8000/dogs
]
#as.view() => 해당 클래스에서 http 메서드랑 일치하는 것을 찾아서 호출할 수 있게끔 도와줌
#POST나 GET이나 endpoint는 같지만 as.view()로 음....

#어떤 컴퓨터든 내 ip 주소를 가리키는 127.0.0.1
#서버를 켜야 구동된다. 아주 많이 하는 실수 python manage.py runserver. 내 컴퓨터로만 서버에 접속 할 수 있다.
#로그인 실습할때는 python manage.py runserver 0:0000 로 하면 외부에서도 접속할 수 있다.