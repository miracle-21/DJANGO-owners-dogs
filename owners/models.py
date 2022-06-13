from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField(default = '0') # null=true. 원래 차있는게 이본인데 빈값이어도 데이터 만들수 있게 한다. dafault를 하면 값없으면 이값으로 정의한다는 뜻. 오홍.
    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default = '0')
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE) #다른앱이름.class이름 -> 다른 앱의 클래스 가져올수있음. 뒤에 옵션 6가지가 있는데 어떤게 있는지 나중에 살펴봐라
    class Meta:
        db_table = 'dogs'