from django.shortcuts import render, redirect

from todo_app.forms import TodoForm
from todo_app.models import TodoModel


def add_subject(request):
    forms=TodoForm()
    print("forms")
    if request.method == 'POST':
        form1 = TodoForm(request.POST)
        print("form1")
        if form1.is_valid():
            form1.save()

    return render(request, 'add_subject.html',{'forms':forms})

def content_view(request):
    data=TodoModel.objects.all()
    print(data)
    return render(request, 'content_view.html',{'data':data})

def delete_data(request,id):
    data=TodoModel.objects.get(id=id)
    data.delete()
    return redirect("content_view")


def update_data(request,id):
    data=TodoModel.objects.get(id=id)
    form=TodoForm(instance=data)
    if request.method == 'POST':
        form=TodoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('content_view')
    return render(request, 'update.html', { 'forms': form})


def index(request):
    return render(request, "index.html")
def dashboard1(request):
    return render(request, "dashboard1.html")


