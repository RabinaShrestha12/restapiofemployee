from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..serializers import EmployeeSerializer,CategorySerializer, ProductSerializer
from ..models import Employee, Category, Product
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
    

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def product_view(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # kun user la added gara ko vanara dhaki dinxa yo code ma request user pass gara ko thau ma 
            return Response({'message':"Product addes successfully", 'product':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'msg':'Failed to add product', 'err': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'msg':'Product doesnot exists', 'err':e})
        

@api_view(['PUT','GET','DELETE'])
def product_by_id(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'msg':"product doenot exist"})
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"product updated sucessfully"},status=status.HTTP_200_OK)
        else:
            return Response({'msg':"product doesnot updated", 'err':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method =='DELETE':
        product.delete()
        return Response({'msg':'product delete successfully'},status=status.HTTP_200_OK)

    elif request.method =='GET':
        serializer = ProductSerializer(product)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        
    else:
        return Response({'err':'failed to fetch the data'})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_list(request,category_id):
    if request.method == 'GET':
        product = Product.objects.filter(category=category_id)
        serializer = ProductSerializer(product, many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    else:
        return Response({'error':"Faled to fetch category"}, status=status.HTTP_400_BAD_REQUEST)


    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_with_products(request):
    categories = Category.objects.all()
    data = []

    for category in categories:
        products = Product.objects.filter(category=category.id)
        if products.exists():
            category_data = CategorySerializer(category).data
            product_data = ProductSerializer(products, many=True).data
            category_data['products'] = product_data
            data.append(category_data)

    return Response({'data': data}, status=status.HTTP_200_OK)
