
from rest_framework import viewsets
from .models import Plato
from .serializers import PlatoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def cuenta_total(request):
    precios = request.data.get('precios', [])

    if not isinstance(precios, list):
        return Response({'error': 'Debe ser un numero'}, status=400)

    total = 0
    for precio in precios:
        if not isinstance(precio, (int, float)):
            return Response({'error': 'los elementos son numeros.'}, status=400)
        total += precio

    # Determinar mensaje
    if total < 20:
        mensaje = 'Cuenta pequeña'
    elif 20 <= total <= 60:
        mensaje = 'Cuenta media'
    else:
        mensaje = 'Cuenta alta'

    return Response({'total': total, 'mensaje': mensaje})



@api_view(['POST'])
def aplicar_descuento(request):
    total = request.data.get('total')
    porcentaje = request.data.get('porcentaje')

    if total is None or porcentaje is None:
        return Response({'error': 'total y porcentaje.'}, status=400)

    if not isinstance(total, (int, float)) or not isinstance(porcentaje, (int, float)):
        return Response({'error': 'total y porcentaje es un numero'}, status=400)

    if porcentaje < 0 or porcentaje > 100:
        return Response({'error': 'va de 0 a 100'}, status=400)

    # Cálculos
    monto_descuento = total * (porcentaje / 100)
    total_con_descuento = total - monto_descuento

    return Response({
        'total': total,
        'porcentaje': porcentaje,
        'totalConDescuento': round(total_con_descuento, 2)
    })



