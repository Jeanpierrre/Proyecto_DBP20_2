import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "inicio",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "Login" */ "../views/Login.vue"),
  },
  {
    path: "/recibo",
    name: "recibo",
    component: () =>
      import(/* webpackChunkName: "recibo" */ "../views/recibo.vue"),
  },
  {
    path: "/registro",
    name: "registro",
    props: true,
    component: () =>
      import(/* webpackChunkName: "Registro" */ "../components/Registro.vue"),
  },
  {
    path: "/details/:slug",
    name: "EnglishDetals",
    component: () =>
      import(
        /* webpackChunkName: "EnglishDetals" */ "../views/EnglishDetals.vue"
      ),
  },
  {
    path: "/profile",
    name: "profile",
    component: () =>
      import(/* webpackChunkName: "profileUser" */ "../views/Profile.vue"),
  },
  {
    path: "/administrador",
    name: "administrador",
    component: () =>
      import(
        /* webpackChunkName: "administrador" */ "../views/Administrador.vue"
      ),
  },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
