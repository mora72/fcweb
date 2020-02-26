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

    // configuração do filtro uf
    var filteruf     = $('#filteruf');
    var baseUrl   = 'http://localhost:8000/';

    // configuração do filtro status
    var filterstatus     = $('#filterstatus');
    var baseUrlIrmaos   = 'http://localhost:8000/irmaos/';

    // configuração da busca
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    // configuração da busca irmao
    var searchBtnIrmao = $('#searchirmao-btn');
    var searchFormIrmao = $('#searchirmao-form');

    // configuração da busca local de interesse
    var searchBtnLocalInteresse = $('#search-btn-localinteresse');
    var searchFormLocalInteresse = $('#searchlocalinteresse-form');

    // Ação do filtro uf (change)
    $(filteruf).change(function() {
        var filteruf = $(this).val();
        window.location.href = baseUrl + '?filteruf=' + filteruf;
    });

    // Ação do filtro status (change)
    $(filterstatus).change(function() {
        var filterstatus = $(this).val();
        var filterlocal = $('#filterlocal').val();
        window.location.href = baseUrlIrmaos + '?filterstatus=' + filterstatus + '&filterlocal=' + filterlocal;
    });

    // Ação do filtro local (change)
    $(filterlocal).change(function() {
        var filterlocal = $(this).val();
        var filterstatus = $('#filterstatus').val();
        window.location.href = baseUrlIrmaos + '?filterlocal=' + filterlocal + '&filterstatus=' + filterstatus;
    });

    // Ação da busca Local (click)
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    // Ação da busca Irmao (click)
    $(searchBtnIrmao).on('click', function() {
        searchFormIrmao.submit();
    });

    // Ação da busca Local de Interesse (click)
    $(searchBtnLocalInteresse).on('click', function() {
        searchFormLocalInteresse.submit();
    });

});
