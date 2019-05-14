/*
$(document).ready(function(){
	$('button').click(function(){
		$('h1').hide();
	});
});
*/
/*
$(function(){
	$('button').click(function(){
		$('#olamundo').hide();
		$('h1').css("color", "red");
	});
	$('#changeback').click(function(){
		$('#terraqueos').css("color", "white");
		$('#terraqueos').css("background-color", "green");
	});
});
*/
/*
$(function(){
	$('#blue').click(function(){
		$('p').css("color", "blue");
	});
	$('#red').click(function(){
		$('p').css("color", "red");
	});
});
*/
/*
$(function(){
	$('#red').click(function(){
		$('p').css("color","red");
		$('p').fadeOut('fast');
		$('p').delay(1000);
		$('p').fadeIn('fast');
	});
	$('#blue').click(function(){
		$('p').css("color","blue");
		$('p').fadeOut('slow');
		$('p').delay(1000);
		$('p').fadeIn('slow');
	});
});
*/
/*
$(function(){
	$('#blue').click(function(){
		$('p').css("background-color", "blue");
		$('p').fadeOut();
		$('p').delay(1000);
		$('p').fadeIn();
	});

	$('#red').click(function(){
		$('p').css("background-color", "red");
		$('#mensagem').text("Cor alterada com sucesso");
		$('#mensagem').css("color", "red");
		$('#mensagem').css('border','1px solid red');
		$('#mensagem').delay(1000);
		$('#mensagem').fadeOut('fast');
	});
});
*/
/*
$(function(){
	$('#blue').click(function(){
		$('p')
			.css("background-color", "blue")
			.fadeOut()
			.delay(1000)
			.fadeIn();
	});

	$('#red').click(function(){
		$('p').css("background-color", "red");
		$('#mensagem')
			.text("Cor alterada com sucesso")
			.css("color", "red")
			.css('border','1px solid red')
			.delay(1000)
			.fadeOut('fast');
	});
});
*/
/*
$(function(){
	$('#blue').click(function(){
		$('p')
			.css("background-color", "blue")
			.fadeOut()
			.delay(1000)
			.fadeIn();
	});

	$('#red').click(function(){
		$('p').css("background-color", "red");
		$('#mensagem')
			.text("Cor alterada com sucesso")
			.css({color: 'red', border:'1px solid red', backgroundColor: '#F08080'})
			.delay(1000)
			.fadeOut('fast');
	});
});
*/
$(function(){
	$('#blue').click(function(){
		$('p')
			.css("background-color", "blue")
			.fadeOut()
			.delay(1000)
			.fadeIn();
	});

	$('#red').click(function(){
		$('p').css("background-color", "red");
		$('#mensagem')
			.text("Cor alterada com sucesso")
			.css({color: 'red', border:'1px solid red'})
			.delay(1000)
			.addClass('green');

		$('button').removeClass('redClass');
	});
});