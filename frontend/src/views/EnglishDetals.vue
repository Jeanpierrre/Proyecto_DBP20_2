<template>
  <div>
    <section>
      <div>
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
          <div class="espacio">
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
      slug: this.$route.params.slug,
    };
  },
  computed: {
    todo() {
      return store.todos.find((t) => t.slug === this.slug);
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
  white-space: pre;
}
.cards {
  display: flex;
  flex-direction: row;
  margin-left: auto;
  margin-right: auto;
  justify-content: center;
  width: 50%;
}

.espacio {
  white-space: pre-line;
}
.cards img {
  max-height: 250px;
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
