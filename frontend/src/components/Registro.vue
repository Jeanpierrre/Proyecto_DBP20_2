<template>
  <div class="login-box">
    <h1>Formulario Registro</h1>
    <div class="user-box">
    <input
      type="text"
      class="control"
      name="codigo"
      placeholder="Ingrese su codigo"
      v-model="codigo"
    />
    <br />
    <input
      type="password"
      class="control"
      name="password"
      placeholder="Ingrese su password"
      v-model="password"
    />
    <br />
    <input
      type="text"
      class="control"
      name="nombres"
      placeholder="Ingrese su nombres"
      v-model="nombres"
    />
    <br />
    <input
      type="text"
      class="control"
      name="apellidos"
      placeholder="Ingrese sus apellidos"
      v-model="apellido"
    />
    <br />
    <input
      type="tel"
      class="control"
      name="telefono"
      placeholder="Ingrese su telefono"
      v-model="telefono"
    />
    <br />
    <input
      type="number"
      class="control"
      name="edad"
      placeholder="Ingrese su edad"
      v-model="edad"
      min = "111111111"
      max = "999999999"
    />
    <br />
    <input
      type="text"
      class="control"
      name="colegio"
      placeholder="Ingrese su colegio"
      v-model="colegio"
    />
    </div>
    <br />
    Selecciona el tipo de nivel que tienes:

    <select id="tipo" name="dificultad" v-model="dificultad">
      <option value="Basico">Basico</option>
      <option value="Intermedio">Intermedio</option>
      <option value="Avanzado">Avanzado</option>
    </select>
    <br />
    <br />
    Selecciona la sede:
    <select id="tipo" name="sede" v-model="sede">
      <option value="English-Miraflores">English-Miraflores</option>
      <option value="English-Barranco">English-Barranco</option>
      <option value="English-SA">English-SA</option>
    </select>
    <br />
    <p>Estoy de acuerdo con <a href="https://es.wikipedia.org/wiki/Flask">Terminos y condiciones</a></p>

    <button @click="registro()" >
      <router-link :to="{ name: 'recibo' }">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
       Registrarse
      </router-link>
    </button> 
    
    
  </div>
</template>

<script>
import { ref } from "@vue/runtime-core";
export default {
  name: "Registro",
  data() {
    return {
      codigo: ref(""),
      password: ref(""),
      nombres: ref(""),
      apellido: ref(""),
      telefono: ref(""),
      edad: ref(""),
      colegio: ref(""),

      dificultad: ref(""),
      sede: ref(""),
    };
  },
  methods: {
    async registro() {
      const url = "http://127.0.0.1:5000/registros";
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
          codigo: this.codigo,
          password: this.password,
          nombres: this.nombres,
          apellidos: this.apellido,
          telefono: this.telefono,
          edad: this.edad,
          colegio: this.colegio,
          dificultad: this.dificultad,
          sede: this.sede,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.log("response: ", response);
      const data = await response.json();
      console.log("data: ", data);
    },
  },
};
</script>

<style scoped>
html {
  height: 100%;
}
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  background: linear-gradient(#141e30, #243b55);
}
.login-box {
  position: absolute;
  top: 55%;
  left: 50%;
  width: 400px;
  padding: 40px;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.5);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.6);
  border-radius: 10px;
  margin: 4em;
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
