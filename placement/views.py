from django.shortcuts import render
from rest_framework import mixins, viewsets, permissions
from . import models, serializer

class PlacementApplicationView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.PlacementApplicationModel.objects.all()
    serializer_class = serializer.PlacementApplicationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ApplicationTrackingView(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = serializer.PlacementApplicationSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        student_id = self.request.query_params.get('studentApplication')
        comp_id = self.request.query_params.get('companyApplication')

        if student_id:
            return models.PlacementApplicationModel.objects.select_related('companyId').filter(studentId=student_id).all()
        if comp_id:
            return models.PlacementApplicationModel.objects.filter(companyId=comp_id).all()
        
        return models.PlacementApplicationModel.objects.all()