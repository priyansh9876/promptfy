from django import forms
from .models import Prompt


class PromptSubmissionForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = [
            'category',
            'title',
            'description',
            'prompt_text',
            'tags',
        ]

        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl bg-slate-900 border border-white/10 text-white outline-none'
            }),

            'title': forms.TextInput(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl bg-slate-900 border border-white/10 text-white placeholder-slate-400 outline-none',
                'placeholder': 'Enter prompt title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl bg-slate-900 border border-white/10 text-white placeholder-slate-400 outline-none',
                'rows': 4,
                'placeholder': 'Short description'
            }),

            'prompt_text': forms.Textarea(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl bg-slate-900 border border-white/10 text-white placeholder-slate-400 outline-none',
                'rows': 8,
                'placeholder': 'Paste your AI prompt here'
            }),

            'tags': forms.TextInput(attrs={
                'class': 'w-full px-5 py-4 rounded-2xl bg-slate-900 border border-white/10 text-white placeholder-slate-400 outline-none',
                'placeholder': 'marketing, instagram, growth'
            }),
        }