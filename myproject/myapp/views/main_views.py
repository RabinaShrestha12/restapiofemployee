from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..serializers import EmployeeSerializer,CategorySerializer
from ..models import Employee, Category
from rest_framework.permissions import AllowAny, IsAuthenticated

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


#for category
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def category_view(request):
    if request.method =='POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"category is added successfully"},status=status.HTTP_200_OK)
        else:
            return Response({'msg':"failed to update category", 'err':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    if request.method =='GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['PUT','DELETE','GET'])
def category_by_id(request, id):
    try:
        category = Category.objects.get(id=id)
    except category.DoesNotExist:
        return Response({'msg':"category not found"})
    
    if request.method =='PUT':
        seralizer = CategorySerializer(category, data=request.data, partial=True)
        if seralizer.is_valid():
            seralizer.save()
            return Response({'msg':"category updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({'msg':"failed to updated category data", 'err':seralizer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method =='DELETE':
        category.delete()
        return Response({'msg': 'category delete successfully'}, status=status.HTTP_200_OK)
    
    elif request.method == 'GET':
        seralizer = CategorySerializer(category)
        return Response({'data':seralizer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'err': "failed to fetch category"})
    
