<template>
  <div class="datos-ingreso">
    <form id="form" action="/registros/create" method="POST">
      <h1>Formulario Registro</h1>
      <input
        type="text"
        class="control"
        name="nombre"
        placeholder="Ingrese su nombre"
        v-model="username"
      />

      <input
        type="text"
        class="control"
        name="apellido"
        placeholder="Ingrese su apellido"
        v-model="apellido"
      />

      <input
        type="number"
        class="control"
        name="edad"
        placeholder="Ingrese su edad"
        v-model="edad"
      />

      <input
        type="text"
        class="control"
        name="colegio"
        placeholder="Ingrese su colegio"
        v-model="colegio"
      />

      <input
        type="number"
        class="control"
        name="numero"
        placeholder="Ingrese su numero"
        v-model="numero"
      />

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
      nombre: ref(""),
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
