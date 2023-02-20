$(document).ready(function(){
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/product',
        success: function(respose){
            console.log(respose)
        },
        error: function(error){
            console.log(error)
        }
    })
})
console.log("hello")