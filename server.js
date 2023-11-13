// if not production, require dotenv
if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config()
}

// start express server and require view dependencies
const express = require('express')
const app = express()
const expressLayouts = require('express-ejs-layouts')
const bodyParser = require('body-parser')

const indexRouter = require('./routes/index')
const registerRouter = require('./routes/register')

// tell the app to use these dependencies
app.set('view engine', 'ejs')
//app.set('views', __dirname + '/views')
app.set('layout', 'layouts/layout')
app.use(expressLayouts)
app.use(express.static('public'))
app.use(bodyParser.urlencoded({ limit: '10mb', extended: false}))


// connect to mongodb
const mongoose = require('mongoose')
mongoose.connect(process.env.DATABASE_URL)
const db = mongoose.connection
db.on('error', error => console.error(error))
db.once('open', () => console.log('Connected to Mongoose'))

app.use('/', indexRouter)
app.use('/register', registerRouter)

// listen on port 5000
const PORT = process.env.PORT || 5000
app.listen(PORT, console.log("Server is listening on port " + PORT))