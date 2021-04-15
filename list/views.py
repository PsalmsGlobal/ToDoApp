from django.shortcuts import render, redirect
from .models import MyList
from .forms import MyListForm
from django.contrib import messages
from django.http import HttpResponseRedirect




def home(request):

	if request.method == 'POST':
		form = MyListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = MyList.objects.all
			messages.success(request, ('Item Has Been Added To List!!'))
			return render(request, 'home.html', {'all_items': all_items})

	else:
		all_items = MyList.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def about(request):
	context = {'first_name': 'Nhicoulous', 'last_name': 'Horford'}
	return render(request, 'about.html', context)

def delete(request, List_id):
	item = MyList.objects.get(pk=List_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted'))
	return redirect('home')

def cross_off(request, List_id):
	item = MyList.objects.get(pk=List_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, List_id):
	item = MyList.objects.get(pk=List_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request, List_id):
	if request.method == 'POST':
		item = MyList.objects.get(pk=List_id)

		form = MyListForm(request.POST or None, instance= item)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item Has Been Edited!'))
			return redirect('home')

	else:
		item = MyList.objects.get(pk=List_id)
		return render(request, 'edit.html', {'item': item})

def back(request):
	return render(request, 'home.html')