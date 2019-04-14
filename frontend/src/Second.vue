<template>
  <div>
    <h1>Second bundled app </h1>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
  export default {
    name: 'app',
    data() {
      return {
        msg: 'Secondary bundle'
      }
    }
  }
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  h1, h2 {
    font-weight: normal;
  }

  #app ul {
    list-style-type: none;
    padding: 0;
  }

  #app li {
    display: inline-block;
    margin: 0 10px;
  }

  #app a {
    color: #42b983;
  }
</style>
