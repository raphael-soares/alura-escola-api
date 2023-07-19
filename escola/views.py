from django.http import JsonResponse
from escola.serializer import AlunoSerializer


# Create your views here.


def alunos(request):
    if request.method == "GET":
        aluno = AlunoSerializer.
        return JsonResponse(aluno)

    
