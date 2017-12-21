fs = require('fs');


fs.readFile('main-2013.json', 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    debugger
    console.log(data);
  });

console.log("hi")