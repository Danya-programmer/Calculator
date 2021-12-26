from django.shortcuts import render
from .forms import NameForm
from .logiс import decision


def main(request):
    form = NameForm(request.POST)
    f = str(form)
    f1 = f.split('value="')
    clear_task = f1[-1].split('"')[0]

    return render(request, 'calculator/main.html', {'form': form, 'answer': decision(clear_task)})

# Create your views here.
