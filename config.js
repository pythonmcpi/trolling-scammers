module.exports = {
	debug: false, // Headless?
	target: 'https://disorde.gift/AVBrDhAbECvcW', // URL
	button_selector: 'body > div > div > div > div > div > div > div > button', // Button to open fake login dialog
	//frame_selector: 'body > div:not(#app-mount)', // Fake window containing phishing form
	form_selector: 'form[name=logon]', // Inside iframe
	username_selector: 'div.login_row > input#input_username', // Username input inside form (will have form_selector prepended)
	password_selector: 'div.login_row > input#input_password', // Password input inside form
	submit_selector: 'button[type=submit]', // Submit button
	timeout: 10000, // 10s page load timeout
	repeat_before_reload: 10, // Times to repeat submitting before reloading
}
