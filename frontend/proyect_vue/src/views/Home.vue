<template>
  <NavBar />
  <div class="marco">
    <h1>aa</h1>
  </div>
  <div class="home">
    <div class="todos">
      <div v-for="todo in todos" :key="todo.id">
        <router-link
          :to="{ name: 'EnglishDetals', params: { slug: todo.slug } }"
        >
          <h2>{{ todo.name }}</h2>
        </router-link>
        <figure>
          <router-link
            :to="{ name: 'EnglishDetals', params: { slug: todo.slug } }"
          >
            <img :src="require(`@/assets/${todo.image}`)" :alt="todo.name" />
          </router-link>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import store from "@/store";
import NavBarVue from "@/components/NavBar.vue";
import NavBar from "@/components/NavBar.vue";
export default {
  name: "Home",
  data() {
    return {
      todos: store.todos,
      NavBarVue,
    };
  },
  components: { NavBar },
};
</script>

<style scoped>
img {
  max-width: 200px;
}

.home {
  background-attachment: coral;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}

.todos {
  display: flex;
  background: rgb(28, 57, 221);
  justify-content: space-between;
}

a {
  color: lightseagreen;
  text-decoration: none;
}
.marco {
  z-index: -200;
  width: 320px;
  height: 40px;
  background: rgb(238, 246, 0);
  color: #fff;
  top: 30%;
  left: 20%;
  position: absolute;
  transform: translate(-50%, -50%);
  box-sizing: border-box;
  padding: 25px 35px;
  border-radius: 10px;
}
</style>
