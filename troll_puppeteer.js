/**
  * This script could not be completed because dfscord[.]com stopped serving the phishing page. 
  *
  * troll_puppeteer.js
  * "Scammers should go to the nether without gear"
  *
  * Puppeteer script for automating the sending of fake data to drown out real data.
  *
  * This version is made to target dfscord[.]com/newyear
  *
  */

const puppeteer = require('puppeteer');

(async () => {
	const browser = await puppeteer.launch({
		headless: false,
		slowMo: 250,
	});
	const page = await browser.newPage();
	await page.goto('https://dfscord.com/newyear');
	
})()
