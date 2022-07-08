/*eslint-disable */
<template>
  <div>
    <h1>Administrador</h1>
    <pre>{{ administrador }}</pre>
    <pre>{{ users }}</pre>
    <div v-for="user in users" :key="user.id">
        <h1>{{user.nombres}}</h1> 
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
export default {
  setup() {
    let administrador = ref(null);
    let users = ref(null);
    async function fetchUsuarios(rol) {
      const res = await fetch(`http://127.0.0.1:5000/usuarios/${rol}`);
      const data = await res.json();
      users.value=data['Usuarios'];
    }
    onMounted(async () => {
      administrador.value = await window.localStorage.getItem("user");
      administrador = administrador.value.split(',')
      console.log(administrador.slice(4));
      const rol= administrador.slice(4);
      fetchUsuarios(rol[0].slice(-2,-1));
    });

    return {
      administrador,
      users,
    };
  },
};
</script>

<style lang="scss" scoped></style>
