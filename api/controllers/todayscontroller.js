var Feed = require('rss-to-json');



module.exports.todaysfull = function(req, res) {
  Feed.load('https://blog.networks.nokia.com/feed', function(err, rss){
    res
        .status(200)
        .json(rss);
  });

};

//get all headlines
module.exports.todaystitleall = function(req, res) {
  Feed.load('https://blog.networks.nokia.com/feed', function(err, rss){

    var i = 0;
    var titles=[];var headlines;
      for (i = 0; i < rss.items.length; i++){

      headlines = rss.items[i].title;
      titles.push({
        'headline': headlines
      });

      }

      res
        .status(200)
        .send(titles);
  });

};

//get top 5 news
module.exports.articlegetTop= function(req, res) {
    Feed.load('https://blog.networks.nokia.com/feed', function (err, rss) {
        var topfive=rss.items.slice(0,5);
        res
            .status(200)
            .send(topfive);
    });


};


//get title description of one post
module.exports.articlegetOne = function(req, res) {
    Feed.load('https://blog.networks.nokia.com/feed', function(err, rss){

    var articleId=req.params.articleId;

    console.log("Requested article id:"+articleId);
    var article=rss.items[articleId];
    res
        .status(200)
        .send(article);

});

};