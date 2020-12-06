$(function () {
  $('#clipboard-copy-button').click(function () {
    let copyText = document.getElementById("clipboard-copy-text");
    copyText.hidden = false;
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand("copy");
    $('#clipboard-copy-icon').removeAttr("hidden");
    $('#clipboard-copy-button').addClass("text-success");
    copyText.hidden = true;
  });
})