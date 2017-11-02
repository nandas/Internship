var express = require('express');
var router = express.Router();

var ctrlHotels = require('../controllers/todayscontroller.js');

router
  .route('/todays')
  .get(ctrlHotels.todaysfull);

router
    .route('/all')
    .get(ctrlHotels.todaystitleall);

router
    .route('/articles/:articleId')
    .get(ctrlHotels.articlegetOne);


router
    .route('/top5')
    .get(ctrlHotels.articlegetTop);
module.exports = router;