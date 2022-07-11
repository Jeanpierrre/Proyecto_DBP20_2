<template>
  <div id="nav">
    <p class="logo">English Express</p>
    <ul class="nav-links">
      <li class="links"><router-link to="/">Inicio</router-link> |</li>
      <li v-for="todo in todos" :key="todo.id" class="links">
        <router-link
          :to="{ name: 'EnglishDetals', params: { slug: todo.slug } }"
        >
          {{ todo.name }}
        </router-link>
      </li>
      <li class="links">
        <router-link to="/administrador">Administration</router-link>
      </li>
      <li v-if="administrador==null" class="links">
        <router-link :to="{ name: 'Login' }"> Login </router-link>
      </li>
      <li v-else class="links">
        <button @click="logout()">Logout</button>
      </li>
    </ul>
  </div>
</template>

<script>
import store from "@/store";
import { ref } from "vue";
export default {
  name: "Navegacion",
  setup() {
    let administrador = ref(null);
    let users = ref(null);
    administrador.value = window.localStorage.getItem("user");
    function logout(){
      window.localStorage.removeItem("user");
      administrador.value=null;
    }
    return {
      todos: store.todos,
      administrador,
      logout,
    };
  },
};
</script>

<style scoped>
#nav {
  display: flex;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

.nav-links {
  display: flex;
}

.links {
  padding-right: 20px;
  list-style: none;
}

.links:hover {
  text-decoration: underline;
}

#nav a.router-link-exact-active {
  color: #97c51a;
}
</style>
