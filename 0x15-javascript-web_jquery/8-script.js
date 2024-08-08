//script that fetches and lists the titlefor all movies

let url = 'https://swapi.co/api/people/5/?format=json'
$.get(url, function (data) {
    let rets = data.results;
    for (let ret of rets) {
        $('ul#list_movies').append(<li>${ret.title}</li>);
    }
});