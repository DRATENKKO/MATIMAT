const formulario = document.getElementById('formulario'); //accedemos al formulario 
const inputs = document.querySelectorAll('#formulario input'); //accedemos a todos los inputs del formulario

const expresiones = { // es un objeto que se llama expresiones
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{9}$/, // 9 numeros.
  valor: /^\d{4,8}$/ // 1 numero como mínimo y 8 numeros como máximo
}

const campos = { // ESTO ES UN OBJETO
	nombre: false,
	correo: false,
	telefono: false,
  valor: false
}

const validarFormulario = (e) => {
	switch (e.target.name) { //SWICTH (LO QUE QUIERO COMPROBAR)
		case "nombre":   
			validarCampo(expresiones.nombre, e.target, 'nombre'); // le pasamos la expresion regular que queremos utilizar para validar el campo, le pasamos el input(e.targert) y le pasamos su nombre(por id)
		break;  
		case "correo":
			validarCampo(expresiones.correo, e.target, 'correo');
		break;
		case "telefono":
			validarCampo(expresiones.telefono, e.target, 'telefono');
		break;
    case "valor":
			validarCampo(expresiones.valor, e.target, 'valor');
		break;
	}
}

const validarCampo = (expresion, input, campo) => { //
	if(expresion.test(input.value)){  // accedemos al valor del input(input value) y lo comprobamos con la expresion
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto'); // INPUT INCORRECTO COLOR ROJO 
    // ${campo} estamos tomando el valor que nosotros le pasemos a la variable 
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto'); // INPUT COLOR VERDE
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo'); // AQUI ELIMINAMOS EL TEXTO CUANDO EL TEXTO ESTÁ CORRECTO(EN VERDE)
		campos[campo] = true; // SI LA EXPRESION ES VALIDA ES DECIR QUE LOS CAMPOS SEAN CORRECTOS ( TRUE )
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto'); // SI LE COLOCAMOS UN SIMBOLO ESTARÁ DE COLOR ROJO
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo'); // AQUI MUESTA EL TEXTO DEL ERROR
		campos[campo] = false; // SI LA EXPRESION ES INVALIDA ES DECIR QUE LOS CAMPOS SEAN INCORRECTOS ( FALSE )
	}
}

inputs.forEach((input) => { // por cada input ejecutes un codigo
	input.addEventListener('keyup', validarFormulario);   // cuando levantes la tecla(keyup) se ejecuta (validarFormulario)
	input.addEventListener('blur', validarFormulario); // cuando aprietas el click fuera del formulario (blur)
  // se ejecuta (validarFormulario)
});

