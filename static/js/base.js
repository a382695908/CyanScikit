$(window).scroll(function(){
	  var top=$(window).scrollTop();
	  if(top>=340){
		  $("#nav").addClass("fix");
		  $("#nav").css({color:"red",top:0});
		  }else{
			  $("#nav").removeClass("fix");}
	});


