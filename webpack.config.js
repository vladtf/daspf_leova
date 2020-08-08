const path = require('path')

module.exports = {

    mode: 'development',

    entry: './static/js/main.js',

    output: {
        path: path.resolve(__dirname, 'static/assets'),
        filename: 'app.js'
    },

    // module: {
    //     rules: [
    //         {
    //             test: /\.s[ac]ss$/i,
    //             use: [
    //                 // Creates `style` nodes from JS strings
    //                 'style-loader',
    //                 // Translates CSS into CommonJS
    //                 'css-loader',
    //                 // Compiles Sass to CSS
    //                 'sass-loader',
    //             ],
    //         },
    //     ],
    // },
};