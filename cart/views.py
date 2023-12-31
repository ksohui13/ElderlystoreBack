import json
from json.decoder           import JSONDecodeError
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import MultipleObjectsReturned
from django.db              import transaction
from cart.models            import Cart, Option
from products.models        import Product
from accounts.utils         import login_decorator
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CartSerializer, OtionSerializer

#router
class CartViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 
    #permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    #authentication_classes = [JWTAuthentication]
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class OptionViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

    queryset = Option.objects.all()
    serializer_class = OtionSerializer

#View
class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            product_id = data['product_id'] #확인중
            option_id  = data['option_id']
            quantity   = data['quantity']
            
            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({'message':'PRODUCT_NOT_EXIST'}, status=400)
            
            if not Option.objects.filter(id=option_id).exists():
                return JsonResponse({'message':'OPTION_NOT_EXIST'}, status=400)
                
            if quantity <= 0:
                return JsonResponse({'message':'QUANTITY_ERROR'}, status=400)
            
            cart, is_created = Cart.objects.get_or_create(
                user       = user,
                product_id = product_id,
                option_id  = option_id
            )
            cart.quantity += quantity
            cart.save()   
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except Cart.DoesNotExist:
            return JsonResponse({'message':'INVALID_CART'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
    
    @login_decorator
    def get(self, request):
        user = request.user

        if not Cart.objects.filter(user=user).exists():
            return JsonResponse({'message':'USER_CART_NOT_EXIST'}, status=400)

        carts  = Cart.objects.filter(user=user)
        result = [{
            'cart_id'    : cart.id,
            'product_name'       : cart.product.product_name,
            # 'option_name'     : cart.option.option_name,
            'quantity'   : cart.quantity,
            'price_origin'   : cart.product.price_origin,
            'price_sale'      : cart.product.price_sale,
            # 'image'      : cart.product.productimage_set.get(is_thumbnail=True).image_url
            } for cart in carts]
        return JsonResponse({'result':result}, status=200)
    
    @transaction.atomic
    @login_decorator
    def patch(self, request):
        try:
            data     = json.loads(request.body)
            user     = request.user
            cart_id  = request.GET.get('id')
            quantity = data['quantity']

            if not Cart.objects.filter(id=cart_id, user=user).exists():
                return JsonResponse({'message':'INVALID_CART_ID'}, status=404)

            if quantity <= 0:
                return JsonResponse({'message':'QUANTITY_ERROR'}, status=400)

            cart = Cart.objects.get(id=cart_id, user=user)

            cart.quantity = data['quantity']
            cart.save()
            return JsonResponse({'quantity': cart.quantity}, status=200)

        except MultipleObjectsReturned:
            return JsonResponse({'message':'MULTIPLE_OBJECTS_RETURNED'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

    @login_decorator
    def delete(self, request):
        try:
            user    = request.user
            cart_id = request.GET.get('id')

            if not Cart.objects.filter(id=cart_id, user=user).exists():
                return JsonResponse({'message':'INVALID_CART_ID'}, status=404)

            cart = Cart.objects.get(id=cart_id, user=user)
            
            cart.delete()
            return JsonResponse({'message': 'DELETED'}, status=200)
    
        except MultipleObjectsReturned:
            return JsonResponse({'message':'MULTIPLE_OBJECTS_RETURNED'}, status=400)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)