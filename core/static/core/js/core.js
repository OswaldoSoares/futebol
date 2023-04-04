$(document).ready(function() {
    $(".card-campeonato").hide();
});

$(document).on('click', '.js-gera-campeonato', function(){
    $.ajax({
        type: 'GET',
        url: '/core/gera-campeonato',
        data: {},
        beforeSend: function(){
            $(".card-campeonato").hide();
        },
        success: function(data) {
            $(".card-campeonato").html(data.html_card_campeonato);
            $(".card-campeonato").show();
        },
    });
});