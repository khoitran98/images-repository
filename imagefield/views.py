from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImagefieldForm
from .forms import SearchForm, CreateUserForm
from .models import ImagesModel
from PIL import Image
import imagehash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.forms import modelformset_factory

def success(request): 
    return HttpResponse('successfully uploaded') 

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}
	return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/uploadimage')
		else:
			messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home_view(request):
    context = {}
    if request.method == "POST": 
        form = ImagefieldForm(request.POST, request.FILES)
        hash = 0 
        if form.is_valid(): 
            for filename in request.FILES:
                im = Image.open(request.FILES[filename])
                hash = imagehash.phash(im)
            name = form.cleaned_data.get("name") 
            img = form.cleaned_data.get("image_field") 
            obj = ImagesModel.objects.create( 
                                 title = name,  
                                 img = img, 
                                 hash = int(str(hash), 16),
                                 user = request.user
                                 ) 
            uploaded = obj.save()
            messages.success(request, 'Your image is uploaded!') 
            return redirect('/uploadimage')
    else: 
        yourimages = ImagesModel.objects.raw('SELECT * FROM images WHERE user_id = %s', [request.user.id]) 
        form = ImagefieldForm()
        context['form'] = form
        context['images'] = yourimages
        return render( request, "fileupload.html", context) 

@login_required(login_url='login')
def search_view(request):
    context = {}
    if request.method == "POST": 
        phash = 0
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid(): 
            for filename in request.FILES:
                im = Image.open(request.FILES[filename])
                phash = imagehash.phash(im)
                phash = int(str(phash), 16)
            allimages = ImagesModel.objects.raw('SELECT * FROM images WHERE BIT_COUNT(%s ^ hash) < 5', [phash])
            search = SearchForm()
            context['search'] = search
            context['images'] = allimages
            print(allimages)
            return render(request, "search.html", context)
    else: 
        search = SearchForm()
        context['search'] = search
        return render(request, "search.html", context)
