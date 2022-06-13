from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View): #view 클래스는 view를 붙여주는게 좋다. model이랑 구별하기 위해서! owner 클래스를 view파일에서 임포트해서 써야하기 때문도 있다.
    #post의 목적: 추가하거나 수정하는건 http의 목적. OwnerView에 있는 post의 목적은 주인의 정보를 추가하는것!
    #그럼 정보를 어디서 받냐. client에게 주인의 정보를 받아서 db에 저장.
    #내가 뭘 해야하고 그걸 하려면 어떤 과정을 거쳐야하는가 로직 부터 짜는 습관이 필요! 목적과 과정을 적는 습관을 기르자.

    def post(self, request): #request에는 body라는 속성이 있고, 이 body를 불러옴? body는 json 형태다.
        data = json.loads(request.body) #client에게 주인의 정보를 받는 코드. class로 만들어진 instance가 들어옴. 
        Owner.objects.create( #objects는 major 클래스. orm 관련된 메서드를 사용할 수 있게 한다. 예:create
            name = data['name'], #왼쪽은 model.py에서 정의한 field. name에는 name에 해당되는 value
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'messasage':'created'}, status=201)
    """예시 row하나 만들기. row하나 객체 하나임
    request. body = {
        "name" : "kang", => data('name')는 'kang'값이 들어옴. 만약 "last_name" :"kang" 이라면 error 발생! 프론트랑 잘 얘기해서 'name라는 키로 달라' 해야함.
        "email" : "kang@naver.com",
        "age" : "22
    }
    """
    def get(self, request):
        #get의 목적: 들어있는지는 중요하지 않음. 정보가 없으면 그냥 빈 리스트를 return 하면 되니까. 주인들의 정보를 가져오는 것이 주 목적.
        #db에 있는 모든 주인의 정보를 조회하고, 조회한 정보들을 client가 볼 수 있도록 가공하는 것이 get의 목적
        owners = Owner.objects.all() #주인정보다가져와! owner 테이블에 대해 orm을 사용하겠다. all메서드를 사용했을때는 queryset 데이터가 return 됨
        # 왜 queryset을 dict으로 만들고 다시 queryset으로 하는가?
        # -> json 형태로 바꾸기 위해. 왜?
        #파이썬에서 만든 list객체는 데
        results  = []

        for owner in owners:
            results.append(
                {
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age
                }
            )  
        """예시
        for owner in owners:
            owner_information{
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age
            }
            result.append(owner_information)
        """
        return JsonResponse({'resutls':results}, status=200) #위에 쓴걸 results 안에 append


#주인정보 등록하는 방법
#1. 정보주는 client가 뭘 모를때 owner 객체를 불러오는 방법. get 메서드는 무조건 데이터가 1개만 있어야 한다.
# front가 준 데이터가 없으면 error발생. 이 때 적절한 응답을 주기 위해서 try except로 응답 처리.
#2. id를 직접 주는 방법. id=data['owner_id']
#owner=['owner_id']로 바로 넣을 수도 있지만 front가 주는 id값은 확실하지않으니 Owner.object.get(id=data['owner_id'])으로 판단. 
class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner_id = data['owner']
        )
        return JsonResponse({'messasage':'created'}, status=201)


    def get(self, request):
        dogs = Dog.objects.all()
        results  = []

        for dog in dogs:
            results.append(
                {
                   "name" : dog.name,
                   "age" : dog.age,
                   "owner_name" : dog.owner.name
                }
            )  
        return JsonResponse({'resutls':results}, status=200)

#######################################################################

#역참조를 아느냐
#이중 for문을 사용할줄 아느냐
#dog_set => 역참조를 사용할 수 있게 하는 매니저. all(), filter(), counter()등 사용 가능.
#역참조되는 이름을 다 소문자로 바꾸고 _set을 붙여줌
#foreingkey를 연결한 클래스에서 역참조를 부를 때 사용하는 `related_name=아뭐지` 매니저 이름을 정하는 것. dog_set이 dogs가 됨.
#dog 클래스 안에는 name 속성 등이 있음. owner 클래스는 dog를 역참조해서 dog정보를 알 수 있다...?
#역참조할때는 특정 객체가 정해져 있어야 함. 왜냐하면 어떤 주인의 역참조를 가져와야 할지 알아야 하니까.
#owner.dog_set.all은 Dog.objects.filter(owner=owner) 와 같은 코드. [Dog1, Dog2, ...]로 return
class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results  = []

        for owner in owners:
            results.append(
                {
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age,
                   "dog_list" : [{"dog_name":dog.name} for dog in Dog.objects.filter(owner_id=owner.id)]
                }
            )  
        return JsonResponse({'results':results}, status=200)
