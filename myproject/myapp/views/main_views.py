from rest_framework import status
from rest_framework.response import     Response
from rest_framework.decorators import api_view
from ..serializers import EmployeeSerializer
from ..models import Employee

@api_view(['POST'])
def add_employee(request):
    if request.method =='POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee inserted successfully','data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'Failed to insert data'}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def get_employee(request):
    if request.method =='GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
    

@api_view(['PUT'])
def update_employee(request, id ):
    try:
        employee = Employee.objects.get(id=id)
    except employee.DoesNotExist:
        return Response({'message':"employee not found"})
    if request.method =='PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"employee update successfully", 'data':serializer.data}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'msg':"failed to update student data"},status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def get_employee_by_id(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
       return Response({'errors':"employee not found"},status=status.HTTP_400_BAD_REQUEST)
    seralizer = EmployeeSerializer(employee)
    return  Response({'data': seralizer.data},status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        
    except Employee.DoesNotExist:
        return Response({'msg': "employee not found"})
    
    employee.delete()
    return Response({'msg':'employee delete successfully'},status=status.HTTP_204_NO_CONTENT)
