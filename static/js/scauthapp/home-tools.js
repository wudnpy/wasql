$(document).ready(function(){
    //////////////////////////////////////////////////Создаю список из массиваа
    var python = {};
    python.name = 'Python';
    python.modules = ['Django'];


    var javascript = {};
    javascript.name = 'Javacript';
    javascript.modules = ['jQuery', 'Bootstrap', 'D3.js'];

    var html = {};
    html.name = 'HTML';
    html.modules = ['HTML5'];

    var css = {}
    css.name = 'CSS';
    css.modules = ['CSS3'];

    var db = {}
    db.name = "DB"
    db.modules = ['SQLite']

    var tools = [python, javascript, html, css, db]

    var list = $("#details").append('<ul id=\"tools\"></ul>');

    for (var tool = 0; tool < tools.length; tool++) {
        $('#tools').append('<li id=\"'+ tools[tool].name + '\">' + '<b>' + tools[tool].name + '<b>' + '</li>')
            $('#'+tools[tool].name).append('<ul></ul>');

            for (var modul = 0; modul < tools[tool].modules.length; modul++) {
                $('#'+tools[tool].name).find('ul').append('<li>'+tools[tool].modules[modul]+'</li>');
            }
    }

    alert ('jQuery подключен и отлично работает!');

});
