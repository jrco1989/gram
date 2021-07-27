setTimeout(function(){ alert("Hello"); }, 3000);
location.reload()

document.addEventListener("DOMContentLoaded", function(event) { 
    //do work
  });

  document.getElementById('CANTIDAD_DESAGREGACION_ITEM').type = 'number';
  document.getElementById('CANTIDAD_DESAGREGACION_ITEM').setAttribute('type','password')
  $('#password').attr('type', 'text');
  
  document.getElementById("img1").style.zIndex = "1"; 


  console.log(JSON.stringify({ x: 5, y: 6 })); //method converts a JavaScript object or value to a JSON string