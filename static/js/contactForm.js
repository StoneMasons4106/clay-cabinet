function contactForm() {
  var csrf = $('input[name="csrfmiddlewaretoken"]').attr("value");
    $.ajax({
      type: "POST",
      url: "/contact/",
      data: $('form').serializeArray(),
      headers: {
        'X-CSRFToken': csrf,
      },
      contentType: "application/javascript",
      dataType: "json",
  });
};

function validateEmail(email) {
  const res = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return res.test(String(email).toLowerCase());
};

function callback(){
  if(grecaptcha.getResponse().length !== 0){
    console.log("The captcha has been already solved.");
  } else {
    console.log("The captcha has not been solved.")
  };
};

$(document).ready(function(){
  $('.g-recaptcha').attr("data-callback", "callback");
  var count = 0;
  $('#contact-button').on('click', function() {
    if (count == 1) {
      //do nothing
    } else if ($("input[name='first-name']").val() == "") {
      //do nothing
    } else if ($("input[name='last-name']").val() == "") {
      //do nothing
    } else if ($("input[name='subject']").val() == "") {
      //do nothing
    } else if ($("textarea[name='message']").val() == "") {
      //do nothing
    } else if ($("input[name='email']").val() == "") {
      //do nothing
    } else {
      if(grecaptcha.getResponse().length !== 0) {
        var emailIsValid = validateEmail($("input[name='email']").val());
        if (emailIsValid) {
          count = count + 1;
          contactForm();
          $(this).addClass("button-loading");
          setTimeout(function(){
            $("#contact-button").addClass("success");
          }, 2500);
        } else {
          //do nothing
        };
      } else {
        //do nothing
      };
    };
  });
});
