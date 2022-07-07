import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "inicio",
    component: Home,
  },
  {
    path: "/details/:slug",
    name: "EnglishDetals",
    component: () =>
      import(
        /* webpackChunkName: "EnglishDetals" */ "../views/EnglishDetals.vue"
      ),
  },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
