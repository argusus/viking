from django.shortcuts import render, redirect
from .models import ServicesAndPrice
from .forms import QuestionForm, OrderServicesForm
from django.views.generic import DetailView


def index(request):
    service = ServicesAndPrice.objects.order_by('id')[:9]
    data = {}
    if ServicesAndPrice.objects.count() != 0:
        min_price = ServicesAndPrice.objects.order_by('price')[0]
        max_price = ServicesAndPrice.objects.order_by('-price')[0]
        data.update({
            'min_price': min_price,
            'max_price': max_price,
        })

    data.update({
        'service': service,
    })
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def services(request):
    service = ServicesAndPrice.objects.order_by('id')
    return render(request, 'main/services.html', {'service': service})


class ServiceDetailView(DetailView):
    model = ServicesAndPrice
    template_name = 'main/detail.html'
    context_object_name = 'detail'


def order(request):
    error = ''
    if request.method == 'POST':
        form = OrderServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form error'

    form = OrderServicesForm()
    service = ServicesAndPrice.objects.order_by('id')[:9]

    data = {
        'form': form,
        'error': error,
        'service': service,
    }

    return render(request, 'main/order.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form error'

    form = QuestionForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)
