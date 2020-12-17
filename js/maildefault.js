document.addEventListener("DOMContentLoaded", function(event) {
    console.log("Jpolaaaa")
emailjs.init("user_VCV2fJ7SExXz708nP91Hr");
document.getElementById("submit_btn1").addEventListener("click", () => {
    var templateParams = {
        name: document.getElementById("name1").value,
        email: document.getElementById("email1").value,
        message: document.getElementById("message1").value
    };
    document.querySelectorAll(".getin_form .form-control").forEach( (element) => {
        element.style.border = '2px solid rgb(252,206,47)';
    })
    console.log(templateParams.name)
    if (templateParams.name != '' && templateParams.email != '' && templateParams.message != '' )
    {
        document.querySelectorAll(".getin_form .form-control").forEach( (element) => {
            element.style.border = '2px solid rgb(252,206,47)';
        })
        emailjs.send('service_9ixv46y', 'template_y8ce877', templateParams) //use your Service ID and Template ID
            .then(function(response) {
                document.querySelectorAll(".getin_form .form-control").forEach( (element) => {
                    element.style.border = '2px solid rgb(173,200,40)';
                })
                console.log('Todo salio bien!', response.status, response.text);
                Swal.fire(
                    'Email enviado!',
                    'En la brevedad nos estaremos contactando con usted. Muchas gracias!',
                    'success')
                document.getElementById("name1").value = ''
                document.getElementById("email1").value = ''
                document.getElementById("message1").value = ''
            }, function(error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Algo salio mal!',
                    footer: '<a href>Favor de volver a intentarlo</a>'
                })
            });
        }
    });
});