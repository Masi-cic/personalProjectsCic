var fs = require('fs');
var events = require('events');
var eventEmitter = new events.EventEmitter();

var rs = fs.createReadStream('./demofile.txt');
rs.on('open', function(){
    console.log('the file is open');
});

//creating an event handler
var myEventHandler = function (){
    console.log('i hear a scream');
} 

// assigning the event handler to an event
eventEmitter.on('scream', myEventHandler);

// fire the scream event 
eventEmitter.emit('scream');