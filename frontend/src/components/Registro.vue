<template>
  <div class="datos-ingreso">
    <form id="form" action="/registros/create" method="POST">
      <h1>Formulario Registro</h1>

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
        v-model="apellidos"
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

      <input type="submit" class="submit" value="Pasar datos" />
    </form>
  </div>
</template>

<script>
import { ref } from "@vue/runtime-core";
export default {
  name: "Registro",
  data() {
    return {
      codigo: ref(""),
      apellido: ref(""),
      edad: ref(""),
      colegio: ref(""),
      numero: ref(""),
    };
  },
  methods: {
    async login() {
      const url = "http://127.0.0.1:5000/registro";
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
