from django.db import models
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# MODELOS

class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )

    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )

    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name


class Cruise(models.Model):  
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    destinations = models.ManyToManyField(
        Destination,
        related_name='destinations'
    )

    def __str__(self) -> str:
        return self.name


class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField()
    notes = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.PROTECT
    )

# FORMULARIOS

class InfoRequestForm(forms.ModelForm):
    class Meta:
        model = InfoRequest
        fields = ['name', 'email', 'cruise', 'notes']

    def __init__(self, *args, **kwargs):
        super(InfoRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'slug']

    def __init__(self, *args, **kwargs):
        super(DestinationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Destination'))


class CruiseForm(forms.ModelForm):
    class Meta:
        model = Cruise
        fields = ['name', 'description', 'destinations']

    def __init__(self, *args, **kwargs):
        super(CruiseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Cruise'))