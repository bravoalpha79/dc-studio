from mindfulness_studio.models import MindfulnessStudio


def nav_pages(request):
    return {
        "mindfulness_studio": MindfulnessStudio.objects.visible().first()
    }
