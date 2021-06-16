module.exports = {
  rules:
  {
    'no-console': 'off',
  },
  settings: {
    'import/resolver': {
      alias: {
        map: [
          ['@root', '.'],
          ['@repository', './src/repository'],
        ],
        extensions: ['.ts', '.js', '.jsx', '.json'],
      },
    },
  },
  extends: 'airbnb-base',
};
