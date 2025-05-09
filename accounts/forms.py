from django import forms
from django.db import models


class StyledForm(forms.Form):
    template_name = "accounts/form_snippet.html"

    def __init__(self, *args, **kwargs):
        super(StyledForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            css = visible.field.widget.attrs.get("class", "")
            css += " rounded-md w-full px-2 py-1"
            visible.field.widget.attrs["class"] = css


class UserCreateForm(StyledForm):
    first_name = forms.CharField(
        label="First Name", max_length=65, min_length=2, required=True
    )
    last_name = forms.CharField(
        label="Last Name", max_length=65, min_length=1, required=True
    )
    email = forms.EmailField(required=True)

    subjects = forms.CharField(
        required=True,
        help_text=(
            "What subjects do you require help with? Please include whether this is for the International Baccalaureate (IB) or GCSE level."
            " Please also include any Universities and Courses you're currently targeting."
        ),
        max_length=3000,
        widget=forms.Textarea,
    )
