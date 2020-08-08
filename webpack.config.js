const path = require('path')

module.exports = {

    mode: 'development',

    entry: './static/js/main.js',

    output: {
        path: path.resolve(__dirname, 'static/assets'),
        filename: 'app.js'
    }
}