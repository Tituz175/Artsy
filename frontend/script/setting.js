$(document).ready(function () {
    const userDetailsString = localStorage.getItem("user_details");
    const userDetails = userDetailsString ? JSON.parse(userDetailsString) : null;
  
    console.log(userDetails["occupation"]);
  
    $(".user p").text(`${userDetails["full_name"]}`);
    $(".user small").text(`${userDetails["occupation"]}`);
    
    let profilePic = $("#profic-pic");
    let inputImg = $("#input-img");
  
    inputImg.on("change", function () {
      if (inputImg[0].files && inputImg[0].files[0]) {
        console.log(inputImg[0].files[0])
        let reader = new FileReader();
        reader.onload = function (event) {
            // console.log(event.target.result)
          profilePic.css("background-image", "url(" + event.target.result + ")");
        };
        reader.readAsDataURL(inputImg[0].files[0]);
      }
    });
  });
  