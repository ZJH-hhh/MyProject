<template>
  <NavBar />
  <SearchWork />
  <router-view :key="$route.fullPath" />
</template>

<script>
// 在根组件引入 bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';
import NavBar from './components/NavBar.vue';
import SearchWork from './components/SearchWork.vue'

export default {
  name: "App",
  components: {
    NavBar,
    SearchWork,
  }
}
</script>

<style></style>
