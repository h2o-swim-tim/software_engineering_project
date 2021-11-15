

var SpotifyWebApi = require('spotify-web-api-node');

// credentials are optional
var spotifyApi = new SpotifyWebApi({
  clientId: 'fcecfc72172e4cd267473117a17cbd4d',
  clientSecret: 'a6338157c9bb5ac9c71924cb2940e1a7',
  redirectUri: 'http://www.example.com/callback'
});


spotifyApi.setAccessToken('BQAS477F40VGeWotuMf1ZA7luyC6__BqGP09B_MaZKab3UGzxA-TAgNKA');

//need to add how to ask for a keyword
//var search = window.prompt("Please enter your keyword");

spotifyApi.searchTracks('search')
    .then(function(data) {
      console.log('Search by "search"', data.body);
    }, function(err) {
      console.error(err);
    });

//if (search != null) {
    
//}

console.log('Listening on 8888');
app.listen(8888);
