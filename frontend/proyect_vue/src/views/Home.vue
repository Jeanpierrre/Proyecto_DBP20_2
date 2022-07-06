<template>
  <div class="home">
    <div class="todos">
      <div v-for="todo in todos" :key="todo.id">
        <router-link :to="{ name: 'EnglishDetals', params: { id: todo.id } }">
          <h2>{{ todo.name }}</h2>
        </router-link>
        <figure>
          <router-link :to="{ name: 'EnglishDetals', params: { id: todo.id } }">
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

export default {
  name: "Home",
  data() {
    return {
      todos: store.todos,
    };
  },
};
</script>

<style scoped>
img {
  max-width: 200px;
}

.home {
  background-attachment: coral;
  max-width: 1400px;
}

.todos {
  display: flex;
  background-attachment: coral;
  justify-content: space-between;
}

a {
  color: lightseagreen;
  text-decoration: none;
}
</style>
