from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
)
from App.models import (
	DataM
)
import pandas as pd
import joblib
import json
from .serializers import DataSerializer
#api creation
class Datainsertion(CreateAPIView):
    """
    Model POST API
        Service Usage and Description : This API is used to predict.
        Authentication Required : NO
        Data : 
        {
            "education":"unknown",
            "marital_education":"married-unknown",
            "default":"no",
            "job":"services",
            "targeted":"no",
            "marital":"married",
            "housing":"yes",
            "month":"may"
        }
    """

    serializer_class = DataSerializer
    queryset = DataM.objects.all()

    def post(self, request):
        data = request.data
        df_data=pd.DataFrame.from_records([data])
        reg=joblib.load("prediction/DTmodel.pkl")
        loan_pred = reg.predict(df_data)
        if loan_pred.round() == 0:
            data["loan"]="no"
        elif loan_pred.round() == 1:
            data["loan"]="yes"
        serializer = DataSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                obj = DataM.objects.all()
                if obj.count() != 0:
                    obj[0].delete()
                instance = serializer.save(loan = data["loan"])
                return Response(data=instance,status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)                
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)                
