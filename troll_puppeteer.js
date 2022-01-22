/**
  * troll_puppeteer.js
  * "Scammers should go to the nether without gear"
  *
  * Puppeteer script for automating the sending of fake data to drown out real data.
  *
  * This version is made to target discord-to[.]com/new-years
  *
  */

const config = require('./config');
const puppeteer = require('puppeteer');

(async () => {
	const log = (text, error) => { console.log((error ? '[!] ' : '[+] ') + text) };
	const sleep = (ms) => { return new Promise(resolve => setTimeout(resolve, ms)); };
	
	log('Config:');
	log('Debug = ' + config.debug);
	log('Target = ' + config.target);
	log('Button Selector = ' + config.button_selector);
	//log('Frame Selector = ' + config.frame_selector);
	log('Form Selector = ' + config.form_selector);
	log('Username Selector = ' + config.form_selector + ' > ' + config.username_selector);
	log('Password Selector = ' + config.form_selector + ' > ' + config.password_selector);
	log('Submit Button Selector = ' + config.submit_selector);
	log('Timeout = ' + config.timeout);
	log('Times To Submit Before Reloading = ' + config.repeat_before_reload);
	
	log('Starting puppeteer browser');
	const browser = await puppeteer.launch({
		headless: !config.debug,
	});
	
	let times = 0;
	
	while (true) {
		times += 1;
		log('Opening page (' + times + 'x)');
		
		let loaded = false;
		let page;
		
		while (!loaded) {
			log('Opening browser page');
			page = await (async () => {
				const pages = await browser.pages();
				if (pages.length >= 1) {
					return pages[0];
				} else {
					return await browser.newPage();
				}
			})();
			
			log('Navigating to target page');
			try {
				
				await page.goto(config.target);
				await page.goto(config.target); // Overcome an issue with a blank page
			} catch (e) {
				if (e.toString().startsWith('Error: net::ERR_HTTP_RESPONSE_CODE_FAILURE at')) {
					log('Non 2xx code, we probably got 429\'d. Waiting 10s and retrying.', true);
					await sleep(10000);
					continue;
				}
				log(e.toString(), true);
				throw e;
			}
			
			log('Waiting for page to finish loading (timeout: ' + config.timeout + ' ms)');
			try {
				/*await page.waitForNavigation({
					waitUntil: 'networkidle0',
				});*/
				await page.waitForSelector(config.button_selector, {
					visible: true,
					timeout: config.timeout,
				});
				loaded = true;
			} catch (e) {
				if (e.toString().startsWith('TimeoutError')) {
					log('Timed out, retrying...', true);
				} else {
					log(e, true);
					log('Retrying...', true);
				}
			}
		}
		
		log('Sleeping an extra 500ms');
		await sleep(500);
		
		log('Clicking button');
		while (true) {
			try {
				await page.click(config.button_selector);
			} catch (e) {
				log(e, true);
				continue;
			}
			break;
		}
		
		log('Waiting for frame to finish loading');
		//await page.waitForSelector(config.frame_selector, {
		try {
			await page.waitForSelector('iframe', {
				visible: true,
			});
		} catch (e) {
			if (e.toString().startsWith('TimeoutError')) {
				log('Timed out, reloading', true);
			} else {
				log(e, true);
				log('Reloading...', true);
			}
			continue;
		}
		
		
		log('Fetching frame element');
		//const frame_element = await page.$(config.frame_selector);
		const frame_element = await page.$('iframe'); // Instance of ElementHandle
		const frame = await frame_element.contentFrame(); // Instance of Page
		
		log('Waiting for phishing form');
		let login_form;
		try {
			login_form = await frame.waitForSelector(config.form_selector, {
				visible: true,
			});
		} catch (e) {
			if (e.toString().startsWith('TimeoutError')) {
				log('Timed out, reloading', true);
			} else {
				log(e, true);
				log('Reloading...', true);
			}
			continue;
		}
		
		let fills = 0;
		
		const username_field = await frame.$(config.form_selector + ' > ' + config.username_selector);
		const password_field = await frame.$(config.form_selector + ' > ' + config.password_selector);
		
		while (fills < config.repeat_before_reload) {
			fills += 1;
			
			log('Filling out form (' + fills + '/' + config.repeat_before_reload + ')');
			await username_field.type('ImagineBeingAScammer');
			await password_field.type('SussyBaka');
			
			log('Submitting');
			await frame.click(config.submit_selector);
			
			log('Waiting for login button to become available again');
			try {
				await frame.waitForSelector(config.submit_selector, {
					visible: true,
					timeout: config.timeout,
				});
			} catch (e) {
				if (e.toString().startsWith('TimeoutError')) {
					log('Timed out, reloading', true);
				} else {
					log(e, true);
					log('Reloading...', true);
				}
				break
			}
			
			log('Clearing form');
			await username_field.click({clickCount: 3}); // Triple click to select everything
			await username_field.press('Backspace'); // Delete
			await password_field.click({clickCount: 3});
			await password_field.press('Backspace');
		}
	}
})();
