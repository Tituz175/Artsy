$(document).ready(function () {
  // Check if 'id' exists in local storage
  const id = localStorage.getItem("id");
  if (!id) {
    // Redirect to login if 'id' is not present
    window.location.href = "login-3.html";
    return;
  }

  $.ajax({
    //   url: `https://tituz175.pythonanywhere.com/api/users/${id}`,
    url: `http://127.0.0.1:5000/api/users/${id}`,
    method: "GET",
    success: function (res, textStatus, xhr) {
      const usersDetails = res;
      console.log(textStatus);

      // Check for successful status
      if (xhr.status === 200) {
        console.log(usersDetails);
        $(".user p").text(
          `${usersDetails["first_name"]} ${usersDetails["last_name"]}`
        );
        $(".user small").text(`${usersDetails["occupation"]}`);

        localStorage.setItem(
            "user_details",
            `{"full_name": "${usersDetails["first_name"]} ${usersDetails["last_name"]}", "occupation": "${usersDetails["occupation"]}"}`
          );
          
      } else {
        // Handle other status codes if needed
        console.error("Error: ", xhr.status);
        // Redirect to login in case of an error
        window.location.href = "login-3.html";
      }
    },
    error: function (xhr, textStatus, errorThrown) {
      console.error("AJAX Error: ", errorThrown);
      // Redirect to login in case of an error
      window.location.href = "login-3.html";
    },
  });
});
