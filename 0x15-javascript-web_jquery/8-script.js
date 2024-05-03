$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  const res = data.results;
  const mlist = $('ul#list_movies');
  for (let i = 0; i < res.length; i++) {
    mlist.append(`<li>${res[i].title}</li>`);
  }
});
