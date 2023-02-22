from django import forms

gender=(('male','male'),('female','female'),('others','others'))
course=(('python','python'),('java','java'),('mern','mern'),('AWS','AWS'))

class jsprider(forms.Form):
    name=forms.CharField(max_length=50)
    yop=forms.IntegerField()
    gender=forms.ChoiceField(choices=gender,widget=forms.RadioSelect)
    course=forms.ChoiceField(choices=course)
    