$(function() {
	$( ".inputs" ).on( "focus click", function() {
		$(this).parent().find('label').addClass('active focus');
		$(this).addClass('active focus');
	});
	$( ".inputs" ).blur(function() {
		if($(this).val() == ''){
			$(this).parent().find('label').removeClass('active value focus');
			$(this).removeClass('active value focus');
		}
		else{
			$(this).addClass('value');
			$(this).parent().find('label').addClass('value');
			$(this).parent().find('label').removeClass('focus');
			$(this).removeClass('focus');
		}
	});

	$( ".show_hide_password" ).on( 'click', function(event) {
        event.preventDefault();
        if($( ".pass" ).attr("type") == "text"){
            $('.pass').attr('type', 'password');
            $(this).addClass( "fa-eye-slash" );
            $(this).removeClass( "fa-eye" );
			$(this).removeClass( "active" );
        }else if($('.pass').attr("type") == "password"){
            $('.pass').attr('type', 'text');
            $(this).removeClass( "fa-eye-slash" );
            $(this).addClass( "fa-eye" );
            $(this).addClass( "active" );
        }
    });

	$( ".select" ).on( "focus click", function() {
		$(this).parent().find('label').addClass('active');
		$(this).addClass('active');
	});
	$( ".select" ).blur(function() {
		if($(this).val() == ''){
			$(this).parent().find('label').removeClass('active');
			$(this).removeClass('active');
		}
	});

})
