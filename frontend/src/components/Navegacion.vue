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
        <button @click="logout()">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Logout</button>
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
button {
  background-color: transparent;
  border: none;
}
.login-box h2 {
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
}
.login-box .user-box {
  position: relative;
}
.login-box .user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  margin-bottom: 30px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}
.login-box .user-box label {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  pointer-events: none;
  transition: 0.5s;
}
.login-box .user-box input:focus ~ label,
.login-box .user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #03e9f4;
  font-size: 12px;
}
.login-box button {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  color: #03e9f4;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: 0.5s;
  margin-top: 40px;
  letter-spacing: 4px;
}
.login-box button:hover {
  background: #03e9f4;
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4,
    0 0 100px #03e9f4;
}
.login-box button span {
  position: absolute;
  display: block;
}
.login-box button span:nth-child(1) {
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #03e9f4);
  animation: btn-anim1 1s linear infinite;
}
@keyframes btn-anim1 {
  0% {
    left: -100%;
  }
  50%,
  100% {
    left: 100%;
  }
}
.login-box button span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, transparent, #03e9f4);
  animation: btn-anim2 1s linear infinite;
  animation-delay: 0.25s;
}
@keyframes btn-anim2 {
  0% {
    top: -100%;
  }
  50%,
  100% {
    top: 100%;
  }
}
.login-box button span:nth-child(3) {
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(270deg, transparent, #03e9f4);
  animation: btn-anim3 1s linear infinite;
  animation-delay: 0.5s;
}
@keyframes btn-anim3 {
  0% {
    right: -100%;
  }
  50%,
  100% {
    right: 100%;
  }
}
.login-box button span:nth-child(4) {
  bottom: -100%;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(360deg, transparent, #03e9f4);
  animation: btn-anim4 1s linear infinite;
  animation-delay: 0.75s;
}
@keyframes btn-anim4 {
  0% {
    bottom: -100%;
  }
  50%,
  100% {
    bottom: 100%;
  }
}
</style>
