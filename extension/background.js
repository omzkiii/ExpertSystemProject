/** ON ENTER */
function callPyBackend(tab) {
    fetch('http://localhost:5000/send_url', {
            method: 'POST',
            body: 'url=' + encodeURIComponent(tab.url)
        }).then(response => {
            if (response.ok) {
                console.log('URL sent successfully.');
            } else {
                console.error('Failed to send URL.');
                console.error('Failed to send URL:', response.status, response.statusText);

            }
        }).catch(error => { // Catch any network errors
            console.error('Error:', error);
        });
}

chrome.tabs.onActivated.addListener(function (activeInfo) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {


        var currentTime = new Date().toLocaleTimeString();
        //console.log(`[${currentTime}] Activated tab:`, tab.url);

        //console.log(`[${currentTime}] Activated tab:`, websiteName);


        // Send URL to Flask server
        callPyBackend(tab);


        // Check if URL contains "facebook" using regex
        if (/facebook/i.test(tab.url)) {
            // Set a timeout to execute the event after 3 minutes
            setTimeout(function() {
                var currentTime = new Date().toLocaleTimeString();
                console.log(`[${currentTime}] Event triggered after 3 minutes on Facebook.`);
                // Execute your event here
            }, 180000); // 3 minutes in milliseconds
        }
    });
});



/** ON UPDATE PAGE */
chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.url) {
        var currentTime = new Date().toLocaleTimeString();
        console.log(`[${currentTime}] Updated tab:`, change.url);

        callPyBackend(tab);

    }
});

var tabToUrl = {};

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    tabToUrl[tabId] = tab.url;
});

chrome.tabs.onRemoved.addListener(function (tabId, removeInfo) {
    var currentTime = new Date().toLocaleTimeString();
    console.log(`[${currentTime}] Removed tab:`, tabToUrl[tabId]);

    delete tabToUrl[tabId];
});


/** CREATE PAGE */
chrome.tabs.onCreated.addListener(function (tab) {
    

    var currentTime = new Date().toLocaleTimeString();
    console.log(`[${currentTime}] Tab created:`, tab.url);

    callPyBackend(tab);

});
