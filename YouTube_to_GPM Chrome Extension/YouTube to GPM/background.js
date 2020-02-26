// Passes URL to http:/localhost:8000/ in an HTTP request
function sendUrl() {
    // Get the currently selected tab
	chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
		// Get full URL address
		var activeUrl = tabs[0].url;
		
		// Makes sure the site loaded is YouTube only
		if (activeUrl.toLowerCase().includes("youtube") || activeUrl.toLowerCase().includes("youtu.be") ) { // site is youtube:
			// Creating HTTP request
		const HTTP = new XMLHttpRequest();			// HTTP request
		const URL  = "http://localhost:8000/";	// HTTP handler's URL
		
		HTTP.open("POST", URL, true);	
		HTTP.send(activeUrl);	// sending the selected tab's URL
		
		HTTP.onreadystatechange=(e)=>{
			// keep this here or it dies
		}
		} else { // site isn't youtube:
			alert("The site: " + activeUrl + " isn't a YouTube site.");
		}
	});
}

// Creates menu item "Convert YouTube Video to GooglePlay Music"
chrome.contextMenus.create({
    id: "convert",
    title: "Convert YouTube Video to GooglePlay Music",
    contexts: ["all"]
});

// Runs sendUrl() when above menu item is clicked
chrome.contextMenus.onClicked.addListener(function(info, tab) {
    if (info.menuItemId == "convert") {
        sendUrl();
    }
});
