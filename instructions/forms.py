from django import forms
from .models import Instruction
from crispy_forms.helper import FormHelper


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "blueForms"
