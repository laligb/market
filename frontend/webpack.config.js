const path = require('path');

module.exports = {
  entry: './src/App.js',
  output: {
    path: path.resolve(__dirname, 'build', 'static', 'js'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
