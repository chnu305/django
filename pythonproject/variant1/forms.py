from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from variant1.models import Accounts, Files

class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Save account'))


class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Save file'))