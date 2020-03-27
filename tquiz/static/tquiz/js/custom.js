

$("document").ready(function(){

move();

/* show marking scheme */
$('.m-scheme').click(function(){
    $('#detailed-res').removeClass('w3-hide');
})

/* show filter */
$("#filter").click(function(){
    $('#f-content').css('height',"100%");
})

/* hide filter */
$(".overlay-action").click(function(){
    $('#f-content').css('height',"0");
})

$("#bars").click(function(){
   $("#menu").css("width" , "100%");
})

$("#menu").click(function(){
   $("#menu").css("width" , "0");
})


$("#search-icon").click(function(){
   $("#search").css("height" , "100%");
})


$("#close-search").click(function(){
   $("#search").css("height" , "0");
})

/** tab controller **/
$('.quiz').click(function(){
  showTab('quiz');
})


$(".tutorials").click(function(){
  showTab('tutorials');
})

$('.q-n-a').click(function(){
  showTab('q-n-a');
})


$('.not-answered').click(function(){
  showTab('not-answered');
})


$('.answered').click(function(){
  showTab('answered');
})
/** end **/


})




/* progress bar js */
var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 0;
    var id = setInterval(frame, 160);

    function frame() {
      if (width >= 100) {
        clearInterval(id);
        $("#auto-submit").click();
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
        elem.innerHTML = width + "%";
      }
    }
  }
}


/* toggleTab function definition */
function showTab(tabName){

var tabId = "#" + tabName;
var tabClass = "." + tabName;
$('.tabNav').removeClass('active');
$(tabClass).addClass('active');
$(tabId).removeClass('w3-hide');
$('.tabContent').hide();
$(tabId).show();

};