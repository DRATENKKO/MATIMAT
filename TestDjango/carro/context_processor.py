def importe_total_carrito(request):
    total = 0

    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total+int(value["precio"])
            
    else : 
        total = "Debes iniciar sesión para ver el total."
    return {"importe_total_carrito":total}