<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en">
<head>
	<title>Sign in to XFINITY WiFi</title>
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
	<meta name="description" content="login.page.description">
	<meta name="viewport" content="width=1070">
	<meta name="format-detection" content="telephone=no">
	<link rel="shortcut icon" href="static/images/global/favicon.ico">
	<!-- Reset Stylesheets -->
	<link href="static/css/reset.css" media="screen" rel="stylesheet" type="text/css" />

	<!-- Wifi Stylesheets -->
	<link href="static/css/comcast.wifi.css" media="screen" rel="stylesheet" type="text/css" />

	<script src="/jquery/js/jquery.js"></script>

	<script>
		$(document).ready(function() { 
									
												if ($("#error").text().length == 0) $("#error").hide();
			if ($("#error-amenity").text().length == 0) $("#error-amenity").hide();
			//alert($("#error-amenity").text().length);
					    $('#sign_in').click(function() {  

		        var hasError = false;
		        $("#error-amenity").hide();
		        $("#error").text("");
		        if($("#username").val() == '') {
			        $("#error").append("<li>Email or username can not be blank</li>");
			        hasError = true;
		        }

		        if($("#password").val() == '') {
			        $("#error").append("<li>Password can not be blank</li>");
			        hasError = true;
		        }

		        if(hasError == true) { 
		        	$("#error").show();
		        	return false; 
		        }

		    });
		     $('#mdu-sign_in').click(function() {  

		        var hasError = false;
		        $("#error").hide();
		        $("#error-amenity").text("");
		        if(!isValidEmailAddress($("#mdu-email").val()))
			    {
			    	$("#error-amenity").append("<li>Email is not valid</li>");
			    	hasError = true;
			    }

		        var zipRegex = /^\d{5}$/;
			    if (!zipRegex.test($("#zip_code").val()))
			    {
			    	$("#error-amenity").append("<li>Zip code is not valid</li>");
			        hasError = true;
			    }

				if(!$("#mdu-terms").is(':checked') ) {
					$("#error-amenity").append("<li>Please accept Terms of Service</li>");
		           	hasError = true;
		        }

		        if(hasError == true) { 
		        	$("#error-amenity").show();
		        	return false; 
		        }

		    });

		     function isValidEmailAddress(emailAddress) {
			    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
			    return pattern.test(emailAddress);
			};
		});
	</script>
