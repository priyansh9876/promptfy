from django.shortcuts import render
from prompts.models import Prompt, Category
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from prompts.models import Prompt


def home(request):
    trending_prompts = Prompt.objects.filter(
        approved=True
    ).order_by('-upvotes')[:6]

    latest_prompts = Prompt.objects.filter(
        approved=True
    ).order_by('-created_at')[:6]

    categories = Category.objects.all()
    
    total_prompts = Prompt.objects.filter(approved=True).count()
    total_categories = Category.objects.count()

    total_views = Prompt.objects.filter(
        approved=True
    ).aggregate(Sum('views'))['views__sum'] or 0

    context = {
        'trending_prompts': trending_prompts,
        'latest_prompts': latest_prompts,
        'categories': categories,
        'total_prompts': total_prompts,
        'total_categories': total_categories,
        'total_views': total_views,
    }

    return render(request, 'core/home.html', context)

@login_required
def dashboard(request):
    saved_prompts = request.user.favorite_prompts.filter(
        approved=True
    ).order_by('-created_at')

    submitted_prompts = request.user.submitted_prompts.order_by('-created_at')

    return render(request, 'core/dashboard.html', {
        'saved_prompts': saved_prompts,
        'submitted_prompts': submitted_prompts,
    })