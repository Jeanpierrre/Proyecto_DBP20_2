<template>
  <div>
    <h1>Login</h1>
    <p>Hello {{ name }}</p>
    <form @submit.prevent="login">
      <input v-model="name" placeholder="Enter your name" /><br />
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
      name: "",
      password: "",
    };
  },
};
</script>

<style scoped></style>