</head>
<!--[if IE 7]><body class="ie7"><![endif]-->
<!--[if IE 8]><body class="ie8"><![endif]-->
<!--[if IE 9]><body class="ie9"><![endif]-->
<!--[if !IE]><!-->
<body>
<!--<![endif]-->
	<div id="container">
		<div id="hero-container">
			<img id="hero-splash" src="static/images/hero-park.jpg" alt=""/>
			<div id="hero-logo"></div>
						<div id="hero-copy">
				<h1>Getting online has <strong>never been easier.</strong></h1>
				<p>Surf, stream, or share from thousands of XFINITY<sup>&reg;</sup> WiFi hotspots.</p>
			</div>
		</div>

		<div id="content">
			<div class="hotspots-info">
				<h2>Hotspots wherever you go</h2>
				<p>Conserve usage on your wireless data plan at over 500,000 hotspots.</p>
				<div class="content-link">
					<a href="http://hotspots.wifi.comcast.com/">Find a hotspot</a>
				</div>
			</div>
			<div class="hotspots-columns group">
				<div class="hotspots-column hotspots-column-1">
					<div class="hostspot-img"></div>
					<h2>Blazing fast Internet speeds</h2>
					<p>XFINITY<sup>&reg;</sup> Internet delivers reliably fast speeds, so you can do more of what you love online &ndash; at home or away.</p>
					<div class="content-link">
						<a href="http://www.comcast.com/wifi/trial.htm ">Learn more about XFINITY Internet</a>
					</div>
				</div>
				<div class="hotspots-column hotspots-column-2">
					<div class="hostspot-img"></div>
					<h2>Awesome is having it all &ndash; your way</h2>
					<p>Enjoy XFINITY services the way you want &ndash; from movies in the park to HD calls from your TV, and much more.</p>
					<div class="content-link">
						<a href="http://www.comcast.com/corporate/learn/xfinity-overview.html">Learn more about XFINITY</a>
					</div>
				</div>
			</div>

			<div id="terms-disclaimer">
			<span>To manage your Comcast communication preferences click <a href="https://emails.xfinity.com/pub/rf?_ri_=X0Gzc2X%3DWQpglLjHJlYQGr4zgAjba6i2K26HGRmKWO25oCdfVwjpnpgHlpgneHmgJoXX0Gzc2X%3DWQpglLjHJlYQGotvlvN3GwqOGzfX9ef2zftaIuU8n&CAMPAIGN_NAME=WiFi_amenity_signup">here</a>. Not available in all areas.
						 Restrictions apply. Hotspots claim based on June 21, 2013 study by Allion Test Labs, Inc. 
						 XFINITY WiFi is included for XFINITY Internet Performance tier and above only. Requires 
						 compatible WiFi-enabled laptop or mobile device. Hotspots available in select locations only. 
						  Call 1-800-XFINITY or email <a href="mailto:xfinitywifi_support@cable.comcast.com">xfinitywifi_support@cable.comcast.com</a> for details. Comcast © 2013. 
						  All rights reserved. 
						  </span>
			</div>

			<div id="legal-disclaimer">
			<span>Parks and Recreation (c)&nbsp;2013 Open 4 Business Productions LLC.</span></div>

		</div>

		<div class="rails-container">
			<div class="signin-rail rails-box">
				<form name="signin" action="user_login.php" method="post">
				<h2>Get started here!</h2>
				<div class="rails-padding">
					<h3>XFINITY Internet or Comcast Business customers sign in here</h3>
					<p id="error" class="error"></p>
				
					<div class="form-field">
						<div class="ie-placeholder">
							<label >Email or username</label>
							<input tabindex="1" type="text" placeholder="Email or username" name="username" maxlength="50" id="username" class="text">
						</div>
						<span class="validation-error">Please enter a valid username</span>
						<a tabindex="2" href="https://login.comcast.net/myaccount/lookup?continue=http%3A%2F%2Fwifilogin.comcast.net%2Fwifi%2Fxwifi.php%3Fhash%3DQPOcjvD4O2isG6zxDRkrRFZDVEJv%252B%252BgM%252Bw%252BFyd%252Bb1vEYorLv3j5Vhu6etuwYFB1JyNgm9svZSMYRNAUzKCER6SH7pfZIt8zkcrJrYlui0%252Fw0YlYMCm5R7pBz%252Ffv4rISutpTCBMLnLPAdn%252BcWlz8FntI1i6FAaoNtw0GShRnL8aJ9Gy0fRZRSVJvKXTm0ngKcEfkgunb1WoUrQh92KGrSgI3XjZoCOn%252BSGCQTzB35KDFY7ox5bn0jXXpQrftPU1Fr" class="">Don&rsquo;t know your email or username?</a>
					</div>
					<div class="form-field">
						<div class="ie-placeholder">
							<label >Password</label>
							<input tabindex="3" type="password" placeholder="Password" maxlength="50" id="password" class="text" name="password">
						</div>
						<span class="validation-error">Please enter a valid password</span>
						<a tabindex="4" id="forgotPwdLink" href="https://login.comcast.net/myaccount/reset?continue=http%3A%2F%2Fwifilogin.comcast.net%2Fwifi%2Fxwifi.php%3Fhash%3DQPOcjvD4O2isG6zxDRkrRFZDVEJv%252B%252BgM%252Bw%252BFyd%252Bb1vEYorLv3j5Vhu6etuwYFB1JyNgm9svZSMYRNAUzKCER6SH7pfZIt8zkcrJrYlui0%252Fw0YlYMCm5R7pBz%252Ffv4rISutpTCBMLnLPAdn%252BcWlz8FntI1i6FAaoNtw0GShRnL8aJ9Gy0fRZRSVJvKXTm0ngKcEfkgunb1WoUrQh92KGrSgI3XjZoCOn%252BSGCQTzB35KDFY7ox5bn0jXXpQrftPU1Fr" title="Reset Password" tabindex="60">Don&rsquo;t know your password?</a>
					</div>
					<div class="btn btn-yellow">
						<button tabindex="5" type="submit" id="sign_in" class="submit">Sign in</button>
						<input type="hidden" id="hash" name="hash" value="QPOcjvD4O2isG6zxDRkrRFZDVEJv++gM+w+Fyd+b1vEYorLv3j5Vhu6etuwYFB1JyNgm9svZSMYRNAUzKCER6SH7pfZIt8zkcrJrYlui0/w0YlYMCm5R7pBz/fv4rISutpTCBMLnLPAdn+cWlz8FntI1i6FAaoNtw0GShRnL8aJ9Gy0fRZRSVJvKXTm0ngKcEfkgunb1WoUrQh92KGrSgI3XjZoCOn+SGCQTzB35KDFY7ox5bn0jXXpQrftPU1Fr" />
					</div>
				</div>
				</form>
			</div>

			
			<div class="support-rail rails-box" id="phone-box">
				<div class="rails-padding">
					<div class="phone-support">
						<p>For username &amp; password help call:</p>
						<h3>1-800-XFINITY</h3>
												<p style="margin-top:1em;">Customers in the New England area call:</p>
						<h3>1-855-845-6834</h3>
											</div>
					<a href="http://www.comcast.com/wifi/default.htm?SCRedirect=true">Learn more about XFINITY WiFi</a>
					<span>Comcast Business customers, call: 1-800-391-3000</span>
					<span>Not an XFINITY customer? Call: 1-855-214-1190</span>
				</div>
			</div>
		</div>

		<div id="footer-container">
			<div id="footer-wifi">
				<div id="footer-logo"></div>

				<span>&copy; 2013 Comcast</span>

				<a href="http://www.comcast.com/wifi/comcastwifiprivacy.html">
					Privacy Statement
				</a>

				<a href="http://www.comcast.com/wifi/comcastwifiAUP.html">
					Acceptable Use Policy
				</a>

				<a href="http://www.comcast.com/wifi/comcastwifiterms.html">
					Terms of Service
				</a>

			</div>
		</div>
	</div>
</body>
</html>
read:errno=0
