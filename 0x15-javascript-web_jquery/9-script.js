//script that fetches from url and displays the value of hello

let url = 'https://hellosalut.dev/?lang=fr'
$.get('url', function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});