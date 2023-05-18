import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LabelSpread from '../views/LabelSpreadView.vue';
import SparkView from '../views/SparkView.vue';

const routes = [
  {
    path: '/graph/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/graph/labelspread/',
    name: 'LabelSpread',
    component: LabelSpread
  },
  {
    path: '/graph/spark/',
    name: 'SparkView',
    component: SparkView
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
