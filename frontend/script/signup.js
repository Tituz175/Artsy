$(document).ready(function () {
  $("form").on("submit", function (e) {
    e.preventDefault();

    const name = $('input[type="text"]').val();
    const email = $('input[type="email"]').val();
    const password = $('input[type="password"]:eq(0)').val();

    if (password == $('input[type="password"]:eq(1)').val()) {
      const data = {
        first_name: name.includes(" ") ? name.split(" ")[0].trim() : name,
        last_name: name.includes(" ") ? name.split(" ")[1].trim() : "",
        email: email,
        password: password,
      };

      $.ajax({
        url: "http://127.0.0.1:5001/api/v1/signup",
        method: "POST",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function (res, testStatus, resCode) {
          console.log(res);
          console.log(testStatus);
          console.log(resCode.status);
          if (resCode.status != 201) {
            $(".error").text(`${res.message}`);
            $(".error").addClass("showerror");
            setTimeout(() => {
              $(".error").removeClass("showerror");
            }, 3000);
          } else {
            window.location.href = "login-3.html";
          }
        },
      });
    } else {
      $(".error").text("Password mismatch");
      $(".error").addClass("showerror");
      setTimeout(() => {
        $(".error").removeClass("showerror");
      }, 3000);
    }
  });
});
