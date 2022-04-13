from products.models import Product

def validate_publisher(product_id, publisher_id):
    product = Product.objects.select_related('publisher').get(pk=product_id)
    
    if product.publisher.id != publisher_id:
        return False
    return True
