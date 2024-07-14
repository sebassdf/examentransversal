


class Cart:
    def __init__(self, request):
        self.request=request 
        self.session=request.session
        cart= self.session.get("cart") #cada sesion tiene su cart

        if not cart:                                              #si la sesion no tiene cart entonces crea uno en forma de diccionario
            cart= self.session["cart"]= {}
                                                        # si la sesion tiene entonces lo usa
        self.cart= cart


    def agregar(self,producto): 
        if(str(producto.id) not in self.cart.keys()):                 #si el producto (id) no esta en el carrito agregalo
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }                                                         # entonces agrega todo esto
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"]= value["cantidad"]+1
                    value["precio"]= float(value["precio"])+ producto.precio
                    
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["cart"]= self.cart
        self.session.modified=True

    def eliminar_carrito(self, producto):
        producto.id= str(producto.id)
        if producto.id in self.cart:
            del self.cart[producto.id]
            self.guardar_carro()

            

    def restar_producto(self, producto):
        for key, value in self.cart.items():
                if key== str(producto.id):
                    value["cantidad"]= value["cantidad"]-1
                    value["precio"]= float(value["precio"])- producto.precio
                    if value["cantidad"] < 1:
                        self.eliminar_carrito(producto)
                    break
                
        self.guardar_carro()

    def limpiar_carrito(self):
        self.session["cart"] = {}
        self.session.modified=True