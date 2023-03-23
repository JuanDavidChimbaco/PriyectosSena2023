let listaPeliculas = [];
$(function () {
    $("#tblPeliculas").DataTable();
    $('#file_Foto').on('change', function (e){
        validarFoto(e)
    })
});

async function agregarPelicula() {
    if (validarDatos()) {
        const url = "/agregarPelicula";
        const datos = new FormData(document.getElementById("frmPelicula"));
        const response = await fetch(url, {
            method: "post",
            body: datos,
        });

        const respuesta = await response.json();
        console.log(respuesta);
        if (respuesta.estado) {
            Swal.fire("Registro Pelicula", respuesta.mensaje, "success").then(
                (result) => {
                    if (result.isConfirmed) {
                        // Acción a realizar después de que se cierre el modal Swal
                        limpiar();
                        location.reload()
                    }
                }
            );
        } else {
            Swal.fire("Registro Pelicula", respuesta.mensaje, "warning");
        }
    } else {
        Swal.fire("Registro Pelicula", "Faltan Datos", "warning");
    }
}

function validarDatos() {
    codigo = document.getElementById("txtCodigo").value;
    titulo = document.getElementById("txtTitulo").value;
    duracion = document.getElementById("txtDuracion").value;
    director = document.getElementById("txtDirector").value;
    fechaLanzamiento = document.getElementById("txtFechaLanzamiento").value;

    if (
        codigo == "" ||
        titulo == "" ||
        duracion == "" ||
        director == "" ||
        fechaLanzamiento == ""
    ) {
        //alert("Campos Vacio ") borrar esto
        return false;
    } else {
        //alert("Campos LLenos") borrar esto
        return true;
    }
}

async function consultarPorCodigo() {
    if (document.getElementById("txtCodigo").value != "") {
        const url = "/consultarPorCodigo";
        const data = new FormData();
        codigo = document.getElementById("txtCodigo").value;
        data.append("codigo", codigo);
        const response = await fetch(url, { method: "post", body: data });
        const respuesta = await response.json();
        console.log(respuesta);
        if (respuesta.peliculaConsultada != null) {
            document.getElementById("idPelicula").value =
                respuesta.peliculaConsultada[0];
            document.getElementById("txtTitulo").value =
                respuesta.peliculaConsultada[2];
            document.getElementById("txtDuracion").value =
                respuesta.peliculaConsultada[3];
            document.getElementById("txtDirector").value =
                respuesta.peliculaConsultada[4];
            let fecha = convertFecha(respuesta.peliculaConsultada[5]);
            document.getElementById("txtFechaLanzamiento").value = fecha;
            document.getElementById("txtResumen").value =
                respuesta.peliculaConsultada[6]; 
            document.getElementById("cbGenero").value = 
                respuesta.peliculaConsultada[7];
            
        } else {
            Swal.fire("Consultar Pelicula", respuesta.mensaje, "warning");
        }
    } else {
        Swal.fire("Consultar Pelicula", "Debe ingresar codigo", "warning");
    }
}

function convertFecha(fechaPython) {
    let fecha = new Date(fechaPython);
    dia = fecha.getDate();
    mes = fecha.getMonth() + 1;
    year = fecha.getFullYear();
    if (mes < 10) {
        mes = "0" + mes;
    }
    if (dia < 10) {
        dia = "0" + dia;
    }
    fechaCompleta = year + "-" + mes + "-" + dia;
    return fechaCompleta;
}

async function actualizar() {
    const data = new FormData(document.getElementById("frmPelicula"));
    const url = "/actualizar";
    if (validarDatos()){
        const response = await fetch(url, {
                method: "post",
                body: data
        });
        const respuesta = await response.json();
        console.log(respuesta);
        if (respuesta.estado) {
            listaPeliculas = respuesta.listaPeliculas;
            mostrarDatosTabla();
            Swal.fire("Actualizacion Pelicula", respuesta.mensaje, "success")
            .then(
                (result) => {
                    if (result.isConfirmed) {
                        // Acción a realizar después de que se cierre el modal Swal
                        limpiar();
                        location.reload()
                    }
                }
            );
        } else {
            Swal.fire("Actualizacion Pelicula", respuesta.mensaje, "warning");
        }
    }
}

function limpiar() {
    document.getElementById("txtCodigo").value = "";
    document.getElementById("txtTitulo").value = "";
    document.getElementById("txtDuracion").value = "";
    document.getElementById("txtDirector").value = "";
    document.getElementById("txtFechaLanzamiento").value = "";
    document.getElementById("txtResumen").value = "";
    document.getElementById("cbGenero").value = "0";
}

function mostrarDatosTabla() {
    let datos = "";
    listaPeliculas.forEach((pelicula) => {
        datos += "<tr>";
        datos += "<td>" + pelicula[1] + "</td>";
        datos += "<td>" + pelicula[2] + "</td>";
        datos += "<td>" + pelicula[3] + "</td>";
        datos += "<td>" + pelicula[4] + "</td>";
        datos += "<td>" + convertFecha(pelicula[5]) + "</td>";
        datos += "<td>" + pelicula[6] + "</td>";
        datos += "<td>" + pelicula[8] + "</td>";
        datos += `<td><img src="./static/img/${pelicula[0]}.jpg" alt="${pelicula[2]}" width="75" height="100"> </td>`;
        datos += "</tr>";
    });
    document.getElementById("datosPeliculas").innerHTML = datos;
    //$('#tblPeliculas').dataTable();
}

function modalEliminar() {
    Swal.fire({
        title: "Eliminar Pelicula",
        text: "¿Esta seguro de eliminar la Pelicula ?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, borrar esto!",
        cancelButtonText: "No, dejar esto!",
    }).then((result) => {
        if (result.isConfirmed) {
            if (document.getElementById("idPelicula").value != "") {
                eliminar();
                limpiar();
            } else {
                Swal.fire(
                    "Eliminado!",
                    "Debe consultar Primero la Pelicula.",
                    "warning"
                );
            }
        }
    });
}

async function eliminar() {
    const url = "/eliminar";
    const datos = {
        idPelicula: document.getElementById("idPelicula").value,
    };
    const response = await fetch(url, {
        method: "post",
        body: JSON.stringify(datos),
        headers: { "Content-Type": "application/json" },
    });
    const respuesta = await response.json();
    console.log(respuesta);
    if (respuesta.estado) {
        listaPeliculas = respuesta.listaPeliculas;
        location.reload()
        mostrarDatosTabla();
        Swal.fire("Eliminado!", respuesta.mensaje, "success");
    } else {
        Swal.fire("Eliminado!", respuesta.mensaje, "warning");
    }
}

function validarFoto(evt) {
    let foto = document.getElementById("file_Foto");

    var archivos = evt.target.files || evt.target.value;
    let file_name = archivos[0].name;
    let size = archivos[0].size;

    if (size > 1000000) {
        Swal.fire({
            icon: "warning",
            title: "Muy grande",
            text: "El tamaño de la foto es superior a 1 Mega",
        });
    } else {
        let ext = file_name.split(".").pop().toLowerCase();

        if (ext != "jpg") {
            Swal.fire({
                icon: "warning",
                title: "Formato no valido",
                text: "Solo se aceptan archivos jpg",
            });
        } else {
            return true;
        }
    }

    foto.value = "";
    return false;
}
