function performLogin() {
    var inputUsername = document.getElementById("username");
    localUsername = inputUsername.value;

    var inputPassword = document.getElementById("password");
    localPassword = inputPassword.value;
    
    if (1){
      window.location.href = "index.html";
    } else {
      alert("Check Username or Password");
    }
  }

  function clearForm() {
    // Clear input fields and any previous error messages
    var inputUsername = document.getElementById("username");
    var inputPassword = document.getElementById("password");

    inputUsername.value = "";
    inputPassword.value = "";
  }