import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', //根路径
      name: 'home', //路由名称
      component: () => import('../views/Home.vue')
    }
  ],
})

export default router
