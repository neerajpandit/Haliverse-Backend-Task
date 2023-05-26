from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer
from datetime import datetime
# from rest_framework.views import APIView

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Quiz created successfully'}, status=201)

    @action(detail=False, methods=['get'])
    def active(self, request):
        current_time = datetime.now()
        try:
            quiz = Quiz.objects.get(start_date__lte=current_time, end_date__gte=current_time)
            serializer = self.get_serializer(quiz)
            return Response(serializer.data)
        except Quiz.DoesNotExist:
            return Response({'message': 'No active quiz found'}, status=404)

    @action(detail=True, methods=['get'])
    def result(self, request, pk=None):
        id=pk
        if id is not None:
            quiz = self.get_object(id=id)
            if quiz.status == 'finished':
                return Response({'result': quiz.right_answer})
        try:
            quiz = self.get_object()
            if quiz.status == 'finished':
                return Response({'result': quiz.right_answer})
            else:
                return Response({'message': 'Quiz is still active'}, status=400)
        except Quiz.DoesNotExist:
            return Response({'message': 'Quiz not found'}, status=404)

    @action(detail=False, methods=['get'])
    def all(self, request):
        quizzes = Quiz.objects.all()
        serializer = self.get_serializer(quizzes, many=True)
        return Response(serializer.data)




# class QuizViewall(APIView):
    # queryset = Quiz.objects.all() 
    # serializer_class = QuizSerializer

    # def post(self,request,default=None):
    #     serializer=QuizSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #         # return Response({'msg':'Success'})
    #     return Response({'msg':'SOmthing Wrong'})

    # def get(self, request,*args,**kwargs):
    #     quizzes = Quiz.objects.all()
    #     serializer = QuizSerializer(quizzes, many=True)
    #     return Response(serializer.data)