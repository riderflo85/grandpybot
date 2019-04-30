$(document).ready(function () {

    console.log('Page prete')
    var data = $('#champsDeSaisie');

    data.keypress(function (event){
        if (event.key === "Enter") {
            $.ajax({
                url: '/search',
                type: 'GET',
                data: 'phrase=' + data.val(),
                success: function (response) {
                    console.log(response);
                    var repJson = JSON.parse(response);
                    console.log(repJson.result);
                },
                error: function (error) {
                    console.log(error);
                }
            });
            data.val("");
        }
    });
});