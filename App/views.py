from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
)
from App.models import (
	DataM
)

class Datainsertion(CreateAPIView):
    """
    Model POST API
        Service Usage and Description : This API is used to create a theme.
        Authentication Required : YES
        Data : {
            
        }
    """

    serializer_class = DataSerializer
    queryset = DataM.objects.all()

    def post(self, request):
        data = request.data
        serializer = ThemeSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save(brandid=brand_id,isEditable=True)
                brandqs = Brand.objects.filter(id=brand_id)[0]
                brandqs.theme = instance
                brandqs.save()
                return Response(data={"themeid":instance.id}, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)                
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)                
