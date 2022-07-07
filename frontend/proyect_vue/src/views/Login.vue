<template>
  <div class="login-caja">
    <img
      class="avatar"
      src="https://e6.pngbyte.com/pngpicture/533159/png-Login-Clipart-Thumb-Image-user-login-png-transparent.png"
      alt="Ingresar Logo"
    />
    <h1>Login</h1>
    <input v-model="codigo" placeholder="Enter your name" /><br />
    <input
      v-model="password"
      type="password"
      placeholder="Enter your password"
    />
    <button @click="login()">Login</button>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      codigo: "",
      password: "",
    };
  },
  methods: {
    async login() {
      this.$router.push({
        name: "registro",
      });
    },
  },
};
</script>

<style scoped>
.login-caja {
  width: 320px;
  height: 420px;
  background: black;
  color: #fff;
  top: 50%;
  left: 50%;
  position: absolute;
  transform: translate(-50%, -50%);
  box-sizing: border-box;
  padding: 70px 30px;
}
.login-caja .avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  position: absolute;
  top: -50px;
  left: calc(50%-50px);
}
.login-caja label {
  margin: 0px;
  padding: 0px;
  font-weight: bold;
  display: block;
}
.login-caja h1 {
  margin: 0;
  padding: 0 0 20px;
  text-align: center;
  font-size: 22px;
}

.login-caja input {
  width: 100%;
  margin-bottom: 20px;
}
.login-caja input[type="text"],
.login-caja input[type="password"] {
  border: none;
  border-bottom: 1px solid white;
  background: transparent;
  outline: none;
  height: 40px;
  color: white;
  font-size: 16px;
}

.login-caja input[type="submit"] {
  border: none;
  outline: none;
  height: 40px;
  background: #b80f22;
  color: white;
  font-size: 18px;
  border-radius: 20px;
}
.login-caja a {
  text-decoration: none;
  font-size: 12px;
  line-height: 20px;
  color: rgb(117, 77, 77);
}
.login-caja a:hover {
  color: white;
}
</style>
