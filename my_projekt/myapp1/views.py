from django.shortcuts import render
from myapp1.models import Worker

def index_page(request):
    
    

    all_workers = Worker.objects.all()
    print(all_workers)
    Worker_filtered = Worker.objects.filter(salary=60000)
    print(Worker_filtered)

    for i in all_workers:
        print(f"№{i.id}) Имя сотрудника: {i.name}, Фамилия: {i.second_name}, Зарплата: {i.salary}")
    return render(request,'index.html')