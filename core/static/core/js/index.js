function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

$(function () {
  $('#image-upload-form').on('submit', (function (e) {
    let form = this;
    $('#step-1').addClass("d-none");
    $('#step-2').removeClass("d-none");
    setTimeout(function() {
      form.submit()
    }, 2000);

    return false;
  }));

  $("#image-upload-input").on("change", function () {
    $("#image-upload-form").submit();
  });
})