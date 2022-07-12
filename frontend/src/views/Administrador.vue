/*eslint-disable */
/*<pre>{{ users }}</pre>*/
/*<pre>{{ administrador }}</pre>*/

<template>
  <div>
    <div class="box">
      <input
        type="text"
        name="search"
        placeholder="buscar"
        class="src"
        autocomplete="off"
        v-model="searchInput"
        @keyup.enter="searchUser(searchInput)"
      />
    </div>
    <h1>Nombres:</h1>
    <div v-for="user in users" :key="user.id" class="n">
      <h1>{{ user.nombres }}</h1>
    </div>
    <h2>Sede:</h2>
    <div v-for="user in users" :key="user.id" class="h2">
      <h2>{{ user.sede }}</h2>
    </div>
    <h3>Telefono:</h3>
    <div v-for="user in users" :key="user.id" class="h3">
      <h3>{{ user.telefono }}</h3>
    </div>
  </div>
</template>
<script>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

export default {
  setup() {
    let administrador = ref(null);
    let users = ref([]);
    let searchInput = ref('');
    const router = useRouter();
    const route = useRoute();
    async function fetchUsuarios(rol) {
      const res = await fetch(`http://127.0.0.1:5000/usuarios/${rol}`);
      const data = await res.json();
      users.value = data["Usuarios"];
    }

    async function searchUser(value) {
      users.value=[]
      const res = await fetch(`http://127.0.0.1:5000/usuarios/1?search=${value}`);
      const data = await res.json();
      users.value = data["usuario"];
      console.log(users.value)
    }

    onMounted(async () => {
      administrador.value = await window.localStorage.getItem("user");
      administrador = administrador.value.split(",");
      console.log(administrador.slice(4));
      const rol = administrador.slice(4);
      if (rol[0].slice(-2, -1) == 0) {
        router.push("/");
      } else {
        fetchUsuarios(rol[0].slice(-2, -1));
      }
    });
    return {
      administrador,
      users,
      searchUser,
    };
  },
};
</script>
<style  scoped>
h1 {
  font-size: 3rem;

  width: 650px;

  height: 25px;

  top: 50%;
  left: 10%;
  transform: translate(0%, 0%);
  font-size: 22px;
  margin-bottom: 20px;
  font-family: "Times New Roman", Times, serif;
  color: rgb(255, 255, 255);
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.9);
}

h2 {
  width: 650px;
  height: 25px;
  top: 20%;
  left: 10%;
  transform: translate(70%, -550%);
  color: rgb(255, 255, 255);
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.9);
  font-size: 22px;
  margin-bottom: 20px;
  font-family: "Times New Roman", Times, serif;
}

h3 {
  width: 650px;
  height: 25px;

  top: 10%;
  left: 10%;
  transform: translate(150%, -1100%);
  color: rgb(255, 255, 255);
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.9);
  font-size: 22px;
  margin-bottom: 20px;
  font-family: "Times New Roman", Times, serif;
}
.nivel-caja {
  text-align: center;
  width: 400px;
  height: 355px;
  background: #7858587d;
  margin: auto;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 70px 5px;
  border-radius: 20px;
  margin-bottom: 20px;
  font-family: "Times New Roman", Times, serif;
}
.sede-caja {
  text-align: center;

  width: 400px;
  height: 500px;
  top: 50%;
  left: 80%;
  position: absolute;
  transform: translate(-50%, -50%);
  box-sizing: border-box;
  padding: 70px 5px;
  background: #7858587d;
  border-radius: 20px;
}

.nombres {
  width: 320px;
  height: 40px;
  background: rgb(120, 56, 189);
  color: #fff;
  top: 30%;
  left: 20%;
  position: absolute;
  transform: translate(-50%, -50%);
  box-sizing: border-box;
  padding: 25px 35px;
  color: white;
  border-radius: 10px;
}
.nombres-caja {
  text-align: center;
  top: 50%;
  left: 20%;
  width: 400px;
  height: 500px;
  background: #7858587d;
  margin: auto;
  position: absolute;
  position: absolute;
  transform: translate(-50%, -50%);
  box-sizing: border-box;
  padding: 25px 35px;
  color: white;
  border-radius: 10px;
}
.box {
  position: absolute;
  top: 80px;
  left: 50px;
}

input.src {
  padding: 9px 10px 9px 32px;
  outline: none;
  font-size: 18px;
  border-radius: 15px;
  color: #444;
  border: 3px solid #a50559;
  background: #fff
    url("https://static.tumblr.com/ftv85bp/MIXmud4tx/search-icon.png") no-repeat
    9px center;
  width: 60px;
  transition: all 0.5s;
}

input.src:hover {
  width: 180px;
  background-color: #fff;
  border-color: #8c10b3;
  box-shadow: 0 0 5px #6dcff680;
}
</style>


