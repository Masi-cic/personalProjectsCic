const express = require("express");
const bodyPraser = require('body-parser');
var nodeMailer = require('nodemailer');

const app = express();
const route = express.Router();

const transporter = nodeMailer.createTransport({
    port: 465,
    host: "smtp.gmail.com",
    auth: {
        user: 'danm06339@gmail.com',
        pass: '1Qw-masi',
    },
    secure: true,
});

route.post('/text-mail', (req, res) => {
    const { to, subject, text } = req.body;
    const mailData = {
        from: "masidaniel02@gmail.com",
        to: to,
        subject: subject,
        text: text,
        html: '<b>Hey there! </b><br> This is our first message sent with Nodemailer<br/>'
    };

    transporter.sendMail(mailData, (error, info)=>{
        if (error) {
            return console.log(error);
        }
        res.status(200).send({message: "Mail send", message_id: info.messageId});
    });
});


app.use(bodyPraser.json());

app.use(bodyPraser.urlencoded({ extended: false }));


const port = process.env.PORT || 5000;

app.use('/v1', route);
app.listen(port, () => {
    console.log(`server listening on port ${port}`)
})