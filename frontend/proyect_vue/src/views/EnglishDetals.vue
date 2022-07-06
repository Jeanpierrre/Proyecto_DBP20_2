<template>
  <div>
    <section>
      <div :style="{ 'background-image': 'url(.assets/wallpaper.jpg)' }">
        <h1>{{ todo.name }}</h1>
        <div class="todo-details">
          <img :src="require(`@/assets/${todo.image}`)" :alt="todo.name" />
          <div>
            {{ todo.description }}
          </div>
        </div>
      </div>
    </section>
    <section class="evidences">
      <div class="cards">
        <div
          v-for="evidence in todo.evidences"
          :key="evidence.name"
          class="card"
        >
          <img
            :src="require(`@/assets/${evidence.image}`)"
            :alt="evidence.name"
          />
          <span class="card_text">
            {{ evidence.name }}
          </span>
          <div>
            {{ evidence.description }}
          </div>
        </div>
      </div>
    </section>
  </div>
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
.todo_details {
  display: flex;
  justify-content: space-between;
}
.cards {
  display: flex;
  flex-direction: row;
}
.cards img {
  max-height: 300px;
}

.card {
  padding: 0 20px;
  position: relative;
}

.card__text {
  position: absolute;
  color: white;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 25px;
  font-weight: bold;
  text-decoration: none;
}
</style>
