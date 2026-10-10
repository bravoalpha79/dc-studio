from expert_education.models import ExpertEducation
from mindfulness_studio.models import MindfulnessStudio


def nav_pages(request):
    return {
        "mindfulness_studio": MindfulnessStudio.objects.visible().first(),
        "expert_educations": list(ExpertEducation.objects.visible())
    }
