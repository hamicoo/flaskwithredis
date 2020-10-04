
$(document).ready(function() {
    $('button#txtword').click(function(){
     
        var userword = $('#search').val();

        $.ajax({
        url: "/findtheword",
        type: "get",
        data: {
            userword: userword
            
        },

        success: function(response) {

 
             Toastify({
             text: response.message,
                 duration: 5000,
                 //destination: "https://github.com/apvarun/toastify-js",
             newWindow: true,
             close: true,
             gravity: "top", // `top` or `bottom`
             position: 'center', // `left`, `center` or `right`
             backgroundColor: response.noticetype ,
             stopOnFocus: true
                 //  ,  Prevents dismissing of toast on hover
             // onClick: function(){} // Callback after click
             }).showToast();


       },
       error: function(xhr) {
         Toastify({
             text: 'Error calling service please try again later',
                 duration: 5000,
                 //destination: "https://github.com/apvarun/toastify-js",
                 newWindow: true,
             close: true,
             gravity: "top", // `top` or `bottom`
             position: 'center', // `left`, `center` or `right`
             backgroundColor: "linear-gradient(to right, #eb5149, #fc190f)",
             stopOnFocus: true
                 //  ,  Prevents dismissing of toast on hover
             // onClick: function(){} // Callback after click
             }).showToast();
      }
      });
    });
 });











