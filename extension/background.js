chrome.tabs.onActivated.addListener(function (activeInfo) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {
        var currentTime = new Date().toLocaleTimeString();
        console.log(`[${currentTime}] Activated tab:`, tab.url);

        // Set a timeout to execute the event after 3 minutes
        setTimeout(function() {
            var currentTime = new Date().toLocaleTimeString();
            console.log(`[${currentTime}] Event triggered after 3 minutes.`);
            // Execute your event here
        }, 180000); // 3 minutes in milliseconds
    });
});

chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.url) {
        var currentTime = new Date().toLocaleTimeString();
        console.log(`[${currentTime}] Updated tab:`, change.url);

        // Set a timeout to execute the event after 3 minutes
        setTimeout(function() {
            var currentTime = new Date().toLocaleTimeString();
            console.log(`[${currentTime}] Event triggered after 3 minutes.`);
            // Execute your event here
        }, 180000); // 3 minutes in milliseconds
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

chrome.tabs.onCreated.addListener(function (tab) {
    

    var currentTime = new Date().toLocaleTimeString();
    console.log(`[${currentTime}] Tab created:`, tab.url);

    // Set a timeout to execute the event after 3 minutes
    setTimeout(function() {
        var currentTime = new Date().toLocaleTimeString();
        console.log(`[${currentTime}] Event triggered after 3 minutes for tab:`, tab.url);
        // Execute your event here
    }, 3000); // 3 minutes in milliseconds
});
