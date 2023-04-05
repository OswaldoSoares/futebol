$(document).ready(function() {
    $(".card-campeonato").hide();
});

$(document).on('click', '.js-gera-campeonato', function(){
    $.ajax({
        type: 'GET',
        url: 'gera_campeonato/',
        data: {},
        beforeSend: function(){
            $(".card-campeonato").hide();
        },
        success: function(data) {
            $(".card-campeonato").html(data.html_tabela_campeonato);
            $(".card-campeonato").show();
            $(".js-gera-campeonato").hide();
        },
    });
});