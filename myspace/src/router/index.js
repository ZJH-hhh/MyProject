import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserList from '../views/UserList.vue'
import UserProfile from '../views/UserProfile.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import NotFound from '../views/NotFound.vue'

const routes = [
  {
    path: '/myspace/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/myspace/userlist/',
    name: 'userlist',
    component: UserList
  },
  {
    path: '/myspace/userprofile/:userid/',
    name: 'userprofile',
    component: UserProfile
  },
  {
    path: '/myspace/login/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/myspace/register/',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/myspace/404/',
    name: '404',
    component: NotFound
  },
  {
    path: '/myspace/:catchAll(.*)',
    redirect: '/myspace/404/',
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
