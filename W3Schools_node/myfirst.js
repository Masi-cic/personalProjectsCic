var http = require('http');
var dateTime = require('./myFirstModule'); // importing your own modules

//creation of a server object:
http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'});// this is an http header and shows that the 
    // response should be displayed as HTML 
    res.write("the data and time currently is "+ dateTime.myDatetime());
    res.write('Hello world');
    //the above are responses to the client 
    res.end();// this ends the responses 

}).listen(8080);