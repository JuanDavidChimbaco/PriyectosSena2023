listaProductos = [];
listaClientes = [];
listaDetalles = [];

$("#txtCodigoProducto").change(function () {
    buscarProductos();
})
$("#btnConsultarCliente").click(function () {
    buscarClientes();
})
$("#btnAgregarDetalle").click(function () {
    agregarDetalle();
    imprimirDetalle();
    limpiar();
    $("#txtIdentificacion").val('')
})

function buscarClientes() {
    let codigo = $("#txtIdentificacionCliente").val();
    existe = false
    listaClientes.forEach(cliente => {
        if (cliente[0] == codigo) {
            existe = true
            console.log(cliente)
            Swal.fire('CLIENTE','Cliente Seleccionado','success')
            return existe
        }
    });
    if (!existe) {
        Swal.fire('CLIENTE','Cliente No existe','warning')
        $("#txtIdentificacion").val('')
    }
}

function buscarProductos() {
    let codigo = $("#txtCodigoProducto").val();
    existe = false
    listaProductos.forEach(producto => {
        if (producto[0] == codigo) {
            $("#txtNombreProducto").val(producto[1]);
            console.log(producto)
            existe = true
            Swal.fire('PRODUCTOS','Producto Seleccionado','success')
            return existe
        }
    
    });
    if (!existe) {
        Swal.fire('PRODUCTOS','Producto No existe','warning')
        limpiar();
    }
}

function limpiar() {
    $("#txtCodigoProducto").val('')
    $("#txtCantidadProducto").val('')
    $("#txtNombreProducto").val('')
}

function agregarDetalle() {
        let codigo = $("#txtCodigoProducto").val();

        listaProductos.forEach(producto => {
            console.log(producto)
            if (producto[0] == codigo) {
                
                const p = {
                    "codigo": codigo,
                    "nombre": producto[1],
                    "precio": producto[2],
                    "cantidad": $("#txtCantidadProducto").val(),
                    "valor": parseInt($("#txtCantidadProducto").val()) * parseInt(producto[2])
                }
                listaDetalles.push(p);
                console.log(listaDetalles);
                Swal.fire('DETALLES','Detalle Agregado','success');
                limpiar();
            }
        });
}

function imprimirDetalle() {
    let tabla = document.querySelector("table tbody#datosTabla");

    let fila = document.createElement("tr");
    let celdaCodigo = document.createElement("td");
    let celdaNombre = document.createElement("td");
    let celdaPrecio = document.createElement("td");
    let celdaCantidad = document.createElement("td");
    let celdaValor = document.createElement("td");

    listaDetalles.forEach(detalle => {
        celdaCodigo.textContent = detalle.codigo;
        celdaNombre.textContent = detalle.nombre;
        celdaPrecio.textContent = detalle.precio;
        celdaCantidad.textContent = detalle.cantidad;
        celdaValor.textContent = detalle.valor;

        fila.appendChild(celdaCodigo);
        fila.appendChild(celdaNombre);
        fila.appendChild(celdaPrecio);
        fila.appendChild(celdaCantidad);
        fila.appendChild(celdaValor);

    })
    tabla.appendChild(fila);
}

function obtenerListaProductos() {
    $.ajax({
        url: '/obtenerListaProducto',
        type: 'GET',
        dataType: 'json',
        cache: false,
        success: function (resultado) {
            console.log(resultado);
            listaProductos = resultado.datos;
        },
        error: function (resultado) {
            console.log(resultado);
        }
    });
}

function obtenerListaClientes() {
    $.ajax({
        url: '/obtenerListaCliente',
        type: 'GET',
        dataType: 'json',
        cache: false,
        success: function (resultado) {
            console.log(resultado);
            listaClientes = resultado.datos;
        },
        error: function (resultado) {
            console.log(resultado);
        }
    });
}