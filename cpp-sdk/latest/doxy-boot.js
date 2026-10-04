var ready = (callback) => {
  if (document.readyState != "loading") callback();
  else document.addEventListener("DOMContentLoaded", callback);
}



ready(() => { 
    var header = document.querySelector("div.headertitle");
    header.classList.add("page-header");
    var title =  document.querySelector("div.title");
    title.classList.add("h1");
    //$("div.headertitle").addClass("page-header");
    //$("div.title").addClass("h1");

    var divHeader = document.querySelector("div.header");
    divHeader.classList.remove("header");

    var tableparams = document.querySelector("table.params");
    tableparams.classList.add("table");
    //$("table.params").addClass("table");
  
});

