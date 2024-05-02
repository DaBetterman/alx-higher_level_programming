$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (starwars) {
  $.each(starwars.results, function (position, value) {
    $('#list_movies').append('<li>' + value.title + '</li>');
  });
});
