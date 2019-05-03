
function initMap(geolocation, div) {
    var ville = geolocation;
    var miniMap = new google.maps.Map(
        document.getElementById(div),
        {
            zoom: 12,
            center: ville
        });
    var marker = new google.maps.Marker({position: ville, map: miniMap});
}

function initStyleMsg() {
    var classBot = "table-warning text-secondary border border-warning rounded-lg px-2 msg-bot";
    var lastTextBot = $('#cardBody > p:last');

    lastTextBot.addClass(classBot);
    lastTextBot.removeClass('d-none');
}

function firstMsgBot(text, maps=false, coord=null) {
    var addBaliseBot = "<p class='d-none'>"+text+'</p>';

    $(addBaliseBot).appendTo('#cardBody');
    initStyleMsg();

    if (maps) {
        var idMiniMap = "miniMapTest"+num;
        var addMiniMap = "<div id='"+idMiniMap+"'></div>";
        
        $(addMiniMap).appendTo('#cardBody');

        var miniMap = $('#'+idMiniMap);

        miniMap.addClass('mapTest');
        initMap(coord, idMiniMap);
        num++;
    }
}

function secondMsgBot(text) {
    var imgBotMsg = "<img src='/static/img/img_msg.png' alt='papy message' class='img-fluid'>";
    var addBaliseBot = "<p class='d-none'>"+text+'</p>';

    $('#cardBody img').remove();
    $(imgBotMsg).appendTo('#cardBody');
    $(addBaliseBot).appendTo('#cardBody');
    initStyleMsg();
}

var num = 0;

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

    var data = $('#champsDeSaisie');
    var emojiTired = "<i class='far fa-tired'></i>";
    var emojiGrinWink = "<i class='far fa-grin-wink'></i>";
    var classUser = "table-primary text-primary border border-primary rounded-lg px-2 msg-user";
    var scrollElem = document.getElementById('cardConversation');
    var textBot1;
    var textBot2;

    scrollElem.scrollTop = scrollElem.scrollHeight;

    data.keypress(function (event){
        if (event.key === "Enter") {

            var textUser = data.val();
            if (textUser !== "") {
                var addBaliseUser = "<p class='d-none'>"+textUser+'</p>';

                data.val("");
                $(addBaliseUser).appendTo('#cardBody');

                var lastTextUser = $('#cardBody > p:last');

                lastTextUser.addClass(classUser);
                lastTextUser.removeClass('d-none');
                scrollElem.scrollTop = scrollElem.scrollHeight;
                // var intervalId = setInterval(ClignotementImg, 2000);

                $.ajax({
                    url: '/search',
                    type: 'GET',
                    data: 'phrase=' + textUser,
                    success: function (response) {

                        /* Response Ajax */
                        var reponseAjax = JSON.parse(response);
                        var informations;
                        var check;
                        var history = reponseAjax.history;
                        console.log(history);
                        /* end response Ajax */

                        if (reponseAjax.result === "Lieu non trouver") {
                            informations = {'formatted_address': 'Aucune adresse ne correspond', 'name': 'ta demande'};
                            check = false;
                        }else {
                            informations = reponseAjax.result;
                            var coordinate = informations.location;
                            check = true;
                        }

                        if (history === "La page n'existe pas") {
                            if (check) {
                                textBot1 = "Voici l'adresse que tu ma demander gamins<br>"+informations.formatted_address+"<br>"+emojiGrinWink;
                                firstMsgBot(textBot1, maps=true, coord=coordinate);
                                textBot2 = "Je suis désoler, j'ai pas réussi à trouver d'histoire sur "+informations.name+".<br>Soit il est trop vieux et mes aventures ne mi conduisent pas, ou soit il est trop récent pour moi "+emojiTired;
                                secondMsgBot(textBot2);
                            }else{
                                textBot1 = "Tu m'excuseras mais GrandPy n'a pas réussi à trouver d'adresse pour "+informations.name+". "+emojiTired;
                                firstMsgBot(textBot1);
                                textBot2 = "Je suis désoler, j'ai pas réussi à trouver d'histoire sur "+informations.name+".<br>Soit il est trop vieux et mes aventures ne mi conduisent pas, ou soit il est trop récent pour moi "+emojiTired;
                                secondMsgBot(textBot2);

                            }
                        }else {
                            textBot1 = "Voici l'adresse que tu ma demander gamins<br>"+informations.formatted_address+emojiGrinWink;
                            firstMsgBot(textBot1, maps=true, coord=coordinate);
                            textBot2 = "Mon petit voici l'histoire de "+informations.name+".<br>"+history.description+"<br>Si tu veut en savoir plus sur ce lieu, vas voir ici <a href=\""+history.link+"\" class='badge badge-info'>wikipedia</a>";
                            secondMsgBot(textBot2);
                        }

                        scrollElem.scrollTop = scrollElem.scrollHeight;
                    },
                    error: function (error) {
                        console.log(error);
                    }
                });
                }
            
            scrollElem.scrollTop = scrollElem.scrollHeight;
        }
    });
});