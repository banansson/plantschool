//document.write("Markup Dump was here!");
//alert("foo");

function mup_Traverse(current) {
  var target = []
  if (current) {
    var tagName = current.tagName;
    if (tagName) {
      target.push(tagName);
      alert("tag: " + tagName);
    }

    var index = 0;
    var currentChild = current.childNodes[index];
    while(currentChild) {
      var childTarget = mup_Traverse(currentChild);
      if (childTarget.length !== 0) {
        target.concat(childTarget);
      }
      index++;
      currentChild = current.childNodes[index]
    }
  }
  return target;
}

var doc = document;
var nodes = doc.body.childNodes;
alert("nodes: " + nodes.length);

var data = mup_Traverse(doc.body);
alert("data: " + data.length);

/*for(n in target) {
  alert(data[n]);
}*/

/*
for(var i = 0; i < nodes.length; i++) {
  if (typeof nodes[i].id !== "undefined") {
    alert(nodes[i].id);
  }
}
*/
