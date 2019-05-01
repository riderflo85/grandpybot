
function initMap() {
    var uluru = {lat: -25.344, lng: 131.036};
    var map = new google.maps.Map(
        document.getElementById('mapTest'),
        {
            zoom: 9,
            center: uluru
        });
    var marker = new google.maps.Marker({position: uluru, map: map});
}

$(document).ready(function () {

    // var cond = 0;
    // function ClignotementImg() {
    //     if (cond <= 5) {
    //         $('#cardBody img').fadeOut(900).delay(300).fadeIn(800);
    //         cond++; 
    //     }else if (cond === 5) {
    //         clearInterval(intervalId);
    //         cond++;
    //     }
    // }



    console.log('Page prete')
    var data = $('#champsDeSaisie');

    var imgBotMsg = "<img src='/static/img/img_msg.png' alt='papy message' class='img-fluid'>";
    var classBot = "table-warning text-secondary border border-warning rounded-lg px-2 msg-bot"
    var classUser = "table-primary text-primary border border-primary rounded-lg px-2 msg-user"

    var scrollElem = document.getElementById('cardConversation');
    scrollElem.scrollTop = scrollElem.scrollHeight;

    data.keypress(function (event){
        if (event.key === "Enter") {

            var textUser = data.val();
            var addBaliseUser = "<p class='d-none'>"+textUser+'</p>';

            $(addBaliseUser).appendTo('#cardBody');

            var lastTextUser = $('#cardBody > p:last');

            lastTextUser.addClass(classUser);
            lastTextUser.removeClass('d-none');
            // var intervalId = setInterval(ClignotementImg, 2000);
            // $.ajax({
            //     url: '/search',
            //     type: 'GET',
            //     data: 'phrase=' + data.val(),
            //     success: function (response) {
            //         console.log(response);
            //         var repJson = JSON.parse(response);
            //         console.log(repJson.result);
            //     },
            //     error: function (error) {
            //         console.log(error);
            //     }
            // });

            data.val("");
            // var textUser = repJson;

            var textBot = "Voici ton adresse mon petit, va voir c'est chouette";
            var addBaliseBot = "<p class='d-none'>"+textBot+'</p>';

            $('#cardBody img').remove();
            $(imgBotMsg).appendTo('#cardBody');
            $(addBaliseBot).appendTo('#cardBody');

            var lastTextBot = $('#cardBody > p:last');

            lastTextBot.addClass(classBot);
            lastTextBot.removeClass('d-none');
            scrollElem.scrollTop = scrollElem.scrollHeight;
            
        }
    });
});