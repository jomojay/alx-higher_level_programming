$(document).ready(() => {
  $('input#btn_translate').click(() => {
    const lang = $('input#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`, (data) => {
      $('div#hello').html(data.hello);
    });
  });
});
