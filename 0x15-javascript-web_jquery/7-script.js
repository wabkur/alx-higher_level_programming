//javascript that fetches the character name

let url = 'https://swapi.co/api/people/5/?format=json'
$.get(url, function (data, textstatus) {
    $('div#character').text(data.name);
});