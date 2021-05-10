from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImagefieldForm
from .models import ImagefieldModel 
from .models import GetImage 
# Create your views here.
  
# Create your views here. 
def home_view(request): 
    context = {}
    if request.method == "POST": 
        form = ImagefieldForm(request.POST, request.FILES) 
        if form.is_valid(): 
            name = form.cleaned_data.get("name") 
            img = form.cleaned_data.get("image_field") 
            obj = ImagefieldModel.objects.create( 
                                 title = name,  
                                 img = img 
                                 ) 
            obj.save() 
            print(obj)
            return redirect('success') 
    else: 
        form = ImagefieldForm()
        context['form'] = form
        return render( request, "fileupload.html", context) 

def success(request): 
    return HttpResponse('successfully uploaded') 
