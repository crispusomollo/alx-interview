#!/usr/bin/node
//the above line species to the interpreter to be used for the script. in this case it is the Node.js
const request = require('request');
//This line imports the 'request' module, to make HTTP requests in Node.js. It allows the script to make API requests to fetch data.
const API_URL = 'https://swapi-api.hbtn.io/api';
//This line defines the base URL for the Star Wars API.

if (process.argv.length > 2) {
  //This condition checks whether command-line arguments are present running the script. 
  //process.argv is an array containing the command-line arguments passed to the Node.js process.
  //process.argv.length is checked to ensure that there is at least one additional argument (beyond the default arguments passed to Node.js).
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    //Here, an HTTP GET request is made to the Star Wars API to fetch information about a specific film. 
    //The process.argv[2] represents the first additional argument provided in the command line (index 0 represents 'node', index 1 represents the script file). 
    //This argument specifies the film ID in the API URL.
    if (err) {
      console.log(err);
    }
    //If an error occurs during the API request, it will be logged to the console.
    const charactersURL = JSON.parse(body).characters;
    //The response body from the API request is parsed as JSON (JSON.parse(body)), and the characters property is extracted. 
    //This property contains URLs to the characters' information related to the specified film.
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));
      //For each character URL fetched from the film data, a new Promise is created. 
      //This Promise is used to make individual requests to the character URLs and resolve with the character names.


    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
//Promise.all is used to handle all the promises created for character names. 
//It waits for all the promises to resolve and then collects the character names in an array (names). 
//Finally, it prints the character names separated by newline characters ('\n') to the console.
