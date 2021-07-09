function myFunction() {
  console.log("clicked");
  var element = document.getElementById("menu-container-dropdown-id");

  if (element.classList) { 
    element.classList.toggle("menu-container-dropdown-display-non-class");
  } else {
    var classes = element.className.split(" ");
    var i = classes.indexOf("menu-container-dropdown-display-non-class");

    if (i >= 0) 
      classes.splice(i, 1);
    else 
      classes.push("menu-container-dropdown-display-non-class");
      element.className = classes.join(" "); 
  }
}


function removeDropdownHidingClass(){
     var element = document.getElementById("menu-container-dropdown-id");
     if (window.matchMedia("(max-width: 892px)").matches) {
        /* The viewport is less than, or equal to, 700 pixels wide */
        element.classList.remove("menu-container-dropdown-display-non-class");
      } else {
        /* The viewport is greater than 700 pixels wide */
      }

}






