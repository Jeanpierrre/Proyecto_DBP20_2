<template>
  <div>
    <h1>Login</h1>
    <p>Hello {{ name }}</p>
    <form @submit.prevent="login">
      <input v-model="codigo" placeholder="Enter your name" /><br />
      <input
        v-model="password"
        type="password"
        placeholder="Enter your password"
      /><br />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      const url = "http://127.0.0.1:5000/login";
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
          codigo: this.username,
          password: this.password,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.log("response: ", response);
      const data = await response.json();
      console.log("data: ", data);
      if (data["success"]) {
        this.$router.push({
          name: "Todos-Manager",
          params: {
            username: data["profile"]["name"],
          },
        });
      }
    },
  },
};
</script>

<style scoped></style>
