<template>
  <body>
    <Navegacion />
    <router-view :key="$route.path" />
  </body>
</template>

<script>
import Navegacion from "./components/Navegacion.vue";

export default {
  name: "App",
  components: {
    Navegacion,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
body {
  font-family: sans-serif;
  margin: 0;

  background-size: cover;
  margin: 0px;
  padding: 0px;
  z-index: -200;
  background: rgb(209, 98, 19);
  height: 100vh;
}
</style>
