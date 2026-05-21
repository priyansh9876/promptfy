from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Prompt, Category
from .forms import PromptSubmissionForm


def prompt_list(request):
    prompts = Prompt.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'prompts/prompt_list.html', {'prompts': prompts})


def trending_prompts(request):
    prompts = Prompt.objects.filter(approved=True).order_by('-upvotes')
    return render(request, 'prompts/prompt_list.html', {'prompts': prompts})


def category_prompts(request, slug):
    category = get_object_or_404(Category, slug=slug)

    prompts = Prompt.objects.filter(
        approved=True,
        category=category
    )

    return render(request, 'prompts/prompt_list.html', {
        'prompts': prompts,
        'category': category
    })


def search_prompts(request):
    query = request.GET.get('q', '').strip()

    prompts = Prompt.objects.filter(approved=True)

    if query:
        prompts = prompts.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        )

    prompts = prompts.order_by('-upvotes')

    return render(request, 'prompts/prompt_list.html', {
        'prompts': prompts,
        'query': query
    })


@login_required
def submit_prompt(request):
    if request.method == 'POST':
        form = PromptSubmissionForm(request.POST)

        if form.is_valid():
            prompt = form.save(commit=False)
            prompt.approved = False
            prompt.submitted_by = request.user
            prompt.save()

            return render(request, 'prompts/submit_success.html')

    else:
        form = PromptSubmissionForm()

    return render(request, 'prompts/submit_prompt.html', {
        'form': form
    })


def upvote_prompt(request, slug):
    prompt = get_object_or_404(
        Prompt,
        slug=slug,
        approved=True
    )

    voted_prompts = request.session.get('voted_prompts', [])

    if prompt.pk not in voted_prompts:
        prompt.upvotes += 1
        prompt.save()

        voted_prompts.append(prompt.pk)
        request.session['voted_prompts'] = voted_prompts

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def toggle_favorite(request, slug):
    prompt = get_object_or_404(
        Prompt,
        slug=slug,
        approved=True
    )

    if request.user in prompt.favorited_by.all():
        prompt.favorited_by.remove(request.user)
    else:
        prompt.favorited_by.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


def prompt_detail(request, slug):
    prompt = get_object_or_404(
        Prompt,
        slug=slug,
        approved=True
    )

    viewed_prompts = request.session.get('viewed_prompts', [])

    if prompt.pk not in viewed_prompts:
        prompt.views += 1
        prompt.save()

        viewed_prompts.append(prompt.pk)
        request.session['viewed_prompts'] = viewed_prompts

    is_favorited = False

    if request.user.is_authenticated:
        is_favorited = request.user in prompt.favorited_by.all()

    return render(request, 'prompts/prompt_detail.html', {
        'prompt': prompt,
        'is_favorited': is_favorited
    })