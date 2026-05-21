from django.db import migrations

def seed_data(apps, schema_editor):
    Category = apps.get_model('prompts', 'Category')
    Prompt = apps.get_model('prompts', 'Prompt')

    coding, _ = Category.objects.get_or_create(name='Coding', slug='coding')
    study, _ = Category.objects.get_or_create(name='Study', slug='study')
    ai, _ = Category.objects.get_or_create(name='AI Tools', slug='ai-tools')

    prompts = [
        {
            "category": coding,
            "title": "Senior Python Code Reviewer",
            "slug": "senior-python-code-reviewer",
            "description": "Get production-grade code review feedback.",
            "prompt_text": "Act as a senior Python engineer. Review my code for bugs, security flaws, performance bottlenecks, architecture issues, and readability improvements.",
            "tags": "python,coding,review",
        },
        {
            "category": study,
            "title": "Exam Study Planner",
            "slug": "exam-study-planner",
            "description": "Build an optimized study timetable.",
            "prompt_text": "Act as an academic productivity coach. Build a realistic study plan for my exam.",
            "tags": "study,exam,productivity",
        },
        {
            "category": ai,
            "title": "Startup Idea Validator",
            "slug": "startup-idea-validator",
            "description": "Validate startup ideas with AI.",
            "prompt_text": "Act as a startup strategist and validate my business idea.",
            "tags": "startup,business,ai",
        },
    ]

    for p in prompts:
        Prompt.objects.get_or_create(
            slug=p["slug"],
            defaults={
                **p,
                "approved": True,
                "upvotes": 10,
                "views": 100,
            }
        )

class Migration(migrations.Migration):

    dependencies = [
        ('prompts', '0002_prompt_favorited_by_prompt_submitted_by'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]