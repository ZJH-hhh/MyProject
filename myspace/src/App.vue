<template>
  <NavBar />
  <router-view :key="$route.fullPath" />
</template>

<script>
// 在根组件引入 bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';
import NavBar from './components/NavBar';

// 需要用到某个组件是要将他 export到components中
export default {
  name: "App",
  components: {
    NavBar,
  }
}
</script>

<style></style>
