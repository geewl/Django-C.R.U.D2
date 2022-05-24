import json
from unittest import result

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            owner = Owner.objects.create(
                name  = data["name"],
                email = data["email"],
                age   = data["age"]
            )

            return JsonResponse({"message" : "created!"}, status = 201)
        except KeyError:
            return JsonResponse({"message" : "KeyError"}, status = 400)

    def get(self, request):
        result = []
        owners = Owner.objects.all()

        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list = []

            for dog in dogs:
                dog_information = {
                    "name" : dog.name,
                    "age"  : dog.age
                }
                dog_list.append(dog_information)

            owner_information = {
                "name"  : owner.name,
                "email" : owner.email,
                "age"   : owner.age
            }
            result.append(owner_information)

        return JsonResponse({"result" : result}, status = 200)

class DogView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            owner = Owner.objects.get(name = data["owner"])
            Dog.objects.create(
                name  = data["name"],
                age   = data["age"],
                owner = owner
            )

            return JsonResponse({"message" : "created!"}, status = 201)
        except KeyError:
            return JsonResponse({"message" : "KeyError"}, status = 400)

    def get(self, request):
        result = []
        dogs = Dog.objects.all()

        for dog in dogs:
            dog_information = {
                "dog_id"   : dog.id,
                "name"     : dog.name,
                "age"      : dog.age,
                "owner_id" : dog.owner.id,
                "owner"    : dog.owner.name
            }
            result.append(dog_information)

        return JsonResponse({"result" : result}, status = 200)