from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

# class OwnersView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Owner.objects.create(
#             name = data['name'],
#             email = data['email'],
#             age = data['age']
#         )
#         return JsonResponse({'messasage':'created'}, status=201)

#     def get(self, request):
#         owners = Owner.objects.all()
#         results  = []

#         for owner in owners:
#             results.append(
#                 {
#                    "name" : owner.name,
#                    "email" : owner.email,
#                    "age" : owner.age
#                 }
#             )  
#         return JsonResponse({'resutls':results}, status=200)


      
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

# class DogsList(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Dog.objects.create(
#             name = data['name'],
#             age = data['age'],
#         )
#         return JsonResponse({'messasage':'created'}, status=201)

#     def get(self, request):
#         dogs = Dog.objects.all()
#         results  = []

#         for dog in dogs:
#             results.append(
#                 {
#                    "name" : dog.name,
#                    "age" : dog.age,
#                    "owner_name" : dog.owner.name
#                 }
#             )  
#         return JsonResponse({'resutls':results}, status=200)