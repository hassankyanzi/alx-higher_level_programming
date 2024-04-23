#!/usr/bin/node

const https = require('https');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

const options = {
    rejectUnauthorized: false
};

https.get(apiUrl, options, (res) => {
    let data = '';

    res.on('data', (chunk) => {
        data += chunk;
    });

    res.on('end', () => {
        const filmData = JSON.parse(data);
        const charactersUrls = filmData.characters;

        charactersUrls.forEach(characterUrl => {
            https.get(characterUrl, options, (res) => {
                let data = '';

                res.on('data', (chunk) => {
                    data += chunk;
                });

                res.on('end', () => {
                    const characterData = JSON.parse(data);
                    console.log(characterData.name);
                });
            });
        });
    });
}).on('error', (err) => {
    console.error('Error:', err.message);
});
