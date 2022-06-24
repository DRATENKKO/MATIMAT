class Carro:
    def __init__(self, request): #peticion 
        self.request = request # 
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        
        self.carro = carro

    def agregar(self, producto):
        if(str(producto.idProducto) not in self.carro.keys()):
            self.carro[producto.idProducto]={
                "producto_id": producto.idProducto,
                "nombre" : producto.nombre,
                "precio": producto.precio,
                "cantidad": 1
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=value["precio"]+producto.precio
                    break
        self.guardar_carro()
        
        
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.idProducto)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=value["precio"]-producto.precio
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
