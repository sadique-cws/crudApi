from rest_framework.generics import GenericAPIView
from .serializers import VcardSerializer
from .models import Vcard
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

class VcardList(APIView):
    vcard = Vcard.objects.all()
    serializer = VcardSerializer(vcard,many=True)
    
    def get(self,req,id=None):
        return Response(self.serializer.data, status=200)
   

    def post(self, req):
        data = {
            "name":req.POST.get("name"),
            "contact" : req.POST.get("contact")
        }
        serializer = VcardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
    


class VcardDetails(generics.GenericAPIView):
    serializer_class = VcardSerializer

    def get(self, req, id=None):
        singleVcard = Vcard.objects.get(id=id)
        serializer = VcardSerializer(singleVcard)
        return Response(serializer.data,status=200)
    
    def delete(self,req,id=None):
        singleVcard = Vcard.objects.get(id=id)
        singleVcard.delete()
        return Response(status=200)

    def patch(self, req, id=None):
        singleVcard = Vcard.objects.get(id=id)
        serializer = VcardSerializer(singleVcard, data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response({"msg":"record not updated","error":serializer.errors})
        

        