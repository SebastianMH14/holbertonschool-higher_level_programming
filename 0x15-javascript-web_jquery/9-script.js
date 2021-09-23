$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $.each(data, function (i, hola) {
        $('DIV#hello').html(data[i]);
      });
    }
  });
});
