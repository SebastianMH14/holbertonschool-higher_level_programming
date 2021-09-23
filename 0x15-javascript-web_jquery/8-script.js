$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      const titles = data.results;
      $.each(titles, function (i, title) {
        $('UL#list_movies').prepend($('<li></li>').text(titles[i].title));
      });
    }
  });
});
