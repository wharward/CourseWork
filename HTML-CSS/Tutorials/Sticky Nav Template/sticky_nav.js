$(document).ready(function () {
	
	
    $(window).scroll(function(){
		var mn = $(".main-nav");
		var scrollAmount = $(window).scrollTop();
		var documentHeight = $(document).height();
		var scrollPercent = (scrollAmount / documentHeight) * 100;
		
		mn.addClass("main-nav-scrolled");
		if(scrollAmount < 200) {
			// run a function called doSomething
			mn.removeClass("main-nav-scrolled");
		}
		else{
			mn.addClass("main-nav-scrolled");
		}
	});
});
