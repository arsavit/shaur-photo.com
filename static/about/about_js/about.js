$(document).ready(function () {

    $('.ars-panel-heading').click (function () {
        $(this).toggleClass('in').next().slideToggle();
        $('.ars-panel-heading').not(this).removeClass('in').next().slideUp();
        return false;
    });



});