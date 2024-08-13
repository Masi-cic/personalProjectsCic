const express = require("express")
const router = express.Router()

//handling requestvusing router 
router.get("/home", (req, res, next)=>{
    res.send("This is the homepage request")
 
})

//importing the router 
module.exports = router
