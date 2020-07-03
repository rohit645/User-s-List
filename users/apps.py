from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "My Application"
    def ready(self):
        pass
        import requests, json
        from users.serializers import UsersSerializer
        from rest_framework.response import Response
        from users.models import Users

        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        jsonData = response.json()
        for data in jsonData:
            username = data['username']
            try:
                user = Users.objects.get(username=username)
            except (Users.DoesNotExist, Users.MultipleObjectsReturned):
                serializer = UsersSerializer(data=data)
                if(serializer.is_valid()):
                    serializer.save()
                else:
                    print("hey")
                return Response(serializer.data)