// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'Home', component: () => import('@/views/Home.vue'), meta:{ transition: 'fade'} }, 
  // ADD NEW ROUTES HERE
  { path: '/live', name: 'Live', component: () => import('@/views/Live.vue'), meta:{ transition: 'fade'} }, 
  { path: '/control', name: 'Control', component: () => import('@/views/Control.vue'), meta:{ transition: 'fade'} },
  { path: '/analysis', name: 'Analysis', component: () => import('@/views/Analysis.vue'), meta:{ transition: 'fade'} },
  { path: '/global', name: 'Global', component: () => import('@/views/Global.vue'), meta:{ transition: 'fade'} },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
