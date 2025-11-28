import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', //根路径
      name: 'home', //路由名称
      component: () => import('../views/home/Home.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login/Login.vue'),
    },

    {
      path: '/about',
      name: 'about',
      component: () => import('../views/About.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/Contact.vue')
    },
  ],
})

export default router
