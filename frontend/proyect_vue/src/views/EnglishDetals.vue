<template>
  <section>
    <h1>{{ todo.name }}</h1>
    <div class="todo-details">
      <img :src="require(`@/assets/${todo.image}`)" :alt="todo.name" />
      <div>
        {{ todo.description }}
      </div>
    </div>
  </section>
</template>

<script>
import store from "@/store";

export default {
  name: "EnglishDetals",
  data() {
    return {
      todoId: this.$route.params.id,
    };
  },
  computed: {
    todo() {
      return store.todos.find((t) => t.id === parseInt(this.todoId));
    },
  },
};
</script>

<style scoped>
img {
  max-height: 400px;
  max-width: 600px;
}
</style>
