// An example 128-bit key (16 bytes * 8 bits/byte = 128 bits)


// Convert text to bytes
//https://github.com/ricmoo/aes-js?utm_source=sharklabs.com.br&utm_medium=post-criptografia-javascript-aes&utm_campaign=criptografia-javascript-aes

var key = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ];

function encrypted(text){
	
	var textBytes = aesjs.utils.utf8.toBytes(text);

	// The counter is optional, and if omitted will begin at 1
	var aesCtr = new aesjs.ModeOfOperation.ctr(key, new aesjs.Counter(5));
	var encryptedBytes = aesCtr.encrypt(textBytes);

	// To print or store the binary data, you may convert it to hex
	var encryptedHex = aesjs.utils.hex.fromBytes(encryptedBytes);
	//console.log(encryptedHex);

	return encryptedHex;
	// "a338eda3874ed884b6199150d36f49988c90f5c47fe7792b0cf8c7f77eeffd87
	//  ea145b73e82aefcf2076f881c88879e4e25b1d7b24ba2788"
}




$(document).ready(function(){  
    var socket = io.connect("http://localhost:3000");
    var ready = false;

    $("#submit").submit(function(e) {
		e.preventDefault();
		$("#nick").fadeOut();
		$("#chat").fadeIn();
		var name = $("#nickname").val();
		var time = new Date();
		$("#name").html(name);
		$("#time").html('First login: ' + time.getHours() + ':' + time.getMinutes());

		ready = true;
		socket.emit("join", name);

	});

	$("#textarea").keypress(function(e){
        if(e.which == 13) {
			var text = '';
        	text = $("#textarea").val();
        	$("#textarea").val('');
        	var time = new Date();
					$(".chat").append('<li class="self"><div class="msg"><span>' + $("#nickname").val() + ':</span><p>' + text + '</p><time>' + time.getHours() + ':' + time.getMinutes() + '</time></div></li>');
					var textEncrypt = encrypted(text);
					console.log(textEncrypt);
					console.log(decrypted(textEncrypt));
					socket.emit("send", textEncrypt);
					// automatically scroll down
					document.getElementById('bottom').scrollIntoView();
        }
    });


    socket.on("update", function(msg) {
    	if (ready) {
    		$('.chat').append('<li class="info">' + msg + '</li>')
    	}
    }); 

    socket.on("chat", function(client,msg) {
		var msgDecrypted = decrypted(msg);
    	if (ready) {
			console.log(msg);
				var time = new Date();
				$(".chat").append('<li class="field"><div class="msg"><span>' + client + ':</span><p>' + msgDecrypted + '</p><time>' + time.getHours() + ':' + time.getMinutes() + '</time></div></li>');
				
    	}
    });

});

