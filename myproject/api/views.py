from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task




# testing without db connection
person = {"p1":"tamim"}

@api_view(["GET","POST"])
def getData(request):
    global person
    if request.method == "GET":
        # person = {"name":'Tamim'}
        return Response(person)
    if request.method == "POST":
        data = request.data
        person = data
        return Response(f"person : {person}")


# testing with db connection
@api_view(["GET","POST",'DELETE'])
def taskList(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializers = TaskSerializer(tasks,many = True)
        return Response(serializers.data)
    if request.method == "POST":
        serializers = TaskSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    if request.method == "DELETE":
        task = Task.objects.get(id=request.data.id)
        task.delete()
        return Response("Item successfully deleted")
    # print(serializers)
    # return Response("hello world")


