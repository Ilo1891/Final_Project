from django import forms

from common.view import StyleFormMixin
from reservation.models import Table, Reservation
from users.models import User


class TableForms(StyleFormMixin, forms.ModelForm):
    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        if request is not None:
            self.fields['recipients'].queryset = User.objects.filter(owner=request.user)
            self.fields['table'].queryset = Table.objects.filter(owner=request.user)

    class Meta:
        model = Table
        fields = ('table', 'seats', 'image')

class ReservationForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name',
                  'table',
                  'email', 'phone', 'time_reserved',
                  'date_reserved']


class ReservationUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['first_name',
                  'email', 'time_reserved',
                  'date_reserved']