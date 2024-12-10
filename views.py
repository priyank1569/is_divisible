from django.shortcuts import render
my_dict={"data":[10,11,12,13,14,15]}
def first_app(request):
    return render(request,"1.html",context=my_dict)

# Create your views here.
