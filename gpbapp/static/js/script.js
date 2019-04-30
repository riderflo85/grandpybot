$(document).ready(function () {
    $('#champsDeSaisie').on('blur', function (e) {
        elt = e;
        elt.on('keypress', function() {
            inputUser = elt.value;
        });
    });
});