from django.http import JsonResponse


def hola_mundo(request):
    return JsonResponse({
        "mensaje": "Hola Mundo desde la API REST",
        "framework": "Django",
        "estado": "ok",
    })