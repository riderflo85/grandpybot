
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

function secondMsgBot(text, timerAnim) {
    var imgBotMsg = "<img src='/static/img/img_msg.png' alt='papy message' class='img-fluid' id='papyMsg'>";
    var addBaliseBot = "<p class='d-none'>"+text+'</p>';

    $('#papyMsg').remove();
    $(imgBotMsg).appendTo('#cardBody');
    $(addBaliseBot).appendTo('#cardBody');
    initStyleMsg();
    clearTimeout(timerAnim);
    imgAnim.addClass('d-none');
}

function rotate() {
    imgAnim.removeClass('d-none');
    imgAnim.css({ WebkitTransform: 'rotate(' + degree + 'deg)'});  
    imgAnim.css({ '-moz-transform': 'rotate(' + degree + 'deg)'});                      
    timer = setTimeout(function() {
        ++degree; rotate();
    },1);
}

var imgAnim = $("#round");
var degree = 0;
var num = 0;
var timer;

$(document).ready(function () {

    var data = $('#champsDeSaisie');
    var emojiTired = "<i class='far fa-tired'></i>";
    var emojiGrinWink = "<i class='far fa-grin-wink'></i>";
    var classUser = "table-primary text-primary border border-primary rounded-lg px-2 msg-user";
    var scrollElem = document.getElementById('cardConversation');
    var textBot1;
    var textBot2;

    data.keypress(function (event){
        if (event.key === "Enter") {

            var textUser = data.val();
            if (textUser !== "") {
                rotate();
                var addBaliseUser = "<p class='d-none'>"+textUser+'</p>';

                data.val("");
                $(addBaliseUser).appendTo('#cardBody');

                var lastTextUser = $('#cardBody > p:last');

                lastTextUser.addClass(classUser);
                lastTextUser.removeClass('d-none');
                scrollElem.scrollTop = scrollElem.scrollHeight;

                setTimeout(function () {
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
                            var story = reponseAjax.story;
                            /* end response Ajax */

                            /* checks the contents of the Ajax response to display the correct message to the user */
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
                                    textBot1 = "Voici l'adresse que tu ma demander mon poussin<br>"+informations.formatted_address+"<br>"+emojiGrinWink;
                                    firstMsgBot(textBot1, maps=true, coord=coordinate);
                                    textBot2 = "Je suis désoler, j'ai pas réussi à trouver d'histoire sur "+informations.name+".<br>Soit il est trop vieux et mes aventures ne mi conduisent pas, ou soit il est trop récent pour moi "+emojiTired;
                                    secondMsgBot(textBot2, timer);
                                }else{
                                    textBot1 = "Tu m'excuseras mais GrandPy n'a pas réussi à trouver d'adresse pour "+informations.name+". "+emojiTired;
                                    firstMsgBot(textBot1);
                                    textBot2 = "Je suis désoler, j'ai pas réussi à trouver d'histoire sur "+informations.name+".<br>Soit il est trop vieux et mes aventures ne mi conduisent pas, ou soit il est trop récent pour moi "+emojiTired;
                                    secondMsgBot(textBot2, timer);
                                }
                            }else {
                                textBot1 = "Voici l'adresse que tu ma demander mon poussin<br>"+informations.formatted_address+". "+emojiGrinWink;
                                firstMsgBot(textBot1, maps=true, coord=coordinate);
                                textBot2 = informations.name+".<br>"+history.description+"<br>"+"<span class='lead'>"+story+"</span>"+"<br>Si tu veut en savoir plus sur ce lieu, vas voir ici <a href=\""+history.link+"\" class='badge badge-info'>wikipedia</a>";
                                secondMsgBot(textBot2, timer);
                            }
                            /* end check the contents of the Ajax response */

                            scrollElem.scrollTop = scrollElem.scrollHeight;
                        },
                        error: function (error) {
                            console.log(error);
                        }
                    });
                }, 500); // end setTimeOut
                }
            scrollElem.scrollTop = scrollElem.scrollHeight;
        }
    });
});