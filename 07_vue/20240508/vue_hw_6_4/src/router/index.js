import { createRouter, createWebHistory } from 'vue-router'
import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'
import StudentView from '@/views/StudentView.vue'
import StudentDetailView from '@/views/StudentDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/students'
    // },
    {
      path: '/',
      name: 'some',
      component: SomeView
    },
    {
      path: '/other',
      name: 'other',
      component: OtherView
    },
    {
      path: '/students',
      name: 'Students',
      component: StudentView
    },
    {
      path: '/students/:name',
      name: 'StudentsDetail',
      component: StudentDetailView
    }
  ]
})

export default router
