from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Order, Product
from core.serializers.orders import (OrderCreateSerializer,
                                     OrderReadSerializer,
                                     OrderStatusSerializer,
                                     OrderUpdateItemsSerializer)


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Order.objects.select_related('product').all()

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        return OrderReadSerializer

    @swagger_auto_schema(
        method='patch',
        request_body=OrderStatusSerializer,
        responses={200: OrderReadSerializer},
        operation_summary="Изменить статус заказа"
    )
    @action(detail=True, methods=['patch'])
    def set_status(self, request, pk=None):
        order = self.get_object()

        serializer = OrderStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order.status = serializer.validated_data["status"]
        order.save()

        return Response(OrderReadSerializer(order).data)

    @swagger_auto_schema(
        method='patch',
        request_body=OrderUpdateItemsSerializer,
        responses={200: OrderReadSerializer},
        operation_summary="Обновить товар и количество (только в статусе new)"
    )
    @action(detail=True, methods=['patch'])
    def update_items(self, request, pk=None):
        order = self.get_object()

        if order.status != Order.STATUS_NEW:
            return Response(
                {"error": "Редактировать можно только заказ в статусе 'new'"},
                status=400
            )

        serializer = OrderUpdateItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if "product" in data:
            try:
                product = Product.objects.get(id=data["product"])
            except Product.DoesNotExist:
                return Response({"error": "Товар не найден"}, status=404)
            order.product = product

        if "quantity" in data:
            order.quantity = data["quantity"]

        order.save()
        return Response(OrderReadSerializer(order).data)
