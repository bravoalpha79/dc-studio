// toggle show/hide driving sub-links

document.addEventListener("DOMContentLoaded", function(){
  document.querySelector(".driving-dropdown").addEventListener("click", function() {
    let drivingLinks = document.getElementsByClassName("driving-link");
    for (let link of drivingLinks) {
      link.classList.toggle("hidden");
    }
  })
});
