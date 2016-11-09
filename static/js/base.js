$(document).ready(function()
{
	 $("#bs-example-navbar-collapse-1 .nav li").on('click','#bs-example-navbar-collapse-1 .nav',function(){
	 	console.log($(this));
	    $(this).addClass("active").siblings().removeClass("active");
	})



	$(window).scroll(function(){
	  var top=$(window).scrollTop();
	  if(top>=340){
		  $("#nav").addClass("fix");
		  $("#nav").css({color:"red",top:0});
		  }else{
			  $("#nav").removeClass("fix");}
	});

});


