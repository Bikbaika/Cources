from django import forms  

COURSE_QUANTITY_CHOISES = [(i, str(i)) for i in range(1,10)]

class CartAddCourseForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=COURSE_QUANTITY_CHOISES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)