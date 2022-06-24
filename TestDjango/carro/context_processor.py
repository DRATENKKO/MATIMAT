def importe_total_carrito(request):
    total = 0

    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total += total+(int(value["precio"])*value["cantidad"])
            
    else : 
        total = "Debes iniciar sesión para realizar una compra."
    return {"importe_total_carrito":total}