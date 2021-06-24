from .models import Questions, OrderServices, ServicesAndPrice
from django.forms import ModelForm, TextInput, Textarea, Select
from django.utils.translation import ugettext_lazy as _


class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['tel', 'name', 'text_questions']

        widgets = {
            'tel': TextInput(
                attrs={
                    'class': 'CreateTask',
                    'placeholder': _("Номер телефону"),
                    'type': 'tel',
                    'pattern': "[+38]{0,3}[0-9]{3}[0-9]{3}[0-9]{2}[0-9]{2}",
                }
            ),
            'name': TextInput(
                attrs={
                    'type': 'text',
                    'placeholder': _("Ім'я"),
                    'class': "CreateTask",
                }
            ),
            'text_questions': Textarea(
                attrs={
                    'placeholder': _("Питання"),
                    'class': "CreateTaskText",
                }
            ),
        }


class OrderServicesForm(ModelForm):
    class Meta:
        model = OrderServices
        fields = ['tel_service', 'name_service', 'choice_service', 'text_service']

        cho = set()
        cho.add(('------', '---------'))
        c = 1
        for j in ServicesAndPrice.objects.all():
            j = str(j)
            cho.add((j, j))

        widgets = {
            'tel_service': TextInput(
                attrs={
                    'class': 'CreateTask',
                    'placeholder': _("Номер телефону"),
                    'type': 'tel',
                    'pattern': "[+38]{0,3}[0-9]{3}[0-9]{3}[0-9]{2}[0-9]{2}",
                }
            ),
            'name_service': TextInput(
                attrs={
                    'class': "CreateTask",
                    'type': 'text',
                    'placeholder': _("Ім'я"),
                }
            ),
            'choice_service': Select(
                attrs={
                    'class': 'CreateTask select',
                },
                choices=sorted(cho)
            ),
            'text_service': Textarea(
                attrs={
                    'class': 'CreateTaskText',
                    'placeholder': _('Примітки до замовлення')
                }
            ),
        }
