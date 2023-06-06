import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/Home.vue'
import NotFound from '@/views/NotFound'
import LoginView from '@/views/LoginView'
import RegisterView from '@/views/RegisterView'
import WorkList from '@/views/WorkList'
import JobDetail from '@/views/JobDetail'
import PostJob from '@/views/PostJob'
import UserInfo from '@/views/UserInfo'
import UserDetailView from '@/views/UserDetailView'

const routes = [
  {
    path: '/gigplatform/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/gigplatform/login/',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/gigplatform/user/',
    name: 'userinfo',
    component: UserInfo,
  },
  {
    path: '/gigplatform/register/',
    name: 'register',
    component: RegisterView,
  },
  {
    path: '/gigplatform/jobs/:jobname',
    name: 'jobs',
    component: WorkList,
  },
  {
    path: '/gigplatform/postjob/',
    name: 'postjob',
    component: PostJob,
  },
  {
    path: '/gigplatform/404/',
    name: '404',
    component: NotFound,
  },
  {
    path: '/gigplatform/:catchAll(.*)',
    redirect: '/gigplatform/404/',
  },
  {
    path: '/gigplatform/job_detail/:jobid',
    name: 'job_detail',
    component: JobDetail,
  },
  {
    path: '/gigplatform/userdetail/',
    name: 'userdetail',
    component: UserDetailView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
