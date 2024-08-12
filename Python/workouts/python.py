from .models import YourModel
def data(request):
    if request.method ==  'POST':
        name = request.POST('name')
        data = YourModel(name = name)
        data.save()

def data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        data = YourModel.objects.get(name = name)
        return render(request, 'your_template.html', {'data': data})

def data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        data = mymodels(name = name)
        data()


name = reques.POST.get(name)
ko = use(nae = NameError)