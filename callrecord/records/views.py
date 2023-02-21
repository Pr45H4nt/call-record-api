from rest_framework.response import Response
from rest_framework import generics
from .serializers import CallrecordSerializer
from .models import CallRecord
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class InitiateCallView(generics.CreateAPIView):
    '''
    A view for creating CallRecord Instances
    '''
    queryset = CallRecord.objects.all()
    serializer_class = CallrecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'success': True})



class CallReportPagination(PageNumberPagination):
    page_size = 10
    
class CallReportView(generics.ListAPIView):
    '''
    A view for listing callrecords from the database

    The view supports a 'phone' query parameter, which can be used to filter
    the call records by caller or receiver phone number.

    Returns a paginated list of call records.
    '''
    serializer_class = CallrecordSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        '''returns a filtered queryset according to given parameter 'phone' '''
        phone = self.request.query_params.get('phone')
        return CallRecord.objects.filter(from_number=phone) | CallRecord.objects.filter(to_number=phone)


class Call_Update_DeleteView(generics.RetrieveUpdateDestroyAPIView):
    '''
    A view for reading, updating and deleting the instance 
    gets the object according to the given 'id'
    '''

    queryset = CallRecord.objects.all()
    serializer_class = CallrecordSerializer
    lookup_field = 'id'
