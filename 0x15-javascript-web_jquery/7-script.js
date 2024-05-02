$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (starwars) {
  $('#character').text(starwars.name);
});
