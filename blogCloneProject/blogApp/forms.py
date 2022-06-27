from blogApp.models import Post,Comment


class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields = ('author','title','text')
        widgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}) ,
            'text':forms.TextArea(attrs = {'class':'editable medium-editer-textarea postcontent'}) ,
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment

        widgets = {
            'author':forms.TextInput(attrs = {'class':'textinputclass'}) ,
            'text':forms.TextArea(attrs = {'class':'editable medium-editer-textarea'}) ,  
        }
