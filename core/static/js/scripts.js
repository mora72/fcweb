$( document ).ready(function() {
    // configuração do botão deletar
    var deleteBtn = $('#btndelete');
    $(deleteBtn).on('click', function(e) {
        e.preventDefault();
        var delLink = $(this).attr('href');
        var result = confirm('Confirma remoção ? ');
        if(result) {
            window.location.href = delLink;
        }
    });

    // configuração do filtro meio
    var filtermeio = $('#filtermeio');
    var baseUrl   = 'http://localhost:8000/trans/';

    // configuração da busca
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    // Ação do filtro meio (change)
    $(filtermeio).change(function() {
        var filtermeio = $(this).val();
        window.location.href = baseUrl + '?filtermeio=' + filtermeio;
    });

    // Ação da busca Local (click)
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

});
