$(document).ready(function () {
  $("form").on("submit", function (e) {
    e.preventDefault();

    const email = $('input[type="email"]').val();
    const password = $('input[type="password"]').val();

    const data = {
      email: email,
      password: password,
    };

    $.ajax({
      url: "http://127.0.0.1:5001/api/v1/signin",
      method: "POST",
      data: JSON.stringify(data),
      contentType: "application/json",
      dataType: "json",
      success: function (res, testStatus, resCode) {
        console.log(res);
        console.log(testStatus);
        console.log(resCode.status);
        if (res.message) {
          $(".error").text("Invalid logging details");
          $(".error").addClass("showerror");
          setTimeout(() => {
            $(".error").removeClass("showerror");
          }, 3000);
        } else {
          window.location.href = "feed.html";
        }
      },
    });
  });
});
