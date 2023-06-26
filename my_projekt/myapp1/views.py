from django.shortcuts import render
from myapp1.models import Worker

def index_page(request):
    
    my_dict = {"data":"приветик","data2":"как дела?"}

    all_workers = Worker.objects.all()
   
    return render(request,'index.html',{"data":all_workers})