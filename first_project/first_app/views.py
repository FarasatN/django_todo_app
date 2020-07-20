from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import First_app

# Create your views here.
def index(request):
	todos = First_app.objects.all()
	return render(request,'index.html',{'todos':todos})

def addTodo(request):
	if request.method == "GET":
		return redirect('/')
	else:
		title = request.POST.get('title')
		newTodo = First_app(title=title,completed=False)
		newTodo.save()
		return redirect('/')

def update(request,id):
	# todo = First_app.objects.filter(id=id).first()
	todo = get_object_or_404(First_app,id=id)
	todo.completed = not todo.completed
	todo.save()
	return redirect('/')

def delete(request,id):
	# todo = First_app.objects.filter(id=id).first()
	todo = get_object_or_404(First_app,id=id)
	todo.delete()
	return redirect('/')
