/**
 * 
 * @param {*} idProducto 
 */
function abrirModalEliminar(idProducto){
    Swal.fire({
        title: 'Eliminar Producto',
        text: 'Esta seguro de Eliminar?',
        icon : 'warning',
        showCancelButton : true,
        confirmButtonColor:'#3585d6',
        cancelButtonColor: '#d33',
        cancelButtonText: 'NO',
        confirmButtonText:'SI'
    }).then((result)=>{
        if (result.isConfirmed){
            location.href=`/eliminarProducto/${idProducto}/`
        }
    })
}

console.log("La piña de la niña");