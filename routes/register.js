const express = require('express')
const router = express.Router()
const {registerView} = require('../controllers/loginController')

router.get('/', registerView)

module.exports = router