import injectProcessEnv from 'rollup-plugin-inject-process-env';

const plugins = process?.env?.NODE_ENV != 'production' ? [] : [
  injectProcessEnv({
    NODE_ENV: 'production'
  }, {
    exclude: '**/*.css',
    verbose: true
  }),
];

export default {
  plugins: plugins,
  svelte: {
    preprocess: [],
  },
  build: {
    target: "modules",
  },
};