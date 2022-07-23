from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import MaterialForm
from .models import Material
from .minioUpload import minioUpload


def material_list(request):
    materials = Material.objects.all().order_by('-created_on')
    return render(request, 'upload/material_list.html', {
        'materials': materials
    })

def upload_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            x = "C:\\Users\\Asus\\django_projects\\miniFacebook\\media\\materials" + "\\" +str(form.cleaned_data.get('pdf'))
            print(x)
            minioUpload(x, str(form.cleaned_data.get('pdf')))
            return redirect('/story/')
    else:
        form = MaterialForm()
    return render(request, 'upload/upload_material.html', {
        'form': form
    })
