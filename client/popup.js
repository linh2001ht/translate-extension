function googleTranslate() {

  function callAPI(node) {
    var lang = document.getElementsByTagName('html')[0].lang;
    var currentContent = node.nodeValue.trim();
    if (currentContent !== "") {
        fetch("http:127.0.0.1:8000/api/trans-text/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lang: lang,
                text: currentContent,
            }),
        })
        .then(response => response.json())
        .then(data => {
            var newContent = data.result;
            if (data.ok) {
              var newNode = document.createElement('span');
              newNode.innerHTML = newContent;
              node.parentNode.replaceChild(newNode, node);
            }
            
        })
        .catch(error => console.error('Error:', error));
    }
  }
  
  function Init() {
    console.log('transInit');
    var allTextNodes = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    while (allTextNodes.nextNode()) {
        var node = allTextNodes.currentNode;
        callAPI(node);
    }
  }

  Init();
}

document.getElementById("submit").onclick = async () => {
  const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
  chrome.scripting.executeScript(
    {
      target: { tabId: tabs[0].id },
      world: "MAIN",
      func: googleTranslate
    }
  );
};

