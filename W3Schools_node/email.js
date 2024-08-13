var nodemailer = require('nodemailer');
const { format } = require('path');

var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'masidaniel02@gmail.com',
        pass: '1Qw-m@ssi'
    }
});

var mailOptions = {
    form: 'masidaniel02@gmail.com',
    to: 'Daniel.Masi@ke.cicinsurancegroup.com',
    subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};


transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});