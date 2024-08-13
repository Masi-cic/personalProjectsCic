const express = require('express')
const app = express()
const PORT = 3000

const homeroute = require("./routes/Home.js")
const loginroute=require("./routes/login") 


const path = require('path')
app.use('/static', express.static(path.join(__dirname, 'Static Files')))
app.get('/file', (req, res) => {
    res.sendFile(path.join(__dirname, 'image_3.jpg'))
})

//define middleware  and routes here 
app.use(express.json());
// app.post('/', (req, res) => {
//     const {name} = req.body;

//     res.send(`welcome ${name}`)
// })

// app.get('/', (req, res)=>
//     res.send('<h1> Hello, world! </h1>')
// );


app.get('/hello', (req, res) => {
    res.set('Content-Type', 'text/html');
    res.status(200).send("<h1> Hello intern! </h1>");
});

app.use("/",homeroute) 
app.use("/",loginroute) 

app.listen(3000, () => {
    console.log(`Server is listening at http://localhost:3000`);
  });


// app.listen(PORT, (error) => {
//     if (!error)
//         console.log(`server is succesfully running and app is listening on port ${PORT}`)
//     else
//         console.log("error occured, server can't start", error)
// })

