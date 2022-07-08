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
      type="text"
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
      type="number"
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
    <p>Estoy de acuerdo con <a href="#">Terminos y condiciones</a></p>

    <button @click="registro()"  router-link to="/details/Niveles">

       Submit
    </button>
    <router-link to="/details/Niveles">Listo</router-link>
    
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
.login-box {
  position: absolute;
  top: 50%;
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
</style>

