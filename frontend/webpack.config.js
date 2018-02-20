'use strict'
const path = require('path');
const NODE_ENV = process.env.NODE_ENV || 'dev';
const webpack = require("webpack");
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    context: path.join(__dirname, '/assets'),
    entry: './js/main',
    output: {
        path: path.join(__dirname, '/build'),
        publicPath: '/static/',
        filename: './js/bundle.js'
    },
    watch: NODE_ENV == 'dev',
    devtool: NODE_ENV == 'dev' ? 'source-map' : false,
    devServer: {
        contentBase: [path.join(__dirname, "assets"), path.join(__dirname, "assets", "html")],
        compress: true,
        port: 9000,
    },
    module: {
        loaders: [
            {
                test: /\.(jpg|png|svg)$/i,
                loader: "file-loader?name=[path][name].[ext]",
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader?presets[]=env'
            },
            {
                test: /\.(sass|scss)$/,
                loader: ExtractTextPlugin.extract("css-loader?importLoaders=1!postcss-loader!resolve-url-loader!sass-loader?sourceMap")
            },
            {test: /\.(eot|otf|ttf|woff|woff2)(\?v=\d+\.\d+\.\d+)?$/, loader: 'file-loader?name=fonts/[name].[ext]'},
        ],
    },

    plugins: [
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify(process.env.NODE_ENV)
            }
        }),

        new ExtractTextPlugin({filename: "css/styles.css", disable: false, allChunks: true }),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
        })
    ]
}
