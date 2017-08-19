var path = require('path');
var webpack = require('webpack');
module.exports = {
    entry: './static/js/application.js',
    output: {
        path: path.resolve(__dirname, 'static/js'),
        filename: 'bundle.js',
        publicPath: '/static'
    },
    resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
    }
  },
    plugins: [
        new webpack.ProvidePlugin({
            Vue: 'vue',
        })
    ]
}