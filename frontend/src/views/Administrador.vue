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

    <h1>Nombres:</h1>
    <h2>Apellidos:</h2>
    <h3>Sedes:</h3>
    <h4>Telefonos:</h4>
    </div>
    <div class="inicio-avanzado">
      <div v-for="user in users" :key="user.id">
    
          <h1>{{ user.nombres }}</h1>
      </div>        
    </div>
    
    <div class="inicio-2">
      <div v-for="user in users" :key="user.id">
          <h1>{{ user.apellidos }}</h1>
      </div>        
    </div>



    <div class="inicio-basico">
      <div v-for="user in users" :key="user.id">
          <h1>{{user.sede}}</h1>
      </div>        
    </div>


    <div class="inicio-intermedio">
      <div v-for="user in users" :key="user.id">
          <h1>{{user.telefono}}</h1>
      </div>        
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


h1{
    color: black;
    font-size:22px ;
    position: relative;
    margin-bottom: 20px;
    
    font-family: 'Times New Roman', Times, serif;
}
h2{
    color: black;
    font-size:22px ;
    position: relative;
 top: 50%;
  left: 37%;
    position: absolute;
    transform: translate(520%,-50%);
    margin-bottom: 20px;
    font-family: 'Times New Roman', Times, serif;
}
h4{
    color: black;
    font-size:22px ;
    position: relative;
 top: 50%;
  left: 37%;
    position: absolute;
    transform: translate(1370%,-50%);
    margin-bottom: 20px;
    font-family: 'Times New Roman', Times, serif;
}

h3{
  color: black;
    font-size:22px ;
    position: relative;
 top: 50%;
  left: 37%;
    position: absolute;
    transform: translate(1520%,-50%);
    margin-bottom: 20px;
    font-family: 'Times New Roman', Times, serif;
    }
.inicio-avanzado{
  width: 300px;
  height:500px;
  top:50%;
  left: 12%;
  position: absolute;
  transform: translate(-50%,-50%);
  box-sizing: border-box;
  padding: 0px 5px;
  background:rgb(208, 136, 29);
  border-radius:20px;
}

.inicio-2{
  width: 300px;
  height:500px;
  background: rgb(210, 28, 28);
  margin:auto;
  position: absolute;
  top: 50%;
  left: 37%;
  transform: translate(-50%,-50%);
  padding: 0px 5px;
  border-radius:20px;
}
.inicio-basico{
  width: 300px;
  height:500px;
  background: rgb(223, 223, 12);
  margin:auto;
  position: absolute;
  top: 50%;
  left: 60%;
  transform: translate(-50%,-50%);
  padding: 0px 5px;
  border-radius:20px;
  }

.inicio-intermedio{
    width: 300px;
    height:500px;
    top:50%;
    left: 85%;
    position: absolute;
    transform: translate(-50%,-50%);
    box-sizing: border-box;
    padding: 0px 5px;
    background:rgb(13, 213, 213);
    border-radius:20px;
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

