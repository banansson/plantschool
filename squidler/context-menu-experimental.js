var extensionName = "Markup Dump";
var debug = true;

function log(message) {
  if (debug) { console.log(extensionName + " | " + message); }
}

var markupdump = { }
markupdump.ContextMenu = function(/*optional*/ options) {
  if (typeof options !== "undefined") {
    // extract options
  }
}

markupdump.ContextMenu.prototype = {
  main: function() {
    var menu = chrome.contextMenus.create({
      "title"   : "Inspect with Markup Dump",
      "contexts": ["all"],
      "onclick" : this._onParse
    });
    return menu;
  },

  _onParse: function(info, tab) {
    chrome.tabs.executeScript(tab.id, {"file": "content-parser.js"});
  },

}

var app = new markupdump.ContextMenu();
menu = app.main();

log("created context menu (id:  " + menu + ")");
